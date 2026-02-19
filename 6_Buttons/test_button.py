def test_buttons(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    # Click buttons
    page.locator("//button[text()='Login']").click()

    # Optional wait
    page.wait_for_timeout(2000)
