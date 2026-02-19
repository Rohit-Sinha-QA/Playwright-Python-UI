def test_another_way(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    # Click buttons
    page.click("//button[text()='Login']")

    # Optional wait
    page.wait_for_timeout(2000)
