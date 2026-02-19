def test_fill_example(page):
    page.goto("https://rohit-automation.netlify.app/")

    # Type into Email textbox
    page.get_by_label("Email").fill("admin@example.com")

    # Type into Password textbox
    page.get_by_label("Password").fill("admin123")

    page.wait_for_timeout(2000)
