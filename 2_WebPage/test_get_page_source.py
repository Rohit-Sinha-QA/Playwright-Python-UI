def test_get_page_source(page):

    page.goto("https://rohit-automation.netlify.app/")

    # Get Page Source (HTML)
    page_source = page.content()
    print(page_source)
