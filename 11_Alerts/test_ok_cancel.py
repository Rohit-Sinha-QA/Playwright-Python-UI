def test_ok_cancel(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Accept alert
    page.once("dialog", lambda dialog: dialog.accept())

    # Click the button which opens alert
    page.click("//button[text()='Show Confirm Alert']")

    # Optional
    page.wait_for_timeout(2000)

    # Dismiss alert
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Click the button which opens alert
    page.click("//button[text()='Show Confirm Alert']")

    # Optional
    page.wait_for_timeout(2000)
