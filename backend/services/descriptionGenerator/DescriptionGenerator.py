import time
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse
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


def get_product_data(link):
    data_list = []
    r = requests.get(link)
    t = r.text
    soup = BeautifulSoup(t, 'html.parser')

    try:
        if 'fashor' in link:
            sku = soup.select('p.sku')[0].text.strip()
            title = soup.select('h1.product_name')[0].text.strip()
            price = soup.select('span.current_price')[0].text.strip().replace('₹', '').split('.')[0].replace(' ',
                                                                                                             '').replace(
                ',', '')
        elif any(ele in link for ele in ['houseofindya', 'faballey']):
            sku = soup.find('span', {'class': 'proSkuid'}).text.strip()
            title = soup.find('h1', {'itemprop': 'name'}).text.strip()
            price = soup.select('h4')[0].text.strip()
            if ' ' in price:
                price = price.split(" ")[2]
        elif 'rustorange' in link:
            sku = soup.find('span', {'class': 'ProductMeta__SkuNumber'}).text.strip()
            title = soup.find('h1', {'class': 'ProductMeta__Title'}).text.strip()
            price = soup.find('span', {'class': 'ProductMeta__Price'}).text.strip().replace('Rs.', '').replace(' ',
                                                                                                               '').replace(
                ',', '')
        elif 'juniperfashion' in link:
            sku = 'NA'
            title = soup.find('h1', {'class': 'm-0'}).text.strip()
            price = soup.find('span', {'class': 'money'}).text.strip().replace('Rs.', '').split('.')[0].replace(' ',
                                                                                                                '').replace(
                ',', '')
        elif 'usplworld' in link:
            sku = 'NA'
            title = soup.find('li', {'class': 'pl-0'}).text.strip()
            price = soup.find('h4', {'class': 'mb-0 text-uppercase'}).text.strip().split(' ')[0].replace('₹',
                                                                                                         '').replace(
                ',', '')
        elif 'irasoleil' in link:
            sku = 'NA'
            title = soup.find('h1', {'class': 'product-single__title'}).text.strip()
            price = soup.find('span', {'class': 'money'}).text.strip().split('.')[0].replace('₹', '').replace(',', '')
        elif 'aksclothings' in link:
            sku = soup.find('span', {'class': 'value'}).text.strip()
            title = soup.find('h1', {'class': 'product-name'}).text.strip()
            price = soup.find('span', {'class': 'price'}).text.strip().split('.')[0].replace('₹', '').replace(',', '')
        elif 'baniwomen' in link:
            sku = soup.find('span', {'class': 'value'}).text.strip()
            title = soup.find('h1', {'class': 'product-name'}).text.strip()
            price = soup.find('span', {'class': 'price'}).text.strip().split('.')[0].replace('₹', '').replace(',', '')
        elif 'janasya' in link:
            sku = 'NA'
            title = soup.find('h1', {'class': 'product__title'}).text.strip()
            price = soup.find('span', {'class': 'price-item'}).text.strip().replace('Rs.', '').split('.')[0].replace(
                ' ', '').replace(',', '')
        elif 'rajnandinifashion' in link:
            sku = soup.select('p')[10].text.strip()[5:]
            title = soup.find('h1', {'class': 'paira-product-title'}).text.strip()
            price = soup.find('span', {'class': 'paira-default-price'}).text.strip().replace('₹', '').split('.')[
                0].replace(' ', '').replace(',', '')
        else:
            sku = 'NA'
            title = 'NA'
            price = 'NA'
    except:
        parsed = urlparse(link)
        if not parsed.params:
            sku = 'homepage'
            title = 'homepage'
            price = '0'
        else:
            sku = 'NA'
            title = 'NA'
            price = 'NA'

    data_list.append(sku)
    data_list.append(title)
    data_list.append(price)

    return data_list


def get_description(row):
    print('Generating description for: {}'.format(row['influencer_name']))
    output_str = ''
    name = row['influencer_name']
    discount = row['coupon_code']
    month = row['campaign_month']
    brand = row['brand_name']
    coupon_code = get_coupon_code(name, discount)
    utm_campaign = get_utm_campaign(name, brand, month, discount)
    product_links = row['product_links'].replace(' ', '').split(',')
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
        short_links.append(get_short_link(utm_link))

    title_list, price_list, discounted_price_list, short_links = zip(
        *sorted(zip(title_list, price_list, discounted_price_list, short_links), reverse=True))
    homepage_link = get_short_link(get_utm_link(get_homepage_link(product_links), utm_campaign))

    e1 = random.choice(['🎊', '🔆', '🎉'])
    e2 = random.choice(['🔸', '🌈', '☀️', '👉', '🎈', '📌', '🛍️', '🎀', '🔹', '👗', '🌸'])
    e3 = random.choice(['➡️', '👉'])

    output_str = output_str + 'Description: \n\n'
    output_str = output_str + 'Use my coupon code "{}" and get a {} {}% DISCOUNT {} on {} \nWebsite Link: {} {}\n\n'.format(
        coupon_code, e1, discount, e1, brand, e3, homepage_link)
    output_str = output_str + 'Product Links: \n'

    for i in range(len(utm_product_links)):
        output_str = output_str + '{} {}: {}\n'.format(e2, title_list[i], short_links[i])

    output_str = output_str + '\n\nPrice Info:\n'
    for i in range(len(utm_product_links)):
        output_str = output_str + '{}: Original Price - Rs. {} ; After Coupon Code - Rs. {}\n'.format(title_list[i],
                                                                                                      price_list[i],
                                                                                                      discounted_price_list[
                                                                                       i])

    return output_str