"""
Sentiment analysis module placeholder
Expands mood input analysis by evaluating text sentiment
"""
from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return "positive"
    elif analysis.sentiment.polarity < -0.1:
        return "negative"
    else:
        return "neutral"
