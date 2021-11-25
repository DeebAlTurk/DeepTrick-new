from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import Scraping_methods

# {'label': 'title', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 0, 'offset': 0, 'get_what': 'tag'}
# {'label': 'title', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 0, 'offset': 0, 'get_what': 'text'}
# {'label': 'x', 'type': 'tag', 'name': 'title', 'exists': True, 'isRange': 1, 'start': 0, 'end': 4, 'get_what': 'attr', 'attr': 'class'}
s=Service('chromedriver.exe')
browser = webdriver.Chrome(service=s)
# link = "https://www.spinneyslebanon.com/bakery.html"
# browser.get(link)
# soup = BeautifulSoup(browser.page_source, 'lxml')
# next = "{'label': 'next', 'type': 'selector', 'name': 'a.action.next', 'exists': True, 'isRange': 0, 'offset': 0, 'get_what': 'attr', 'attr': 'href'}"
gaint = "https://www.spinneyslebanon.com/promotionsDELMhttps://www.spinneyslebanon.com/seasonal.htmlDELMhttps://www.spinneyslebanon.com/alcohol.htmlDELMhttps://www.spinneyslebanon.com/beverages.htmlDELMhttps://www.spinneyslebanon.com/bakery.htmlDELMhttps://www.spinneyslebanon.com/deli-dairy-eggs.htmlDELMhttps://www.spinneyslebanon.com/fruits-vegetables.htmlDELMhttps://www.spinneyslebanon.com/meat-seafood.htmlDELMhttps://www.spinneyslebanon.com/food-cupboard.htmlDELMhttps://www.spinneyslebanon.com/snacks-candy.htmlDELMhttps://www.spinneyslebanon.com/cleaning-household.htmlDELMhttps://www.spinneyslebanon.com/beauty-personal-care.htmlDELMhttps://www.spinneyslebanon.com/baby-child.htmlDELMhttps://www.spinneyslebanon.com/petfectionDELMhttps://www.spinneyslebanon.com/world-foods.htmlDELMhttps://www.spinneyslebanon.com/home-outdoor.htmlDELMhttps://www.spinneyslebanon.com/electronics-appliances.htmlDELMhttps://www.spinneyslebanon.com/party-shop.htmlDELMhttps://www.spinneyslebanon.com/cigarettes.htmlDELMhttps://www.spinneyslebanon.com/gift-cards.html"
gaint_names="protmotionsDELMseasonalDELMalcoholDELMbeveragesDELMbakeryDELMdeli-dairy-eggsDELMfruits-vegetablesDELMmeat-seafoodDELMfood-cupboardDELMsnacks-candyDELMcleaning-householdDELMbeauty-personal-careDELMbaby-childDELMpetfectionDELMworld-foodsDELMhome-outdoorDELMelectronics-appliancesDELMparty-shopDELMtobaccoDELMgift-cards"
links = gaint.split('DELM')
names=gaint_names.split('DELM')
next_links = []
for link in links:
    browser.get(link)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    while 1 == 1:
        if Scraping_methods.is_css_selector_available(soup,
                                                      'a.action.next') and not Scraping_methods.is_css_selector_available(
            soup, '.item.pages-item-next.disabled'):
            next_link = (soup.select_one('a.action.next').get('href'))
            browser.get(next_link)
            soup = BeautifulSoup(browser.page_source, 'lxml')
            next_links.append(next_link)
        else:
            break
# print(next_links)
images_options = {'label': 'images', 'type': 'selector', 'name': '.product-image-photo', 'exists': True,
                  'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'attr', 'attr': 'src'}
names_options = {'label': 'names', 'type': 'selector', 'name': '.product-item-link', 'exists': True,
                 'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'text'}

links_options = {'label': 'links', 'type': 'selector', 'name': '.product-item-link', 'exists': True,
                 'isRange': 1, 'start': 0, 'end': 54, 'get_what': 'attr', 'attr': 'href'}
results = {}
i=0
for link in next_links:
    browser.get(link)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    max_imgs = len(soup.select('.product-image-photo')) + 1
    max_names = len(soup.select('.product-item-link')) + 1
    max_links = max_names
    images_options['end'] = max_imgs
    names_options['end'] = max_names
    links_options['end'] = max_links

    images_options['label']=names[i]+"_images"
    names_options['label']=names[i]+"_names"
    links_options['label']=names[i]+"_links"
    options: list = []
    options.append(images_options)
    options.append(names_options)
    options.append(links_options)
    results = Scraping_methods.scraper(soup, options, results)

Scraping_methods.convert_dict_to_json(results, 4, "Spinneys")