# Sentiment Analyzer API

This is a simple Sentiment Analyzer web API built with FastAPI. It takes in a text input and returns whether the sentiment is **positive**, **negative**, or **neutral** based on keyword matching.

## Features

- Sentiment analysis using a basic rule-based approach
- API built using FastAPI
- One test case included using pytest
- Structured with environment variables using Pydantic
- Uses pre-commit for code formatting with Black

## Project Structure

sentiment-analyser/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entry point
│ ├── schemas.py # Request and response models
│ └── utils.py # Sentiment logic
│
├── tests/
│ └── test_app.py # Test file for the API
│
├── venv/ # Virtual environment
├── .pre-commit-config.yaml
├── requirements.txt
└── README.md

## How to Run

1. Clone the repo:
   git clone https://github.com/su-yash00/sentiment-analyzer/tree/master

2. Set up the virtual environment:
   python3 -m venv venv  
   source venv/bin/activate  
   pip install -r requirements.txt

3. Run the app:
   uvicorn app.main:app --reload

4. Open in browser:
   http://127.0.0.1:8000/docs

## Run Tests

PYTHONPATH=$(pwd) pytest

## Example

Input:
{
"text": "I love this product!"
}

Output:
{
"sentiment": "positive"
}

```bash
PYTHONPATH=$(pwd) pytest
```
