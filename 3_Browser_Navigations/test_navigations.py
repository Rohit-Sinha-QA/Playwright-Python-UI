def test_navigations(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/")

    # Go to another page (example)
    page.goto("https://www.google.com")

    # Go Back
    page.go_back()

    # Go Forward
    page.go_forward()

    # Wait for 2 seconds
    page.wait_for_timeout(2000)

    # Refresh Page
    page.reload()
