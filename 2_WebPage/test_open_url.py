def test_open_url(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/")

    # Sleep (not recommended & optional for debugging)
    page.wait_for_timeout(1000)
