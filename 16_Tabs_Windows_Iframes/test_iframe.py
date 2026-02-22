def test_iframe(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Switch to iframe
    frame = page.frame_locator("#iframe-id")

    # Fill email field inside iframe
    frame.locator("#user").fill("Hello Rohit")

    page.wait_for_timeout(2000)