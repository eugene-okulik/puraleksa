import time
from playwright.sync_api import Page, expect


def test_confirm_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.once("dialog", lambda dialog: dialog.accept())
    # Нажимаем на кнопку, чтобы появился алерт
    page.get_by_role("link", name="Click").click()
    # Проверяем, что на странице в секции "You selected" написано "Ok"
    result_text = page.get_by_text("Ok", exact=True)
    expect(result_text).to_be_visible()
    time.sleep(5)
