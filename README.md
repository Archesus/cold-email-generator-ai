# 📬 Cold Email Generator

A powerful Streamlit application that automatically generates personalized cold emails based on job postings. The app scrapes job descriptions from career pages and uses AI (LangChain + Groq) to create tailored emails highlighting your company's relevant capabilities.

## ✨ Features

- **Job Posting Extraction**: Automatically scrapes and parses job postings from provided URLs
- **AI-Powered Email Generation**: Uses LLaMA 3.3 model via Groq API to generate personalized cold emails
- **Portfolio Integration**: Includes relevant company portfolio links in generated emails
- **JSON-Structured Output**: Extracts job details in structured format (role, experience, skills, description)
- **Error Handling**: Robust exception handling for parsing and scraping failures
- **User-Friendly Interface**: Clean, intuitive Streamlit UI for easy interaction

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Simple web framework for data apps
- **LLM**: [LangChain](https://www.langchain.com/) + [Groq API](https://console.groq.com/) - LLaMA 3.3 model for text generation
- **Web Scraping**: BeautifulSoup4 - HTML parsing and data extraction
- **Environment Management**: python-dotenv - Secure API key management

## 🧱 Architecture
<div align="center">
  <img src="Untitled Diagram.drawio.png" alt="Logo" width="100%" height="100%">
</div>

## 🌌 App UI
<div align="center">
  <img src="Screenshot 2025-10-15 233916.png" alt="Logo" width="100%" height="100%">
</div>

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (get one free at [console.groq.com](https://console.groq.com/))
- A virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

## 📦 Project Structure

```
cold-email-generator/
├── app/
│   ├── chains.py          # LangChain configuration and prompts
│   ├── utils.py           # Utility functions (scraping, parsing, etc.)
│   └── main.py            # Core Chain class for job extraction and email generation
├── .env                   # Environment variables (keep secret!)
├── .gitignore            # Git ignore file
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── streamlit_app.py     # Main Streamlit application entry point
```

## 🎯 Usage

### 1. Start the Streamlit App
```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

### 2. Using the Application

1. Enter a valid job posting URL in the input field
2. Click the "Submit" button to scrape and analyze the job posting
3. The app will extract job details and generate a personalized cold email
4. Copy the generated email and customize as needed

## 🔑 Getting a Groq API Key

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Add it to your `.env` file as shown above

## 📝 Requirements

See `requirements.txt` for the complete list. Key dependencies:

```
streamlit>=1.28.0
langchain>=0.1.0
langchain-groq>=0.1.0
langchain-core>=0.1.0
beautifulsoup4>=4.12.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## ⚙️ Configuration

### Changing the LLM Model

In `main.py`, modify the model name:
```python
self.llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Change this
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)
```

### Adjusting Temperature

Lower temperature (0) = more deterministic outputs
Higher temperature (1) = more creative, varied outputs

## 🐛 Troubleshooting

### "No module named 'bs4'" Error
```bash
pip install beautifulsoup4
```

### "ModuleNotFoundError" Issues
Make sure your virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Key Not Found
- Ensure `.env` file exists in the project root
- Verify the key name matches `GROQ_API_KEY`
- Restart the Streamlit app after updating `.env`

### Invalid JSON Parsing
This typically occurs when the job posting is too long. The error is caught and displayed to the user.

## 🔒 Security Notes

- **Never commit your `.env` file** to version control
- Keep your Groq API key private
- Use `.gitignore` to exclude `.env` files
- Regenerate API keys if accidentally exposed

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the amazing LLM framework
- [Groq](https://groq.com/) for providing fast API inference
- [Streamlit](https://streamlit.io/) for the awesome web framework

## 📚 Credits & Inspiration

This project was inspired by and built following the tutorial by **[codebasics](https://github.com/codebasics/)**. Check out their original repository: **[cold-email-ai](https://github.com/codebasics/project-genai-cold-email-generator)**
