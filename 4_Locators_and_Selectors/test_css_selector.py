def test_css_selector(page):

    # Open the website
    page.goto("https://rohit-automation.netlify.app/")

    # tagname#id or #id
    page.locator("css=input#user").fill("admin")

    # tagname#id or #id
    page.locator("css=input#pass").fill("admin@1234")

    # tagname.classname or .classname
    page.locator("css=span.toggle-icon").click()

    # tagname[attribute='value'] or [attribute='value']
    page.locator("css=button[type='submit']").click()

    # Optional wait for demo/debugging
    page.wait_for_timeout(2000)
