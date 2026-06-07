def test_login_chaining(page):

    page.goto("https://rohit-automation.netlify.app/")

    # Fill email
    page.locator("#loginForm").get_by_label("Email").fill("admin")

    # Fill password
    page.locator("#loginForm").get_by_label("Password").fill("admin@1234")

    # Click login
    page.locator("#loginForm").get_by_role("button", name="Login").click()

    # optional wait
    page.wait_for_timeout(2000)
