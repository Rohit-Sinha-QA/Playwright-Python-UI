def test_get_title(page):
    page.goto("https://rohit-automation.netlify.app/")

    # Get Title
    title = page.title()
    print(title)
