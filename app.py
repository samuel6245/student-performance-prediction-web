from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")


@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/style.css")
def style():
    return FileResponse("style.css")


@app.get("/script.js")
def script():
    return FileResponse("script.js")

@app.get("/data")
def data():
    return FileResponse('training_model.py')

@app.get('/theory')
def theory():
    return FileResponse('project_theory.txt')

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction[0]}