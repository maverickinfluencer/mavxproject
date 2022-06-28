from urllib.parse import urlparse
import requests
import json
import time
from services.descriptionGenerator.PriceInfo import get_product_data
import random
from services.googlesheets.GoogleSheetsService import GoogleSheetsService
import re


def get_homepage_link(product_links):
    for link in product_links:
        parsed = urlparse(link)
        return 'https://' + parsed.netloc


def get_after_discount_price(original_price, discount):
    return int(original_price - ((discount / 100) * original_price))


def get_utm_campaign(name, brand, month, discount):
    return name + '_' + brand + '_' + month + str(discount)


def get_utm_link(original_link, utm_campaign):
    if '?' in original_link:
        return original_link + '&utm_source=youtube&utm_medium=maverick&utm_campaign=' + utm_campaign
    else:
        return original_link + '?utm_source=youtube&utm_medium=maverick&utm_campaign=' + utm_campaign


def get_shortend_link(long_link):
    time.sleep(2)
    headers = {'Authorization': 'Bearer 62bc203ade942dba3a485c965fb69a3f01cace1f', 'Content-Type': 'application/json'}
    data = {
        'long_url': long_link.replace('\n', ''),
        'domain': 'fash.la',
        'group_guid': 'Bl46gSjWbYD'
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json.dumps(data))
    short_link = json.loads(response.text)['link']
    return short_link


def get_short_link_if_exisits(long_link, df):
    return df.loc[df['long_link'] == long_link]


def get_brand_info():
    google_service = GoogleSheetsService()
    return google_service.get_brand_info()
def get_brand_hashTag(brand_name):
    brand_info = get_brand_info()
    for item in brand_info:
        if item[0] == brand_name:
            return item[3]
    return []
def get_brand_discount(brand_name):
    google_service = GoogleSheetsService()
    brand_info = google_service.get_brand_info()
    for item in brand_info:
        if item[0] == brand_name:
            return item[2]
    return []


def get_description(influencer_name, coupon_code, campaign_month, brand_name, uncleaned_links):
    print('Generating description for: {}'.format(influencer_name))
    output_str = ''
    price_info = ''
    name = influencer_name
    discount = int(get_brand_discount(brand_name))
    coupon_code = coupon_code
    month = campaign_month
    brand = brand_name
    utm_campaign = get_utm_campaign(name, brand, month, discount)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    uncleaned_tuples = re.findall(regex, uncleaned_links)
    product_links = []
    for x in range(len(uncleaned_tuples)):
        product_links.append(uncleaned_tuples[x][0])
    print(product_links)
    temp_hashtags = get_brand_hashTag(brand_name)
    print(temp_hashtags)
    hashtags = temp_hashtags.replace("\n"," ")
    utm_product_links = []
    title_list = []
    price_list = []
    discounted_price_list = []
    short_links = []

    for link in product_links:
        utm_link = get_utm_link(link, utm_campaign)
        utm_product_links.append(utm_link)
        product_data = get_product_data(utm_link)
        title_list.append(product_data[1])
        price_list.append(int(
            product_data[2].replace('₹', '').replace(' ', '').replace('.', '').replace(',', '').replace('Rs',
                                                                                                        '').replace("'",
                                                                                                                    '')))
        discounted_price_list.append(get_after_discount_price(int(
            product_data[2].replace('₹', '').replace(' ', '').replace('.', '').replace(',', '').replace('Rs',
                                                                                                        '').replace("'",
                                                                                                                    '')),
            discount))
        short_links.append(get_shortend_link(utm_link))
    title_list, price_list, discounted_price_list, short_links = zip(
        *sorted(zip(title_list, price_list, discounted_price_list, short_links), reverse=True))
    homepage_link = get_shortend_link(get_utm_link(get_homepage_link(product_links), utm_campaign))
    e1 = random.choice(['🎊', '🔆', '🎉'])
    e2 = random.choice(['🔸', '🌈', '☀️', '👉', '🎈', '📌', '🛍️', '🎀', '🔹', '👗', '🌸'])
    e3 = '👉'
    first_line = random.choice([
        'Use my coupon code "{}" and get a {} {}% DISCOUNT {} on {} \nWebsite Link: {} {}'.format(
            coupon_code, e1, discount, e1, brand, e3, homepage_link),
        'Get a {} {}% DISCOUNT {} on {} by using my coupon code "{}" \nWebsite Link: {} {}'.format(
            e1, discount, e1, brand, coupon_code, e3, homepage_link),
        '{}  {}% off  {} on {}! Use my coupon code "{}" and shop top designer Kurtis!\nWebsite Link: {} {}'.format(
            e1, discount, e1, brand, coupon_code, e3, homepage_link),
        'Enjoy {} {}% off {} by using my coupon code "{}" on {}! \nWebsite Link: {} {}'.format(
            e1, discount, e1, coupon_code, brand, e3, homepage_link)])
    desc = random.choice([
        'Explore designer Kurtis online at {}. From A-line Kurti, and Anarkali Kurti to cotton Kurtis, Sequins and '
        'Fancy Kurtis, and embroidered Kurtis, {} is the one-stop solution for all party wear and festive branded '
        'Kurtis at {}. You can buy Kurti for women online with an easy return policy. Get partywear cheap Indian '
        'Kurtis online under budget with upto {}% discount with my code {}!'.format(
            brand, brand, brand, discount, coupon_code),
        'Get Designer Kurtis online at {}. Buy Anarkali Kurtis, Cotton Kurtis and Aline Kurtis Online, Sequins and '
        'Fancy Kurtis. {} has all the party wear and festive branded kurta sets that you need! Explore Kurtis for '
        'women online with the easy return policy. Explore Indian Kurtis online under budget with up to {}% discount '
        'with my code {}!'.format(
            brand, brand, discount, coupon_code),
        'Check out stylish Kurti, sleeveless Kurtis and designer Kurtis at {}! From short Kurtis to long Kurtis, '
        'Kurti dresses, ladies Kurti, {} has everything. Get affordable and cheap Kurti for women online with an easy '
        'return policy and exciting offers! Use my code {} and get up to {}% discount on selected designer Kurtas for '
        'women!'.format(
            brand, brand, coupon_code, discount),
        'Enjoy {}% discount on selected designer Kurtas for women! Use {} and get designer Kurtis and sleeveless '
        'Kurtis online at {}. Shop for Kurtis online for women for all occasions- Partywear kurta sets to casual '
        'wear, daily wear and office wear; {} is a one-stop shop for all your ethnic wear needs.'.format(
            discount, coupon_code, brand, brand)])

    output_str += first_line
    output_str = output_str + '\n\nProduct Links: \n'

    for i in range(len(utm_product_links)):
        output_str = output_str + '{} {}: {}\n'.format(e2, title_list[i], short_links[i])
    output_str = output_str + '\nMy Measurements:\nHeight:\nBust Size:\nSize:\n\n'
    output_str += desc + "\n\n" + hashtags

    return output_str
