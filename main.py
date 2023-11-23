from time import sleep

from fire import Fire

from botoros import botoros, config, orders


order = orders.CHICKEN_BURRITO


def main():
    driver = botoros.setup()
    driver.get(config.URL)

    for type_, element in order.items():
        print(type_)
        botoros.click(driver=driver, element=element)

    for topping in config.TOPPINGS:
        topping_element = botoros.checkbox(topping)
        print(topping)
        botoros.click(driver=driver, element=topping_element)

    botoros.add_to_order(driver)
    botoros.review_order(driver)
    botoros.enter_email(driver)
    botoros.enter_info(driver)

    for _ in range(2):
        botoros.next(driver)

    sleep(1000)  # Adjust the duration as needed


if __name__ == '__main__':
    Fire(main)
