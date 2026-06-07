def test_radio_buttons(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.locator("#idradiobutton2").check()

    # Optional wait
    page.wait_for_timeout(2000)

    page.locator("#idradiobutton1").click()

    # Optional wait
    page.wait_for_timeout(2000)
