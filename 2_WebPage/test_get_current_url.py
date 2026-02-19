def test_get_current_url(page):
    page.goto("https://rohit-automation.netlify.app/")

    # Get Current URL
    current_url = page.url
    print(current_url)
