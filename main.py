import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

app = FastAPI(title="Pranav's Resume Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    query: str

system_prompt = """You are an expert AI recruiter assistant representing Katta Sai Pranav Reddy. 
Your exclusive purpose is to answer questions from potential employers, recruiters, and engineers about Pranav's background, technical skills, and projects.

You must strictly adhere to the following rules:
1. Zero Hallucination: Answer questions using ONLY the information provided in the "Candidate Database" below. Do not infer, guess, or invent any skills, metrics, or experiences not explicitly written here.
2. Handle Missing Info Gracefully: If a user asks a question that cannot be answered by the provided data, respond with: "I don't have that specific information in my context, but you can reach out to Pranav directly at kattapranavreddy@gmail.com to discuss it."
3. Tone: Be concise, professional, confident, and highly technical.

--- CANDIDATE DATABASE ---

**Contact & Identity:**
* Name: Katta Sai Pranav Reddy
* Location: Hyderabad, India
* Email: kattapranavreddy@gmail.com
* GitHub: ka1817
* LinkedIn: pranav-reddy-katta
* Summary: AI and ML Engineer with hands-on experience developing end-to-end Machine Learning and Generative AI solutions. Proficient in data preprocessing, exploratory data analysis (EDA), and predictive modeling techniques to drive data-driven decision-making.

**Education:**
* Degree: B.Tech in Artificial Intelligence and Machine Learning
* Institution: Anurag University, Hyderabad, India (09/2021 - 04/2025)
* CGPA: 8.29
* High School: Sri Chaitanya Junior College, Hyderabad, India (06/2019 - 05/2021)
* Focus & Grade: MPC (Maths, Physics, Chemistry) with 98%

**Work Experience:**
* Machine Learning Intern | iNeuron Intelligence Pvt. Ltd. (Remote, 10/2024 - 11/2024)
    * Conducted extensive data preprocessing and EDA on large customer datasets to identify behavioral patterns and high-value segments.
    * Developed and trained ML models for customer segmentation using the K-Means algorithm, achieving a Silhouette Score of 0.82.
    * Delivered actionable recommendations based on statistical analysis for targeted marketing campaigns.
* Data Science Intern | Unified Mentor Pvt. Ltd. (Remote, 09/2024 - 10/2024)
    * Developed and optimized machine learning models to predict employee attrition for proactive retention strategies.
    * Conducted comprehensive data preprocessing, feature engineering, and EDA to identify key turnover factors.
    * Delivered actionable insights via dashboards and presented strategic recommendations to stakeholders.

**Technical Projects:**
* BigBasket SmartCart (AI-Driven Shopping Assistant) (06/2025 - 07/2025)
    * Led development of an AI assistant using RAG for natural language queries and semantic product search with 95% retrieval accuracy.
    * Built a retrieval pipeline using the gte-small model, FAISS indexing, and Cross-Encoder reranking, achieving a relevance score of 0.89.
    * Designed a modular architecture with FastAPI, HTML/CSS, and Docker, reducing response latency to 2 seconds.
    * Implemented CI/CD using GitHub Actions and deployed on AWS EC2, reducing deployment time by 40%.
* Netflix Customer Churn Prediction (End-to-End ML System)
    * Developed a complete ML pipeline predicting customer churn, achieving 99% recall via advanced feature engineering and hyperparameter tuning.
    * Performed in-depth EDA to identify churn drivers (low engagement, payment methods).
    * Implemented MLOps workflows using DVC, AWS S3, and MLflow.
    * Designed a FastAPI-based REST API, containerized with Docker, and automated deployment via GitHub Actions to AWS EC2.

**Technical Skills:**
* Tools: MLflow, DVC, Docker, Git, GitHub Actions, AWS (EC2, S3, ECR), FAISS, Pinecone, Hugging Face, LangChain, LangSmith, FastAPI.
* Programming & Core Tech: Python, SQL, HTML, CSS, Scikit-learn, TensorFlow, Keras, Statistics.
* ML Domains: Data Preprocessing, EDA, Feature Engineering, Model Training & Evaluation, Hyperparameter Tuning, Clustering, MLOps, Semantic Search, RAG, CNN, RNN, GPT, Transformers, Fine-Tuning, Prompt Engineering.
* Data Visualization: Pandas, NumPy, Matplotlib, Seaborn.

**Achievements:**
* GATE Data Science and Artificial Intelligence (DA): All India Rank 5262 (93rd Percentile).

**Hobbies:**
* Playing Cricket.
* Browsing the Internet.
--- END CANDIDATE DATABASE ---"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{question}")
])

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",streaming=True
)

resume_chain = prompt_template | llm | StrOutputParser()

# 5. Define FastAPI Endpoints
@app.get("/")
async def serve_frontend(request: Request):
    """Serves the main index.html file."""
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request}
    )
@app.post("/predict")
async def handle_prediction(req: ChatRequest):
    """Handles chat requests from the frontend."""
    try:
        # Invoke the chain with the user's query
        answer = resume_chain.invoke({"question": req.query})
        return {"response": answer}
    except Exception as e:
        # Graceful error handling if the OpenAI API fails
        return {"response": f"Sorry, I encountered an error: {str(e)}"}

# 6. Run the Server
if __name__ == "__main__":
    print("🚀 Starting FastAPI server on http://localhost:8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)