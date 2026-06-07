def test_show_hide_textbox(page):
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.click("#show-textbox")

    # Wait until textbox is attached to DOM
    page.wait_for_selector("#displayed-text", state="attached")

    # Wait until textbox is visible
    page.wait_for_selector("#displayed-text", state="visible")

    # Optionally, type something
    page.fill("#displayed-text", "Hello Rohit")

    page.click("#hide-textbox")

    # Wait until textbox is hidden (still in DOM)
    page.wait_for_selector("#displayed-text", state="hidden")

    # Remove textbox manually to demonstrate detached
    page.evaluate("document.querySelector('#displayed-text').remove()")

    # Wait until textbox is detached (removed from DOM)
    page.wait_for_selector("#displayed-text", state="detached")