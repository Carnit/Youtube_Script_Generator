# AI-Powered YouTube Script Generator

A modern web application powered by **Streamlit**, **LangChain**, and **Google Gemini** that automatically generates comprehensive YouTube video scripts from a single topic prompt.

## Overview

Creating engaging YouTube scripts can be time-consuming and challenging. This project streamlines the content creation process by leveraging AI to generate well-structured, ready-to-publish scripts. Simply enter your video topic, and the application will generate a complete script with all the essential elements needed for a professional YouTube video.

The application uses an interactive web interface built with Streamlit, making it accessible and user-friendly for both technical and non-technical users.

## Key Features

- **AI-Powered Script Generation:** Automatically generates comprehensive YouTube scripts using Google's Gemini model
- **Interactive Web Interface:** User-friendly Streamlit interface for easy interaction
- **Structured Output:** Uses Pydantic models to ensure consistent, well-formed script output
- **Complete Script Components:**
  - SEO-optimized, catchy title
  - Engaging hook to capture viewer attention
  - Well-structured introduction
  - Detailed main content sections with key points
  - Strong conclusion with call-to-action
  - YouTube-relevant tags for discoverability
  - Estimated video duration
  - Subtitles and speaker notes
- **Real-time Processing:** Get your script within seconds

## How It Works

1. Enter your video topic or description
2. The AI analyzes your input and generates a structured script
3. The script is formatted and displayed with all components
4. Copy and use the script directly for your YouTube video

## Tech Stack

- **Python 3.13+** - Core programming language
- **Streamlit** - Web UI framework for interactive application
- **LangChain** - LLM orchestration and chain management
- **Google Gemini API** - State-of-the-art generative AI model
- **Pydantic** - Data validation and schema definition
- **Python-dotenv** - Environment variable management

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.13 or higher
- A Google Gemini API key (get it from [Google AI Studio](https://aistudio.google.com/app/apikeys))
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Carnit/Youtube_Script_Generator.git
cd Youtube_Script_Generator
```

### 2. Create a Virtual Environment

```bash
# Using Python venv
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Alternatively, if you prefer using `uv`:

```bash
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Or using uv
uv sync
```

### 4. Configure Environment Variables

1. Create a `.env` file in the project root directory:

```bash
touch .env  # On macOS/Linux or Create manually on Windows
```

2. Add your Google API key to the `.env` file:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

⚠️ **Important:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

## Running the Application

Once the setup is complete, you can run the Streamlit application:

```bash
# Using streamlit directly
streamlit run main.py

# Or using uv
uv run streamlit run main.py
```

The application will start and be accessible at `http://localhost:8501` in your web browser.

### Usage

1. **Open the Application:** Navigate to `http://localhost:8501`
2. **Enter a Topic:** Type your YouTube video topic in the input field
3. **Generate Script:** Click the generate button or press Enter
4. **View Results:** The application will display your generated script with all components
5. **Copy and Use:** Copy the script and use it for your YouTube video

### Example Topics

The application works well with topics like:

- "The Future of Artificial Intelligence"
- "How to Learn Programming in 2025"
- "A Beginner's Guide to Cryptocurrency"
- "10 Productivity Tips for Remote Workers"
- "The History of Video Games"

## Project Structure

```bash

Youtube_Script_Generator/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables (not in version control)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── venv/                 # Virtual environment (not in version control)
```

## Environment Variables

The application requires the following environment variable:

- `GOOGLE_API_KEY` - Your Google Gemini API key

## Troubleshooting

### "API Key not configured" Error

- Ensure your `.env` file is in the root directory
- Verify the `GOOGLE_API_KEY` is set correctly
- Restart the Streamlit application after setting the key

### "Module not found" Error

- Ensure you've activated the virtual environment
- Run `pip install -r requirements.txt` again

### Script Generation Timeout

- Check your internet connection
- Verify your Google API key is valid
- Try with a simpler topic

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

**Carnit** - [GitHub Profile](https://github.com/Carnit)

## Acknowledgments

- [LangChain](https://www.langchain.com/) - For powerful LLM orchestration
- [Streamlit](https://streamlit.io/) - For the intuitive web framework
- [Google Gemini](https://gemini.google.com/) - For the amazing AI model
- [Pydantic](https://docs.pydantic.dev/) - For robust data validation

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/Carnit/Youtube_Script_Generator/issues).
