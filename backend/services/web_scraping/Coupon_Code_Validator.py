from selenium import webdriver
import time
#from selenium.webdriver.chrome.service import Service
import re
from selenium.webdriver.chrome.options import Options


# def coupon_code_validator(coupon_code, url):
#     s = Service('/Users/shariqueaman/Downloads/chromedriver')
#     driver = webdriver.Chrome(service=s)
#     coupun_code = coupon_code
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#


def coupon_code_validator(coupon_code, url):
    #vdisplay = Xvfb()
    #vdisplay.start()
    #display = Display(visible=0, size=(800, 800))  
    #display.start()
    #chromeOptions = Options()
    #chromeOptions.headless = True
    DRIVER_PATH = "/usr/local/bin/chromedriver"
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--window-size=1920,1200")
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--remote-debugging-port=9222')
    #s=Service('/home/ubuntu/mavx/mavxproject/backend/linuxchromedriver ')
    driver = webdriver.Chrome(options=chrome_options,executable_path=DRIVER_PATH)
    coupun_code=coupon_code
    url = url
    s = url.split(".com")
    print(s)
    if s[0].find("fashor") > 0:
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
        p_coupun.send_keys(coupun_code)
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
    elif s[0].find("juniper") > 0:
        driver.get(url)
        time.sleep(3)
        size_cart = driver.find_element_by_css_selector('.product-options__section.d-flex.flex-wrap')
        elementList = size_cart.find_elements_by_tag_name("div")
        for x in range(6):
            try:
                driver.execute_script("arguments[0].click();", elementList[x])
                time.sleep(2)
            except:
                print("hi")
        a_cart = driver.find_element_by_css_selector(
            '.btn.btn--full.btn--status.btn--animated.js-product-button-add-to-cart')
        driver.execute_script("arguments[0].click();", a_cart)
        time.sleep(3)
        go_cart = driver.find_element_by_css_selector(
            '.header__btn-cart.position-relative.d-flex.align-items-center.text-nowrap.js-popup-button')
        driver.execute_script("arguments[0].click();", go_cart)
        time.sleep(3)
        product_price = driver.find_element_by_id('stack-discounts-subtotal-value').text
        print(product_price)
        p_coupon = driver.find_element_by_id('coupons_stacker_input')
        p_coupon.send_keys(coupun_code)
        p_coupun_apply = driver.find_element_by_id('coupons_stacker_add_button')
        driver.execute_script("arguments[0].click();", p_coupun_apply)
        time.sleep(5)
        product_price_after = driver.find_element_by_id('stack-discounts-subtotal-value').text
        print(product_price_after)
        res = re.split("₹", product_price_after, 2)[-1]
        print(res)
        if product_price[1:] != res:
            print("hurray juniper")
            return True
        elif product_price[1:] == res:
            print('error juniper')
            return False
    elif (s[0].find("houseofindya") > 0) or (s[0].find("faballey") > 0):
        driver.get(url)
        time.sleep(10)
        size = driver.find_element_by_css_selector(".proSize")
        driver.execute_script("arguments[0].click();", size)
        time.sleep(10)
        a_cart = driver.find_element_by_css_selector(".addbagBtn.addtobag")
        driver.execute_script("arguments[0].click();", a_cart)
        time.sleep(5)
        checkout = driver.find_element_by_css_selector('.headBagitem >a')
        driver.execute_script("arguments[0].click();", checkout)
        time.sleep(5)
        product_price = driver.find_element_by_css_selector('.totlPrice').text
        p_coupun_apply = driver.find_element_by_css_selector('.couponsShow')
        driver.execute_script("arguments[0].click();", p_coupun_apply)
        time.sleep(5)
        p_coupun = driver.find_element_by_id('CouponTxt')
        p_coupun.send_keys(coupun_code)
        p_coupun_apply_final = driver.find_element_by_id('applyCpn')
        driver.execute_script("arguments[0].click();", p_coupun_apply_final)
        time.sleep(5)
        product_price_after = driver.find_element_by_css_selector('.totlPrice').text
        print(product_price)
        print(product_price_after)
        if product_price != product_price_after:
            print("hurray house of indya")
            return True
        elif product_price == product_price_after:
            print('error house of indya')
            return False
    elif s[0].find("rustorange") > 0:
        driver.get(url)
        time.sleep(2)
        a_cart = driver.find_element_by_css_selector(".ProductForm__AddToCart.Button.Button--primary.Button--full")
        driver.execute_script("arguments[0].click();", a_cart)
        time.sleep(3)
        checkout = driver.find_element_by_css_selector('.Cart__Checkout.Button.Button--primary.Button--full')
        driver.execute_script("arguments[0].click();", checkout)
        time.sleep(3)
        product_price = driver.find_element_by_css_selector('.payment-due__price.skeleton-while-loading--lg').text
        p_coupun = driver.find_element_by_id('checkout_reduction_code')
        p_coupun.send_keys(coupun_code)
        p_coupun_apply = driver.find_element_by_id('checkout_submit')
        driver.execute_script("arguments[0].click();", p_coupun_apply)
        time.sleep(5)
        product_price_after = driver.find_element_by_css_selector('.payment-due__price.skeleton-while-loading--lg').text
        print(product_price)
        print(product_price_after)
        if product_price != product_price_after:
            print("hurray rustorange")
            return True
        elif product_price == product_price_after:
            print('error rustorange')
            return False
    else:
        print("NAN")
        return False
    driver.close()

 #   vdisplay.stop()
