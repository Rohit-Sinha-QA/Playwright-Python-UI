def test_prompt(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Handle prompt alert + pass text
    page.once("dialog", lambda dialog: dialog.accept("Hello Rohit"))

    # Click the button which opens prompt alert
    page.click("//button[text()='Show Prompt Alert']")

    # Optional
    page.wait_for_timeout(2000)
