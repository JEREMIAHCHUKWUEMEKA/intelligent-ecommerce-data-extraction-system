import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import pandas as pd
import json


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# limit concurrent browser pages
semaphore = asyncio.Semaphore(5)


async def scrape_page(browser, page_number):

    async with semaphore:

        page = await browser.new_page()

        url = BASE_URL.format(page_number)

        print(f"Scraping page {page_number}")

        try:

            await asyncio.sleep(0.5)

            await page.goto(
                url,
                timeout=60000
            )

            await page.wait_for_selector(".product_pod")

            content = await page.content()

            soup = BeautifulSoup(content, "lxml")

            books = []

            for product in soup.select(".product_pod"):

                title = product.h3.a["title"]

                price = product.select_one(".price_color").text.strip()

                availability = product.select_one(".availability").text.strip()

                rating = product.select_one(
                    "p.star-rating"
                )["class"][1]

                books.append({
                    "title": title,
                    "price": price,
                    "availability": availability,
                    "rating": rating
                })

            await page.close()

            return books

        except Exception as e:

            print(f"Error scraping page {page_number}: {e}")

            await page.close()

            return []


async def scrape_all():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        tasks = []

        for i in range(1, 51):
            tasks.append(
                scrape_page(browser, i)
            )

        results = await asyncio.gather(*tasks)

        await browser.close()

        all_books = [
            book
            for page in results
            for book in page
        ]

        return all_books


async def main():

    data = await scrape_all()

    print(f"\nTotal books scraped: {len(data)}")

    df = pd.DataFrame(data)

    df.to_csv(
        "exports/all_books_async.csv",
        index=False
    )

    with open(
        "exports/all_books_async.json",
        "w"
    ) as f:

        json.dump(data, f, indent=4)

    print("Export completed")


asyncio.run(main())
