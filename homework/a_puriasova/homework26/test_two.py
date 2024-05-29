from time import sleep
from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder("First Name").fill("Aleksa")
    page.get_by_placeholder("Last Name").fill("Pur")
    page.get_by_placeholder("name@example.com").fill("name@ex.com")
    page.get_by_text("Female").click()
    page.get_by_placeholder("Mobile Number").fill("1113306331")
    page.locator("#dateOfBirthInput").click()
    page.get_by_label("Previous Month").click()
    page.get_by_label("Previous Month").click()
    page.get_by_label("Previous Month").click()
    page.get_by_role("combobox").nth(1).select_option("2004")
    page.get_by_label("Choose Tuesday, February 10th,").click()
    page.locator("#subjectsInput").fill("m")
    page.get_by_text("Maths", exact=True).click()
    page.locator("#subjectsContainer div").filter(has_text="Maths").nth(1).click()
    page.locator("#subjectsInput").fill("a")
    page.get_by_text("Arts", exact=True).click()
    page.get_by_text("Sports").check()
    page.get_by_text("Music").check()
    page.get_by_placeholder("Current Address").fill("text text text")
    page.locator("#state svg").click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city svg").click()
    page.get_by_text("Gurgaon", exact=True).click()
    # чтобы посмотреть, что все заполнилось
    sleep(5)
    page.get_by_role("button", name="Submit").click()
    # он не может выполнить это действие - там реклама перекрывает, не получается ее закрыть
    # page.get_by_role("button", name="Close").click()
    page.evaluate('document.querySelector("#closeLargeModal").click()')
    sleep(5)
