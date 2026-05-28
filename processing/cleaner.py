import pandas as pd
import re


def clean_price(price_str):
    """Convert £51.77 → 51.77 (float)"""
    if not price_str:
        return None
    return float(re.sub(r"[^\d.]", "", price_str))


def clean_rating(rating_str):
    """Convert 'Three' → 3"""
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return mapping.get(rating_str, 0)


def clean_availability(text):
    """Extract in-stock number if present"""
    if not text:
        return "Unknown"
    return "In Stock" if "In stock" in text else "Out of Stock"


def clean_dataset(input_file, output_file):
    df = pd.read_csv(input_file)

    print(f"Original rows: {len(df)}")

    # Remove duplicates
    df = df.drop_duplicates(subset=["title"])

    # Clean columns
    df["price"] = df["price"].apply(clean_price)
    df["rating"] = df["rating"].apply(clean_rating)
    df["availability"] = df["availability"].apply(clean_availability)

    # Drop nulls
    df = df.dropna()

    print(f"Cleaned rows: {len(df)}")

    df.to_csv(output_file, index=False)

    return df


if __name__ == "__main__":
    clean_dataset(
        "exports/all_books.csv",
        "exports/clean_books.csv"
    )
