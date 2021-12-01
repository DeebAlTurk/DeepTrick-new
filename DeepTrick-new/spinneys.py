import os
import pickle
from os import path

import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver

import Scraping_methods

chromedriver_autoinstaller.install()
browser = webdriver.Chrome()
gaint = "https://www.spinneyslebanon.com/promotionsDELMhttps://www.spinneyslebanon.com/seasonal.htmlDELMhttps://www.spinneyslebanon.com/alcohol.htmlDELMhttps://www.spinneyslebanon.com/beverages.htmlDELMhttps://www.spinneyslebanon.com/bakery.htmlDELMhttps://www.spinneyslebanon.com/deli-dairy-eggs.htmlDELMhttps://www.spinneyslebanon.com/fruits-vegetables.htmlDELMhttps://www.spinneyslebanon.com/meat-seafood.htmlDELMhttps://www.spinneyslebanon.com/food-cupboard.htmlDELMhttps://www.spinneyslebanon.com/snacks-candy.htmlDELMhttps://www.spinneyslebanon.com/cleaning-household.htmlDELMhttps://www.spinneyslebanon.com/beauty-personal-care.htmlDELMhttps://www.spinneyslebanon.com/baby-child.htmlDELMhttps://www.spinneyslebanon.com/petfectionDELMhttps://www.spinneyslebanon.com/world-foods.htmlDELMhttps://www.spinneyslebanon.com/home-outdoor.htmlDELMhttps://www.spinneyslebanon.com/electronics-appliances.htmlDELMhttps://www.spinneyslebanon.com/party-shop.htmlDELMhttps://www.spinneyslebanon.com/cigarettes.htmlDELMhttps://www.spinneyslebanon.com/gift-cards.html"
# gaint = "https://www.spinneyslebanon.com/bakery.html"
links = gaint.split('DELM')
next_links = []

if not path.exists('targets') or path.getsize('targets') == 0:
    for link in links:
        browser.get(link)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        next_links.append(link)
        while 1 == 1:
            if Scraping_methods.is_css_selector_available(soup,
                                                          'a.action.next') and not Scraping_methods.is_css_selector_available(
                soup, '.item.pages-item-next.disabled'):
                next_link = (soup.select_one('a.action.next').get('href'))
                browser.get(next_link)
                soup = BeautifulSoup(browser.page_source, 'lxml')
                next_links.append(next_link)
                file = open('targets', 'wb')
                pickle.dump(next_links, file)
                file.close()
            else:
                break
else:
    file = open('targets', 'rb')
    next_links = pickle.load(file)
    file.close()
    print(next_links)
names = []
for link in next_links:
    name = link.split('/')[-1].split('.')[0]
    names.append(name)

images_options = {'label': 'images', 'type': 'selector', 'name': '.product-image-photo', 'exists': True,
                  'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'attr', 'attr': 'src'}
names_options = {'label': 'names', 'type': 'selector', 'name': '.product-item-link', 'exists': True,
                 'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'text'}
prices_options = {'label': 'prices', 'type': 'selector', 'name': '.price', 'exists': True,
                  'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'text'}

links_options = {'label': 'links', 'type': 'selector', 'name': '.product-item-link', 'exists': True,
                 'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'attr', 'attr': 'href'}
results = {}
i = 0
page_count = 1
for link in next_links:
    browser.get(link)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    max_imgs = len(soup.select('.product-image-photo')) + 1
    max_names = len(soup.select('.product-item-link')) + 1
    max_prices = len(soup.select('.price')) + 1
    max_links = max_names
    images_options['end'] = max_imgs
    names_options['end'] = max_names
    links_options['end'] = max_links
    prices_options['end'] = max_prices

    options: list = []
    options.append(images_options)
    options.append(names_options)
    options.append(links_options)
    options.append(prices_options)
    print(f"link : {link}\nName : {names[i]}\npage_count : {page_count}")
    if not os.path.exists(f"{names[i]}_page_{page_count}.json"):
        Scraping_methods.convert_dict_to_json(Scraping_methods.scraper(soup, options, results), 4,
                                              f"{names[i]}_page_{page_count}")
    file = open("targets", 'wb')
    pickle.dump(next_links[i+1::], file)
    file.close()
    i += 1
    try:
        if names[i] in link:
            page_count += 1
        else:
            page_count = 1
    except:
        page_count = 1
    results = {}

os.remove('targets')
