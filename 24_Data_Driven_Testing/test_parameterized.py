def test_page_title_simple(page):
    test_data = [
        ("/dashboard/dashboard.html", "Dashboard"),
        ("/webtable", "WebTable"),
        ("/contact/contact", "Contact Us")
    ]
    
    for url, expected_title in test_data:
        page.goto(f"https://rohit-automation.netlify.app{url}")
        assert expected_title in page.title()