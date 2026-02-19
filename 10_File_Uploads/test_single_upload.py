def test_single_upload(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # direct upload file with its path
    page.locator("#idfileupload").set_input_files("D:/Playwright-Python-UI/pic.jpg")

    # Optional
    page.wait_for_timeout(1000)
