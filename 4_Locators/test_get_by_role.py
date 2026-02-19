def test_get_by_role(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # Fill textbox
    page.get_by_role("textbox", name="Email").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin@1234")

    # Click button
    page.get_by_role("button", name="Login").click()

    # Click link
    page.get_by_role("link", name="Log Out").click()

    # Verify page heading
    heading = page.get_by_role("heading", name="Welcome To Automation With Rohit")
    print(heading.inner_text())

    # Optional wait for demo
    page.wait_for_timeout(2000)
