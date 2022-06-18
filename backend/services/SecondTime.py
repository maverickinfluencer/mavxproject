from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def coupon_code_verification():
    s = Service('/Users/shariqueaman/Downloads/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    # url = 'https://fashor.com/products/polka-dots-embroidered-straight-kurta-sky-blue'
    url = "https://juniperfashion.com/products/juniper_red_rayon_printed_anarkali_dress?variant=42351081521371"
    res = browser.get(url)
    time.sleep(5)
    try:
        # btn = browser.find_element_by_css_selector(".ajax-submit.action_button.add_to_cart")
        # print(btn)
        if 'juniperfashion' in url:
            # sku = 'NA'
            # title = soup.find('h1', {'class': 'm-0'}).text.strip()
            # price = soup.find('span', {'class': 'money'}).text.strip().replace('Rs.', '').split('.')[0].replace(' ',
            #                                                                                                     '').replace(
            #     ',', '')
            sku = 'NA'
            price = browser.find_elements_by_css_selector(".money")
            if(len(price)>1):
                print(price[1].text)
    except Exception as e:
        print("Got Exception",e)
    finally:
        browser.close()

# coupon_code_verification()