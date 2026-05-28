from textblob import TextBlob


def analyze_sentiment(reviews):
    """
    Free local sentiment analysis (no API needed)
    """

    text = " ".join(reviews)

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity  # -1 to +1

    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Mixed"

    # simple heuristic summary
    summary = f"Overall sentiment is {sentiment} with score {polarity:.2f}"

    pros = []
    cons = []

    if polarity > 0:
        pros.append("Users generally like the product quality")
        pros.append("Positive customer experience reported")
    else:
        cons.append("Some negative feedback present")
        cons.append("Mixed user satisfaction")

    return {
        "sentiment": sentiment,
        "score": polarity,
        "summary": summary,
        "pros": pros,
        "cons": cons
    }

