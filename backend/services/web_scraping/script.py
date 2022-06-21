from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def webscrap():
    DRIVER_PATH = "/usr/local/bin/chromedriver"
    # DRIVER_PATH = '/Users/shariqueaman/Downloads/chromedriver'
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=chrome_options, executable_path=DRIVER_PATH)
    coupon_code = 'MANSI#10'
    url = 'https://fashor.com/collections/maverick-influencers/products/gota-pintuck-striped-straight-kurta-magenta-pink'
    driver.get(url)
    time.sleep(3)
    a_cart = driver.find_element_by_class_name("purchase-details__buttons ").click()
    time.sleep(5)
    go_cart = driver.find_element_by_css_selector('.icon-cart.mini_cart.dropdown_link')
    driver.execute_script("arguments[0].click();", go_cart)
    time.sleep(3)
    checkout = driver.find_element_by_css_selector('.action_button.add_to_cart')
    driver.execute_script("arguments[0].click();", checkout)
    time.sleep(3)
    product_price = driver.find_element_by_css_selector('.payment-due__price.skeleton-while-loading--lg').text
    p_coupun = driver.find_element_by_id('checkout_reduction_code')
    p_coupun.send_keys(coupon_code)
    p_coupun_apply = driver.find_element_by_id('checkout_submit')
    driver.execute_script("arguments[0].click();", p_coupun_apply)
    time.sleep(5)
    product_price_after = driver.find_element_by_css_selector('.payment-due__price.skeleton-while-loading--lg').text
    print(product_price)
    print(product_price_after)
    if product_price != product_price_after:
        print("hurray fashor")
        return True
    elif product_price == product_price_after:
        print('error fashor')
        return False
    driver.quit()
