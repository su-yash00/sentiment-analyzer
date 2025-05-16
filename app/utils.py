from textblob import TextBlob

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiment = (
        "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    )
    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": sentiment
    }
