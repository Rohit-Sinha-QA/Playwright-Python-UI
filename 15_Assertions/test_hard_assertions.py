from playwright.sync_api import expect

def test_assertions(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    # ----- Page Assertions -----
    expect(page).to_have_url("https://rohit-automation.netlify.app/")
    expect(page).to_have_title("Login")

    # ----- Heading Assertions -----
    heading = page.locator("h2")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Welcome To Automation With Rohit")

    # ----- Radio Button Assertions -----
    employee_radio = page.locator("#employee")
    student_radio = page.locator("#student")

    expect(employee_radio).to_be_checked()
    expect(student_radio).not_to_be_checked()

    # ----- Input Field Assertions -----
    email_input = page.locator("#user")
    password_input = page.locator("#pass")

    expect(email_input).to_be_visible()
    expect(password_input).to_be_visible()
    expect(email_input).to_have_attribute("placeholder", "✉ Enter your email")

    # ----- Button Assertions -----
    login_button = page.locator(".login-button")
    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # ----- Link Assertion -----
    forgot_link = page.locator("#forgotPasswordLink")
    expect(forgot_link).to_be_visible()
    expect(forgot_link).to_have_attribute("href", "forgotPassword.html")