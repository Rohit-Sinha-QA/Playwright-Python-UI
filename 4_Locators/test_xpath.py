def test_xpath(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # Fill an input using XPath
    page.locator("xpath=//input[@id='user']").fill("admin")

    # Click a button using XPath based on text
    page.locator("xpath=//a[text()='Forgot password?']").click()

    # Click a link using XPath based on partial text
    page.locator("xpath=//a[contains(text(),'Cli')]").click()

    # Optional wait for demo/debugging
    page.wait_for_timeout(2000)
