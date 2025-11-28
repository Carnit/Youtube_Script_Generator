# AI-Powered YouTube Script Generator

A command-line tool that leverages Google's Gemini model through LangChain to automatically generate comprehensive YouTube video scripts from a single topic prompt.

This project simplifies the content creation process by providing a structured, ready-to-use script, including a title, hook, main points, conclusion, and relevant tags.

## Features

- **Automated Script Generation:** Creates a full script structure based on a user-provided topic.
- **Structured Output:** Uses Pydantic to ensure the output is always a well-formed object with all necessary components.
- **Key Script Elements:** Generates:
  - A catchy, SEO-friendly title.
  - An engaging hook to capture viewer attention.
  - A clear introduction.
  - Bulleted main content points.
  - A strong conclusion with a call-to-action.
  - A list of relevant YouTube tags for discoverability.
  - An estimated video duration.
- **Interactive CLI:** Simple and easy-to-use command-line interface.

## Tech Stack

- **Python 3.9+**
- **LangChain:** For orchestrating the interaction with the language model.
- **Google Gemini API:** The underlying generative AI model.
- **Pydantic:** For data validation and defining the output schema.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Carnit/UT_AI_training.git>
cd projects/langchain_project
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate
# or 
uv venv 
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
# or
uv sync
```

### 4. Set Up Environment Variables

You need a Google API key to use the Gemini model.

1. Create a file named `.env` in the root of the project directory.
2. Add your Google API key to the `.env` file:

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

## How to Run

Once the setup is complete, you can run the script from your terminal:

```bash
python main.py
# or 
uv run main.py
```

The script will then prompt you to enter a video topic.

### Example Interaction

🎬 Enter your video topic: The history of the internet in 5 minutes

⏳ Generating script...

✅ Script Generated:

Title: The Internet in 5 Minutes: From ARPANET to Your Pocket
