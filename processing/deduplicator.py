import pandas as pd


def remove_duplicates(file_path, output_path):
    df = pd.read_csv(file_path)

    before = len(df)

    df = df.drop_duplicates(subset=["title", "price"])

    after = len(df)

    print(f"Removed {before - after} duplicates")

    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    remove_duplicates(
        "exports/all_books.csv",
        "exports/dedup_books.csv"
    )

