from app.utils import analyze_sentiment

def test_positive_sentiment():
    result = analyze_sentiment("I love this product")
    assert result["sentiment"] == "positive"
