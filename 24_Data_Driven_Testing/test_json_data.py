import json

def test_json_data(page):
    with open("21_Data_Driven_Testing//test_json.json") as f:
        pages = json.load(f)

    for page_data in pages:
        page.goto(f"https://rohit-automation.netlify.app{page_data['url']}")
        assert page_data["title"] in page.title()
        page.wait_for_timeout(1000)
