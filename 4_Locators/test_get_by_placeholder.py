def test_get_by_placeholder(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # Fill the email input using placeholder text
    page.get_by_placeholder("✉ Enter your email").fill("Hello Playwright")

    # Fill another input if needed
    page.get_by_placeholder("🔒 Enter your password").fill("admin@1234")

    # Optional wait for demo/debugging
    page.wait_for_timeout(2000)
