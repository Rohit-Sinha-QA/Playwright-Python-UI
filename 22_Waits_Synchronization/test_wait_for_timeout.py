def test_explicit_wait(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.click("#WaitVisible")

    # Explicit wait (Manual)
    page.wait_for_timeout(5000)

    page.locator("#delayText").is_visible()