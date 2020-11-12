from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd 
import requests

def init_browser():
    executable_path = {'executable_path': "C:/Users/akspe/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    html = browser.html
    soup_news = BeautifulSoup(html, 'html.parser')

    news_title = news_one.find('div', class_='content_title').get_text()
    news_p = news_one.find('div', class_='rollover_description_inner').get_text()

    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)

    full_image_button = browser.find_by_id("full_image")
    full_image_button.click()
    more_info_button = browser.links.find_by_partial_text("more info")
    more_info_button.click()

    html = browser.html
    soup_div = BeautifulSoup(html, 'html.parser')

    image_path = soup_div.select_one("figure.lede a img").get("src")
    photo_link = "https://www.jpl.nasa.gov/" + image_path


    url_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_facts)

    facts_df = tables[0]

    html_table = facts_df.to_html()


    USGS_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(USGS_url)

    USGS_html = browser.html
    soup_USGS = BeautifulSoup(USGS_html, 'html.parser')
    hemispherese_url = (USGS_url.split('/search'))[0]

    hemispheres = soup_hemisphere.find_all('div', class_='description')

    for hemisphere in hemispheres:
        hemisphere_info = {}
        hemisphere_title = hemisphere.find('h3').text
    
        hemisphere_info['title'] = hemisphere_title.split('Enhanced')[0]
    
        hemisphere_route = hemisphere.find('a', class_='itemLink product-item')['href']
    
        hemisphere_link = base_url + hemisphere_route
        browser.visit(hemisphere_link)
        html = browser.html
        soup_hemisphere = BeautifulSoup(html, 'html.parser')
    
        image_url = soup_hemisphere.find('div', class_='downloads').find('ul').find('li').find('a')['href']
    
        hemisphere_info['img_url'] = image_url
    
        hemisphere_image_urls.append(hemisphere_info)

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "photo_link": photo,
        "html_table": table,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return mars_data      