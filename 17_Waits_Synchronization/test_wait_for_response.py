def test_wait_for_response(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    with page.expect_response("**dashboard.html") as response_info:
        page.reload()

    response = response_info.value
    print("Status Code:", response.status)