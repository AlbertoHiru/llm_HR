
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MAX_CHARS = 20000

def _trim_text(text):
    return text[:MAX_CHARS]


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_question(text, question):
    prompt = f"""Usando únicamente el siguiente documento, responde esta pregunta: {question}

Documento:
{_trim_text(text)}"""
    return _call_groq(prompt)

def summarize(text):
    prompt = f"""Resume el siguiente documento de forma clara y concisa:

{_trim_text(text)}"""
    return _call_groq(prompt)

def generate_flashcards(text):
    prompt = f"""Genera 10 flashcards del siguiente documento. 
Formato: Pregunta: ... / Respuesta: ...

{_trim_text(text)}"""
    return _call_groq(prompt)

def generate_exam(text):
    prompt = f"""Crea un examen de 5 preguntas de opción múltiple basado en el siguiente documento.
Incluye 4 opciones por pregunta e indica la respuesta correcta al final.

{_trim_text(text)}"""
    return _call_groq(prompt)


def _call_groq(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        
    )
    return completion.choices[0].message.content