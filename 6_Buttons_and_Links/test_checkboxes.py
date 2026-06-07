def test_checkboxes(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.locator("#idcheckbox1").check()

    # Optional wait
    page.wait_for_timeout(2000)

    page.locator("#idcheckbox2").click()

    # Optional wait
    page.wait_for_timeout(2000)

    page.locator("#idcheckbox1").uncheck()

    # Optional wait
    page.wait_for_timeout(2000)
