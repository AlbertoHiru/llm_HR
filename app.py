import os
from flask import Flask, request, jsonify, render_template
from pdf_reader import extract_text_from_pdf
from ai_assistant import ask_question, summarize, generate_flashcards, generate_exam

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

pdf_text = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global pdf_text
    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    pdf_text = extract_text_from_pdf(file_path)
    return jsonify({"message": "PDF cargado correctamente"})

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    response = ask_question(pdf_text, question)
    return jsonify({"response": response})

@app.route("/summarize", methods=["POST"])
def summarize_route():
    response = summarize(pdf_text)
    return jsonify({"response": response})

@app.route("/flashcards", methods=["POST"])
def flashcards():
    response = generate_flashcards(pdf_text)
    return jsonify({"response": response})

@app.route("/exam", methods=["POST"])
def exam():
    response = generate_exam(pdf_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)