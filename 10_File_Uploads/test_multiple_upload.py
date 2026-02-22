def test_multiple_upload(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # direct upload files with its path in form of list
    page.locator("#fileInput").set_input_files([
        "D:/Playwright-Python-UI/pic.jpg",
        "D:/Playwright-Python-UI/pic2.jpg"
    ])

    page.wait_for_timeout(1000)
