from time import sleep

from fire import Fire

from botoros import botoros, config, orders




def main(is_bowl: bool = False):
    driver = botoros.setup()
    driver.get(config.URL)

    order = orders.CHICKEN_BOWL if is_bowl else orders.CHICKEN_BURRITO

    for type_, element in order.items():
        print(type_)
        botoros.click(driver=driver, element=element)
        # sleep(100)

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


if __name__ == "__main__":
    Fire(main)
