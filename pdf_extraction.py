import os
from dotenv import load_dotenv
import fitz  # PyMuPDF for PDF extraction
import google.generativeai as genai
import autogen
from flask import Flask, render_template, request

# Load API key from .env file
load_dotenv()
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

# Flask App
app = Flask(__name__)

# Custom Gemini LLM function for Autogen
def gemini_llm(prompt):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Summarize or analyze the given content.",
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    return response.text.strip()

# Define PDF Extraction Agent
class PDFExtractorAgent(autogen.Agent):
    def extract_text(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text if text else "No readable text found."

# Define Summarization Agent
class SummarizationAgent(autogen.Agent):
    def __init__(self, name="Summarizer"):
        super().__init__(name)
    
    def summarize(self, text):
        prompt = f"Give a consise summary about the following text:\n\n{text}"
        return gemini_llm(prompt).replace("**", "<strong>").replace("</strong><strong>", "</strong>")

# Define Analysis Agent
class AnalysisAgent(autogen.Agent):
    def __init__(self, name="Analyzer"):
        super().__init__(name)
    
    def analyze(self, text):
        prompt = f"Analyze this text for key insights and sentiment:\n\n{text}"
        return gemini_llm(prompt).replace("**", "<strong>").replace("</strong><strong>", "</strong>")

# Define Manager Agent
class ManagerAgent:
    def generate_report(self, pdf_path):
        text = pdf_extractor.extract_text(pdf_path)
        summary = summarizer.summarize(text)
        analysis_raw = analyzer.analyze(text)
        lines = analysis_raw.split("*")
        analysis = "<ul>" + "".join(f"<li>{line.strip()}</li>" for line in lines if line.strip()) + "</ul>"
        # Structured Report with Bold Formatting
        report = f"""
        <strong>📌 PDF Report</strong><br><br>
        <strong>📖 Summary:</strong><br>{summary}<br><br>
        <strong>🔍 Analysis:</strong><br>{analysis}
        """
        return report

# Instantiate Agents
pdf_extractor = PDFExtractorAgent()
summarizer = SummarizationAgent()
analyzer = AnalysisAgent()
manager = ManagerAgent()

# Flask Routes
@app.route('/')
def landing():
    print("Rendering landing.html")
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Save the file
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    # Generate the report
    final_report = manager.generate_report(file_path)

    return render_template('report.html', report=final_report)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)


