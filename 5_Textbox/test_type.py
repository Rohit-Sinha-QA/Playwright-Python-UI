def test_type_example(page):
    page.goto("https://rohit-automation.netlify.app/")

    page.get_by_label("Email").type("admin@example.com", delay=100)

    page.get_by_label("Password").type("admin123")

    page.wait_for_timeout(2000)
