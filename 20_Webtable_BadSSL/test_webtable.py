def test_webtable_rohit(page):

    page.goto("https://rohit-automation.netlify.app/webtable")

    # Locate table
    table = page.locator("#dataTable")

    # 1️⃣ Count Total Columns
    columns = table.locator("thead tr th")
    print("Total Columns:", columns.count())

    # 2️⃣ Count Total Rows
    rows = table.locator("tbody tr")
    print("Total Rows:", rows.count())

    # 3️⃣ Get Data From First Row
    first_row = rows.nth(0).locator("td")
    first_row_data = [first_row.nth(i).inner_text() for i in range(first_row.count())]
    print("First Row Data:", first_row_data)

    # 4️⃣ Validate City where Name = Henry
    for i in range(rows.count()):

        row = rows.nth(i)
        name = row.locator("td").nth(1).inner_text()

        if name == "Henry":
            city = row.locator("td").nth(3).inner_text()
            print("Henry's City:", city)
            assert city == "Boston"
            break