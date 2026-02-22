import csv

def test_csv_pages(page):
    with open("21_Data_Driven_Testing//test_csv.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            page.goto(f"https://rohit-automation.netlify.app{row['url']}")
            assert row["title"] in page.title()
            page.wait_for_timeout(1000)
