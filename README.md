# 🕷️ AI Scrapper

AI Scrapper is a simple yet powerful web scraping and parsing tool built with **Streamlit**, **Selenium**, and **LangChain** powered by **Ollama (LLaMA 3)**. It lets you extract content from any webpage, clean it up, and then extract specific information using LLM-based natural language parsing.

---

## 🚀 Features

- ✅ Scrape content from any URL using a headless browser.
- 🧹 Clean and sanitize web content for easier processing.
- 📄 View and explore the scraped DOM content.
- 💬 Ask the LLM to extract specific data from the scraped page using plain English.
- 🔗 Powered by `Ollama` and `LLaMA 3` through LangChain.

---

## 🧱 Project Structure

.
├── main.py # Streamlit frontend interface
├── parse.py # LLM-based parser using LangChain and Ollama
├── scrape.py # Web scraping and content processing
├── README.md # This file
└── requirements.txt #python dependencies to run this project

## ⚙️ Requirements

- Python 3.11+
- Google Chrome + Chromedriver (path configured in `scrape.py`)
- [Ollama](https://ollama.com/) with LLaMA 3 installed locally
- Dependencies (see below)

---

## 🧪 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-scrapper.git
cd ai-scrapper
```
2. Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Start Ollama and ensure llama3 is available
```bash
ollama run llama3
```
5. Run the app

```bash
streamlit run main.py
```

---

✍️ How to Use
Enter a website URL and click Scrape Site.

Review the cleaned DOM content if needed.

Type your natural language prompt describing what info you want to extract (e.g., "List all product names and prices").

Click Parse Content and let the LLM do the work.

🔒 Notes
This project assumes the LLM (Ollama) is running locally and accessible.

Avoid scraping websites that disallow bots (check robots.txt).

Not optimized for JavaScript-heavy or single-page applications (SPA) that need dynamic rendering.

🧠 Example Use Cases
Extract product information from e-commerce sites.

Summarize article content from news websites.

Pull contact details or FAQs from business websites.


