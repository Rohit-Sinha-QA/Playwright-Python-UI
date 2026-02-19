def test_another_way(page):
    page.goto("https://rohit-automation.netlify.app/")

    # Type into Email textbox
    page.fill("//input[@id='user']", "admin@example.com")

    page.wait_for_timeout(2000)
