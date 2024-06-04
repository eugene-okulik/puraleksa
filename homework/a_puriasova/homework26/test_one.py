from playwright.sync_api import Page


def test_one(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    press_authentication = page.get_by_role("link", name="Form Authentication")
    press_authentication.click()
    field1 = page.get_by_role('textbox', name="username")
    field1.fill("Aleksa")
    field2 = page.get_by_role("textbox", name="Password")
    field2.fill("12345")
    page.get_by_role("button", name=" Login").click()