from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    polarity: float
    subjectivity: float
    sentiment: str
