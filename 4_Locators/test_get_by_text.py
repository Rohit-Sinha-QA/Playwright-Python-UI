def test_get_by_text(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # Click a button or link using visible text
    page.get_by_text("Login").click()

    # Verify heading by visible text
    text = page.get_by_text("Welcome To Automation With Rohit")
    print(text.inner_text())

    # Optional wait for demo/debugging
    page.wait_for_timeout(2000)
