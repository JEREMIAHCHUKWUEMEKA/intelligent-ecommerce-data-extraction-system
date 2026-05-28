import pandas as pd
from sentiment_analysis import analyze_sentiment


def run_ai_analysis(file_path):
    df = pd.read_csv(file_path)

    results = []

    for _, row in df.iterrows():

        reviews = [
            f"{row['title']} is good",
            f"Price is {row['price']} and quality is decent",
            f"Users rated it {row['rating']} stars experience"
        ]

        analysis = analyze_sentiment(reviews)

        results.append({
            "title": row["title"],
            "analysis": analysis
        })

    return results


if __name__ == "__main__":
    output = run_ai_analysis("exports/clean_books.csv")

    for item in output[:2]:
        print("\n" + "="*50)
        print(item["title"])
        print(item["analysis"])
