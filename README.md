# 📄 PDF Summarizer using AutoGen & Gemini AI

Welcome to the **PDF Summarizer** – an intelligent web application that allows you to **upload any PDF file** and receive a **concise summary and detailed analysis** using Google's **Gemini LLM** and **AutoGen agent architecture**.

# 📌Project Overview
This project combines the power of:
- 🧠 **Generative AI** (Gemini) for summarization and sentiment analysis
- 🤖 **AutoGen multi-agent framework** for modular processing
- 💻 **Flask** for the web interface
- 📚 **PyMuPDF (fitz)** for PDF text extraction

# 🚀 Features of PDF Summarizer AutoGen

| Feature                      | Description |
|-----------------------------|-------------|
| 📄 PDF Upload               | Upload any PDF document through a simple web interface. |
| 🧠 Gemini-Powered Summarization | Uses Google's Gemini model to generate a concise summary of the uploaded PDF content. |
| 🔍 Insightful Analysis      | Extracts key insights and sentiment from the PDF using LLM-based analysis. |
| 💬 Clean HTML Report        | Displays the summary and analysis in a well-formatted HTML report. |
| 🤖 Modular Agent Design     | Uses `autogen`-style agents for extraction, summarization, and analysis – ensuring clean code structure and extensibility. |
| ⚙️ Flask Web App            | Built with Flask for lightweight deployment and smooth browser-based interaction. |
| 🌐 Gemini API Integration   | Securely connects to the Gemini API using an environment variable (`.env` file). |
| 📦 requirements.txt Support | Includes a `requirements.txt` to easily install dependencies and replicate the environment. |

# 📁 Folder Structure

```
PDF-Summarizer-AutoGen/
├── static/                         # Static assets (CSS, JS, images)
│
├── templates/                      # HTML templates
│   ├── landing.html                # Landing page
│   ├── index.html                  # PDF upload interface
│   └── report.html                 # Results display page
│
├── uploads/                        # Stores uploaded PDF files
│
├── .env                            # Environment variables (API key, etc.)
├── app.py                          # Main Flask app and logic
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Files/directories to ignore in Git
```
# Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DHIKSHAMP/pdf-summarizer-autogen.git
   cd pdf-summarizer-autogen
   ```
2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. Create environment variables:

    Create .env.

    Update the variables inside .env with your own values (API key).

5. **Run the python application:**

   ```bash
   python pdf_extraction.py
   ```
6. **Open your browser and go to:**

    ```bash
    http://127.0.0.1:5000
    ```

# 💡 Use Cases

- Students summarizing academic papers or notes
- Professionals analyzing reports or legal documents
- Anyone needing quick insights from large PDFs
# 👤 Author

**DHIKSHA M P**  

🌐 GitHub: [@DHIKSHAMP](https://github.com/DHIKSHAMP)

🔗 LinkedIn: [linkedin.com/in/dhikshamp](https://linkedin.com/in/dhiksha-m-p-095028257)

🌍 Portfolio: [Portfolio](https://sites.google.com/view/dhikshacyber/about)

## ⚖️ License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) – see the [LICENSE](./LICENSE) file for details.

## 🌟 Contributing

💡 Got suggestions or new ideas?  
🛠️ Pull Requests are welcome!  
📧 Contact me if you'd like to collaborate.


