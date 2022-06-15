import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse


def get_after_discount_price(original_price, discount):
    return int(original_price - ((discount / 100) * original_price))


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


def price_info(links, discount):
    title_list = []
    price_list = []
    discounted_price_list = []
    output_str = ''
    print(links)
    product_links = []
    for link in links:
        product_links.append(link.get('link'))
    for link in product_links:
        product_data = get_product_data(link)
        title_list.append(product_data[1])
        price_list.append(int(product_data[2].replace('.', '').replace(',', '').replace('Rs', '').replace("'", '')))
        discounted_price_list.append(get_after_discount_price(
            int(product_data[2].replace('.', '').replace(',', '').replace('Rs', '').replace("'", '')), discount))
    for i in range(len(price_list)):
        output_str += r'{}: Original Price - Rs. {} After Coupon Code - Rs. {} '.format(title_list[i], price_list[i],discounted_price_list[i])
        output_str +="\n"

    return output_str
