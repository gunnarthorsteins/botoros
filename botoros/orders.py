from botoros import botoros


CHICKEN_BURRITO = {
    'chicken burrito': botoros.Element(sleep_duration_s=0.5, value="#lu-menu > div.MenuItemList_local__3DpMe > div > div:nth-child(1) > div > div:nth-child(13) > div > button > div.MenuItemClassic_box__1Kl6R > div > img"),
    'cheese': botoros.radio_button("Melted Monterey Jack Cheese"),
    'beans_div': botoros.div("Choose Beans"),
    'beans': botoros.radio_button("Black Beans"),
    'grain_div': botoros.div("Choose Grain"),
    'grain': botoros.radio_button("Mexican Rice"),
    'filling_div': botoros.div("Filling"),
    'filling': botoros.radio_button("Seared Pollo Asado"),
    'hot_sauce_div': botoros.div("Add Hot Sauce"),
    'hot_sauce': botoros.checkbox("Verde - Medium"),
    'toppings_div': botoros.div("Add Toppings"),
    'expand_div': botoros.div("Show more"),
}   