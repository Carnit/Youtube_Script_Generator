import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List
import datetime

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="YouTube Script Generator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Define the script structure using Pydantic
class ScriptSection(BaseModel):
    title: str
    content: str
    sub_points: List[str]


class YouTubeScript(BaseModel):
    title: str
    hook: str
    introduction: str
    main_sections: List[ScriptSection]
    conclusion: str
    tags: List[str]
    estimated_duration: str


# Prompt + LLM setup
class ScriptGenerator:
    def __init__(self, google_api_key: str, temperature: float = 0.7):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=google_api_key,
            temperature=temperature,
            max_output_tokens=3000,
        )
        self.parser = PydanticOutputParser(pydantic_object=YouTubeScript)

    def generate(
        self, topic: str, mood: str, duration: str, target_audience: str, tone: str
    ) -> YouTubeScript:
        current_year = datetime.datetime.now().year
        prompt = PromptTemplate(
            input_variables=["topic", "mood", "duration", "audience", "tone", "year"],
            template="""You are a helpful YouTube content assistant. Generate a COMPLETE and FULL script based on the following parameters:

Topic: {topic}
Mood: {mood}
Duration: {duration}
Target Audience: {audience}
Tone: {tone}
Current Year: {year}

Generate a FULL DETAILED SCRIPT (not just outlines) with:
- A catchy title that matches the {mood} mood
- A hook (1-2 sentences) that appeals to {audience}
- A complete introduction in a {tone} tone
- 4-6 main sections, each with:
  * A section title
  * Full detailed content (2-3 sentences minimum)
  * 2-4 sub-points for that section (these are bullet points under each main section)
- A strong conclusion with a call-to-action
- 5-8 relevant YouTube tags incorporating {year}
- Estimated duration appropriate for {duration}

Format each main section as an object with title, content, and sub_points list.

{format_instructions}
            """,
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        chain = prompt | self.llm | self.parser
        return chain.invoke(
            {
                "topic": topic,
                "mood": mood,
                "duration": duration,
                "audience": target_audience,
                "tone": tone,
                "year": current_year,
            }
        )


# Main Streamlit UI
def main():
    st.title("🎬 YouTube Script Generator")
    st.markdown("Generate engaging YouTube scripts powered by AI")

    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("❌ Please set your GOOGLE_API_KEY in the .env file.")
        return

    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown("### Configure your script generation preferences")

        # Time/Duration settings
        st.subheader("⏱️ Video Duration")
        duration = st.radio(
            "Expected video length:",
            options=["Short (5-10 mins)", "Medium (10-20 mins)", "Long (20+ mins)"],
            help="This affects the depth and number of points in your script",
        )

        # Mood settings
        st.subheader("😊 Mood & Tone")
        mood = st.selectbox(
            "Select mood:",
            options=[
                "Professional",
                "Casual",
                "Humorous",
                "Educational",
                "Inspirational",
                "Energetic",
            ],
            help="The overall emotional tone of the script",
        )

        tone = st.selectbox(
            "Select tone:",
            options=[
                "Formal",
                "Conversational",
                "Storytelling",
                "News Report",
                "Tutorial",
            ],
            help="How the content should be presented",
        )

        # Target audience
        st.subheader("👥 Target Audience")
        target_audience = st.selectbox(
            "Who is your audience?",
            options=[
                "Beginners",
                "Intermediate Users",
                "Advanced/Experts",
                "General Public",
                "Kids",
                "Professionals",
            ],
            help="Tailor the content complexity and language",
        )

        # Temperature (creativity level)
        st.subheader("🎲 Creativity Level")
        temperature = st.slider(
            "Creativity level:",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher values = more creative, Lower values = more consistent",
        )

        st.divider()
        st.info("💡 Tip: Adjust these settings to customize your script generation!")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        topic = st.text_input(
            "📝 Enter your video topic:",
            placeholder="e.g., 'How to learn Python programming'",
            help="Provide a clear topic for your YouTube video",
        )

    with col2:
        generate_button = st.button(
            "🚀 Generate Script", type="primary", use_container_width=True
        )

    # Generate script on button click
    if generate_button:
        if not topic.strip():
            st.warning("⚠️ Please enter a topic first!")
        else:
            with st.spinner("⏳ Generating your script..."):
                try:
                    generator = ScriptGenerator(api_key, temperature=temperature)
                    script = generator.generate(
                        topic=topic,
                        mood=mood,
                        duration=duration,
                        target_audience=target_audience,
                        tone=tone,
                    )

                    # Display results
                    st.success("✅ Script Generated Successfully!")

                    # Title
                    st.header(script.title)

                    # Tabs for different sections
                    tab1, tab2, tab3, tab4 = st.tabs(
                        ["Overview", "Full Script", "Metadata", "Export"]
                    )

                    with tab1:
                        st.subheader("Hook")
                        st.write(script.hook)

                        st.subheader("Introduction")
                        st.write(script.introduction)

                        st.subheader("Duration")
                        st.info(f"⏱️ {script.estimated_duration}")

                    with tab2:
                        st.subheader("📖 Full Script")

                        for i, section in enumerate(script.main_sections, 1):
                            st.subheader(f"{i}. {section.title}")
                            st.write(section.content)

                            if section.sub_points:
                                st.markdown("**Key Points:**")
                                for sub_point in section.sub_points:
                                    st.markdown(f"  • {sub_point}")
                            st.divider()

                        st.subheader("📝 Conclusion")
                        st.write(script.conclusion)

                    with tab3:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("🏷️ Tags")
                            tags_display = ", ".join(script.tags)
                            st.code(tags_display, language="text")
                        with col2:
                            st.subheader("📊 Statistics")
                            st.metric("Number of Sections", len(script.main_sections))
                            total_sub_points = sum(
                                len(s.sub_points) for s in script.main_sections
                            )
                            st.metric("Total Sub-Points", total_sub_points)
                            st.metric("Number of Tags", len(script.tags))

                    with tab4:
                        # Export as text
                        sections_text = ""
                        for i, section in enumerate(script.main_sections, 1):
                            sections_text += f"{i}. {section.title}\n"
                            sections_text += f"{section.content}\n\n"
                            if section.sub_points:
                                sections_text += "Key Points:\n"
                                for sub_point in section.sub_points:
                                    sections_text += f"  • {sub_point}\n"
                                sections_text += "\n"

                        script_text = f"""
TITLE: {script.title}

HOOK:
{script.hook}

INTRODUCTION:
{script.introduction}

MAIN SECTIONS:
{sections_text}

CONCLUSION:
{script.conclusion}

TAGS:
{", ".join(script.tags)}

ESTIMATED DURATION:
{script.estimated_duration}
"""
                        st.download_button(
                            label="📥 Download Script as Text",
                            data=script_text,
                            file_name=f"youtube_script_{topic[:20]}.txt",
                            mime="text/plain",
                        )

                except Exception as e:
                    st.error(f"❌ Error generating script: {str(e)}")


if __name__ == "__main__":
    main()
