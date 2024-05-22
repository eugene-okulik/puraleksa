from time import sleep
from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    sleep(3)
    page.get_by_placeholder("First Name").fill("Aleksa")
    page.get_by_placeholder("Last Name").fill("Pur")
    page.get_by_placeholder("name@example.com").fill("name@ex.com")
    page.get_by_text("Female").click()
    page.get_by_placeholder("Mobile Number").fill("111330633")
    page.locator("#dateOfBirthInput").click()
    page.get_by_label("Previous Month").click()
    page.get_by_label("Previous Month").click()
    page.get_by_label("Previous Month").click()
    page.get_by_role("combobox").nth(1).select_option("2004")
    page.get_by_label("Choose Tuesday, February 10th,").click()
    page.locator("#subjectsInput").fill("hgjkhkj")
    page.get_by_text("Sports").check()
    page.get_by_text("Music").check()
    page.get_by_placeholder("Current Address").fill("text text text")
    page.locator("#state svg").click()
    # это написала с кодогеном потому что так было удобнее, сама бы не догадалась поставить exact=True
    # если это можно было сделать по другому - напиши пожалуйста
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city svg").click()
    page.get_by_text("Gurgaon", exact=True).click()
    page.get_by_role("button", name="Submit").click()
    sleep(5)
