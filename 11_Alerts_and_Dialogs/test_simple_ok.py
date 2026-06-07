def test_simple_ok(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Accept alert
    page.once("dialog", lambda dialog: dialog.accept())

    # Click the button which opens alert
    page.click("#idalert")

    # Optional
    page.wait_for_timeout(2000)
