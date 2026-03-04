from fastapi import FastAPI
import os

app = FastAPI(title="DevOps Portfolio API")

@app.get("/")
def home():
    return {"message": "Hello from Vishnuvardhan's DevOps Portfolio API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "local")}
