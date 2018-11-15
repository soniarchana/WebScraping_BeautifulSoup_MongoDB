
# coding: utf-8

# Import dependencies

import os
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time



# p = get_ipython().getoutput('which chromedriver')
# print(p)

# Commnenting not required prints from below function code

def scrape():

    # Pointing to the directory where chromedriver exists
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    ### NASA Mars News
    # There is delay in run time wait upto few seconds
    # URL of page to be scraped
    url1 = "https://mars.nasa.gov/news/"
    browser.visit(url1)
    # Create a Beautiful Soup object
    html1= browser.html
    soup1 = bs(html1, 'html.parser')
    # type(soup1)

    news_title = soup1.find("div",class_="content_title").text
    news_paragraph = soup1.find("div", class_="article_teaser_body").text
    print(f"* TITLE: {news_title}\n")
    print(f"* PARAGRAPH: {news_paragraph}\n")



    ### JPL Mars Space Images - Featured Image
    # There is delay in run time wait upto few seconds
    # URL of page to be scraped
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    # Finding id full_image 
    browser.find_by_id("full_image").click()
    time.sleep(5)  
    # Create a Beautiful Soup object
    html2= browser.html
    soup2 = bs(html2, 'html.parser')
    #type(soup2)

    # Setting featured_image_url
    img_url = soup2.find('img', class_='fancybox-image')['src']
    # print(img_url)
    featured_image_url = "https://www.jpl.nasa.gov" + img_url
    print(f"* FEATURED IMAGE URL: {featured_image_url}\n")



    ### Mars Weather
    # There is delay in run time wait upto few seconds
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html3= browser.html
    soup3 = bs(html3, 'html.parser')
    #type(soup3)

    # Store the latest match for class_='TweetTextSize  TweetTextSize--normal js-tweet-text tweet-text
    mars_weather = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text                    
    print(f"* MARS WEATHER: {mars_weather}\n")



    ### Mars Facts
    # There is delay in run time wait upto few seconds
    url4 = "http://space-facts.com/mars/"
    browser.visit(url4)
    html4= browser.html
    soup4 = bs(html4, 'html.parser')
    #type(soup4)

    mars_facts = pd.read_html(url4)
    # mars_facts

    df_mars_facts = mars_facts[0]
    df_mars_facts.columns = ['Mars_Profile', 'Mars_ProfileValue']
    df_mars_facts.set_index('Mars_Profile', inplace=True)
    # df_mars_facts

    # mars_facts_html =df_mars_facts.to_html("mars_facts.html",justify='left')
    mars_facts_html =df_mars_facts.to_html(justify='left')
    print(f"* MARS FACTS HTML: {mars_facts_html}\n")    
    # !open mars_facts.html



    ### Mars Hemispheres
    # There is delay in run time wait upto few seconds
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    html5= browser.html
    soup5 = bs(html5, 'html.parser')
    #type(soup5)

    # Creating empty dictionary for storing images url and title
    mars_hemisphere_dict = []
    for i in range (4):   # we have 4 images
        time.sleep(5)
        imgs = browser.find_by_tag('h3')   # looking for all h3 tags where we have to click
        imgs[i].click()
        html5 = browser.html
        soup5 = bs(html5, 'html.parser')
        url_part = soup5.find("img", class_="wide-image")["src"]
        title = soup5.find("h2",class_="title").text
        iurl = 'https://astrogeology.usgs.gov'+ url_part
        mars_dict={"title": title,"img_url":iurl}
        mars_hemisphere_dict.append(mars_dict)
        browser.back()

    print(f"* MARS HEMISPHERE: {mars_hemisphere_dict}\n")

    # Consolidating all scraped data into one dictionary.
     # mars_mission_data = {
    #     'LATEST_MARS_NEWS_TITLE': news_title,
    #     'LATEST_MARS_NEWS_TEXT' : news_paragraph,
    #     'MARS_FEATURED_IMAGE'   : featured_image_url,
    #     'MARS_WEATHER'          : mars_weather,
    #     'MARS_FACTS'            : mars_facts_html,
    #     'MARS_HEMISPHERE'       : mars_hemisphere_dict
    # }
    mars_mission_data = {
        'news_title'            : news_title,
        'news_paragraph'        : news_paragraph,
        'featured_image_url'    : featured_image_url,
        'mars_weather'          : mars_weather,
        'mars_facts_html'       : mars_facts_html,
        'mars_hemisphere_dict'  : mars_hemisphere_dict
    }
    print(f"** MARS MISSION DATA : {mars_mission_data}\n")
    return mars_mission_data

    # Convert the Jupyter Notebook to Python 
    #get_ipython().system('ipython nbconvert --to=python mission_to_mars.ipynb')


# Calling the scrape function 
# data_from_mars= scrape()
# print("************************************************* PRINTING CONSOLIDATED DATA FROM SCRAPE FUNTION CALL  *********************************************** \n")
# print(data_from_mars)
# print("\n*********************************************** END OF FUNCTION CALL\n")


