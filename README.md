# AskMyDocs

AskMyDocs es un asistente inteligente que te permite conversar con tus documentos PDF. Sube un archivo y podrás hacerle preguntas, obtener resúmenes, generar flashcards y crear exámenes usando inteligencia artificial.

---

## Funcionalidades

- Preguntas y respuestas sobre el contenido del documento
- Resumen automático
- Generación de flashcards con conceptos clave
- Mini examen con preguntas de opción múltiple

---

## Tecnologías

- Python 3.10+
- Flask
- Groq API (llama-3.3-70b-versatile)
- PyMuPDF (lectura de PDFs)

---

## Instalación

Clona el repositorio y entra a la carpeta:

```bash
git clone https://github.com/AlbertoHiru/llm_HR.git
cd askmydocs
```

Crea y activa el entorno virtual:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz del proyecto y agrega tu API key de Groq. Puedes obtenerla gratis en console.groq.com:

```
GROQ_API_KEY=tu_api_key_aqui
```

Ejecuta la aplicación:

```bash
python app.py
```

Abre tu navegador en: [http://localhost:5000](http://localhost:5000)

---

## Estructura del proyecto

```
askmydocs/
├── app.py               # Servidor Flask principal
├── pdf_reader.py        # Extracción de texto del PDF
├── ai_assistant.py      # Lógica de comunicación con Groq
├── templates/
│   └── index.html       # Interfaz web con Tailwind CSS
├── uploads/             # PDFs subidos por el usuario
├── .env                 # API Key (no subir a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Notas

Se recomienda usar PDFs de máximo 50 páginas para mejores resultados. El sistema procesa hasta 20,000 caracteres del documento para mantenerse dentro del límite de tokens de Groq. El archivo `.env` está incluido en `.gitignore` para proteger tu API key. Necesitas conexión a internet para usar la API de Groq.