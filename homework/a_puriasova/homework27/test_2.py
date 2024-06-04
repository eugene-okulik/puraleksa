import time

import pytest
from playwright.sync_api import Page, expect, BrowserContext


def test_new_tab(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")

    # Ожидаем открытие нового таба
    with context.expect_page() as page1_info:
        page.get_by_role("link", name="Click").click()
    page1 = page1_info.value

    # Переключаемся на новый таб и проверяем текст
    new_tab_content = page1.get_by_text("I am a new page in a new tab")
    expect(new_tab_content).to_have_text("I am a new page in a new tab")

    # Переключаемся обратно на исходную страницу и проверяем, что кнопка активна
    page.bring_to_front()
    button = page.get_by_role("link", name="Click")
    expect(button).to_be_enabled()
