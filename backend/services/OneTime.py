import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
from selenium.webdriver.support.ui import WebDriverWait
import time


def one_time():
    google_service = GoogleSheetsService()
    s = Service('/home/sharique/Documents/drivers/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    url = 'https://www.haulpack.com/influencers'
    res = browser.get(url)
    time.sleep(10)
    influencer_div = browser.find_element_by_id('influencersDiv')
    lists = influencer_div.find_elements_by_partial_link_text("Visit Store")
    urls = []
    new_list = []
    for list in lists:
        urls.append(list.get_attribute("href"))
    for ind in range(len(urls)):
        if(ind>797):
            print(urls[ind])
            new_list.append(urls[ind])
    for influencer_url in new_list:
        browser.get(influencer_url)
        time.sleep(5)
        try:
            top = browser.find_element_by_css_selector(".col-12.d-flex.align-items-center.profile_left_sec_mgn")
            name = top.find_element_by_css_selector(".name.profile_space_top")
            top_mid = top.find_element_by_css_selector(".display_only_in_desktop_flex.align-items-center")
            middle = top_mid.find_element_by_css_selector(".d-flex.align-items-center")
            last = middle.find_elements_by_tag_name("a")
            output = []
            influencer_name = name.text
            youtube_url = ""
            insta_url = ""
            facebook_url = ""
            for i in range(len(last)):
                if(last[i].get_attribute("href").__contains__("youtube")):
                    youtube_url = last[i].get_attribute("href")
                elif(last[i].get_attribute("href").__contains__("facebook")):
                    facebook_url = last[i].get_attribute("href")
                elif(last[i].get_attribute("href").__contains__("instagram")):
                    insta_url = last[i].get_attribute("href")
            print(f"influencer_name = {influencer_name}")
            print(f"youtube_url = {youtube_url}")
            print(f"insta_url = {insta_url}")
            print(f"facebook_url= {facebook_url}")
            output.append((
                influencer_name,youtube_url,insta_url,facebook_url
            ))
            google_service.add_row(model=output,tab_range="result",spread_sheet_id="1-68xhTxN001aa5UlWwxfIbx1jNJPkdskOq0ssQck_4c")
        except Exception as e:
            print("got exception.",e)
def mhs():
    google_service = GoogleSheetsService()
    s = Service('/home/sharique/Documents/drivers/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    b_urls = []
    b_urls.append('https://www.myhaulstore.com/mhs-influencer?page=1&per-page=60')
    b_urls.append('https://www.myhaulstore.com/mhs-influencer?page=2&per-page=60')
    b_urls.append('https://www.myhaulstore.com/mhs-influencer?page=3&per-page=60')
    i=0
    in_url = "https://www.myhaulstore.com/my-store/monica-singh"
    for b_url in b_urls:
        browser.get(b_url)
        time.sleep(5)
        influencer_urls = []
        try:
            trend_bar = browser.find_element_by_class_name("trend-bar")
            row = trend_bar.find_element_by_class_name("row")
            links = row.find_elements_by_partial_link_text("Visit Store")
            for link in links:
                i+=1
                print(link.get_attribute("href"))
                influencer_urls.append(link.get_attribute("href"))
            print(f"total incluencers = {i}")
            for influencer_url in influencer_urls:
                output = []
                i_name = ""
                y_link = ""
                time.sleep(3)
                try:
                    browser.get(influencer_url)
                    store_mem = browser.find_element_by_class_name("store-mem")
                    name = store_mem.find_element_by_class_name("store-mem-info")
                    i_name = name.text
                    share = store_mem.find_element_by_css_selector(".hidden-xs.col-sm-4")
                    last = share.find_element_by_tag_name("a")
                    y_link = last.get_attribute("href")
                    output.append((
                        i_name,y_link
                    ))
                    google_service.add_row(model=output, tab_range="result",
                                           spread_sheet_id="1plInTq3E3oRE4vzCmkV5kXH4xwGH0IyszTRsUNZvkNg")
                except Exception as e:
                    print("got exception in influencer",e)
        except Exception as e:
            print("got exception in URLS ",e)