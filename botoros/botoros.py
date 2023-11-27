from dataclasses import dataclass
from functools import partial
from time import sleep
from typing import Callable

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
    NoSuchElementException,
)

from botoros import config


@dataclass
class Element:
    value: str
    by: By = By.CSS_SELECTOR
    sleep_duration_s: float = 0


def checkbox(text: str) -> Element:
    return Element(f'input[type="checkbox"][aria-label="{text} "]')


def click(driver: webdriver.Chrome, element: Element) -> None:
    sleep(element.sleep_duration_s)

    while True:
        try:
            driver.find_element(element.by, element.value).click()
            return

        except (
            ElementNotInteractableException,
            ElementClickInterceptedException,
            NoSuchElementException,
            AttributeError,
        ):
            continue


def div(text: str) -> Element:
    return Element(by=By.XPATH, value=f"//*[text()='{text}']")


def enter_email(driver: webdriver.Chrome) -> None:
    email = invent_email()
    element = driver.find_element(By.CLASS_NAME, "CheckEmail_input__1kYnI")
    element.send_keys((email, Keys.ENTER))
    sleep(1)


def enter_info(driver: webdriver.Chrome) -> None:
    for entry, value in config.USER.items():
        sleep(0.1)
        element = driver.find_element(By.XPATH, f'//input[@placeholder="{entry}"]')
        element.send_keys(value)


def invent_email() -> str:
    response = requests.get(config.RANDOM_NUMBER_URL)
    random_number = int(response.text.strip())

    return config.BASE_EMAIL.replace("INTEGER", str(random_number))


def radio_button(text: str) -> Element:
    return Element(
        f'input[type="radio"][aria-label="{text} "]'
    )  # The space between the text and the closing quote is essential!


def setup() -> webdriver.Chrome:
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")  # To disable cookies
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the browser window

    return driver


add_to_order: Callable[[webdriver.Chrome], None] = partial(
    click,
    element=Element(by=By.ID, value="menuItemDetail-addItemButton", sleep_duration_s=2),
)
next: Callable[[webdriver.Chrome], None] = partial(
    click,
    element=Element(
        by=By.XPATH,
        value='//*[@id="main-content"]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/button',
        sleep_duration_s=1,
    ),
)
review_order: Callable[[webdriver.Chrome], None] = partial(
    click,
    element=Element(
        by=By.XPATH,
        value='//*[@id="lu-order"]/div/div/div[3]/div[3]',
        sleep_duration_s=0.5,
    ),
)
