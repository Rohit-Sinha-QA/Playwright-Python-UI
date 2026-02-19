def test_get_by_label(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # Fill the Username input using label text
    page.get_by_label("Email").fill("admin")

    # Fill the Password input using label text
    page.get_by_label("Password").fill("admin@1234")

    # Optional wait for demo/debugging
    page.wait_for_timeout(2000)
