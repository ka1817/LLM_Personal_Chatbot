# 🚀 Pranav's AI Resume Assistant

An intelligent, AI-powered conversational agent designed to act as an expert recruiter assistant representing Katta Sai Pranav Reddy. Built with **FastAPI**, **LangChain**, and **Groq (LLaMA 3.3 70B)**, this application allows potential employers and recruiters to interactively query Pranav's background, technical skills, and projects.

---

## ✨ Features

* **Conversational AI Interface:** Allows users to ask natural language questions about the candidate's resume.
* **Strict Hallucination Control:** The system prompt restricts the AI to answer *only* using the predefined Candidate Database, ensuring 100% factual accuracy regarding the candidate's profile.
* **Graceful Fallbacks:** Directs users to contact the candidate directly for queries outside the scope of the provided database.
* **High-Performance LLM:** Utilizes Groq's blazing-fast inference engine with the `llama-3.3-70b-versatile` model.
* **Modern Web Interface:** Serves a frontend UI using Jinja2 templates and static assets.
* **Automated CI/CD Pipeline:** Fully dockerized with GitHub Actions for automated builds, Docker Hub integration, and continuous deployment to Render.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **AI/LLM:** LangChain, ChatGroq
* **Frontend:** HTML/CSS/JS (Jinja2 Templates)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Deployment:** Render (via Deploy Hook), Docker Hub

---

## 📂 Project Structure

Based on the repository structure (as seen in `image_555587.png`), the project is organized as follows:

```text
RAG/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions pipeline for Docker build & Render deployment
├── notebook/              # Jupyter notebooks for experimentation and testing
├── static/                # Static assets (CSS, JavaScript, images)
├── templates/
│   └── index.html         # Frontend Jinja2 template
├── venv/                  # Python virtual environment
├── .dockerignore          # Exclusions for Docker build
├── .env                   # Environment variables (API keys)
├── .gitignore             # Exclusions for Git version control
├── Dockerfile             # Container configuration
├── main.py                # Core FastAPI application and LangChain logic
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies 

📬 Contact

Katta Sai Pranav Reddy

Email: kattapranavreddy@gmail.com

LinkedIn: https://www.linkedin.com/in/pranav-reddy-katta/

GitHub: https://github.com/ka1817