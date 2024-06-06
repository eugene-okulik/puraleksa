from playwright.sync_api import Page, expect


def test_dynamic_properties(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")

    # Ожидаем, пока кнопка изменит цвет на красный
    button = page.locator("#colorChange")
    expect(button).to_have_class("mt-4 text-danger btn btn-primary", timeout=10000)  # Устанавливаем тайм-аут 10 секунд

    # Нажимаем на кнопку
    button.click()
