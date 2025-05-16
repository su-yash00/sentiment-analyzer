from fastapi import FastAPI
from app.schemas import TextRequest, SentimentResponse
from app.utils import analyze_sentiment

app = FastAPI()

@app.post("/analyze", response_model=SentimentResponse)
def analyze(request: TextRequest):
    result = analyze_sentiment(request.text)
    return result
