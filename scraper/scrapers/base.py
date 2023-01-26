from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np
import re
from random import randrange
from tqdm import tqdm #progress bar
from typing import List, Dict, Optional


def extract_base_info(url_list:str) -> Optional[List[Dict]]:

    results_url = []
    results_base = []
    results_p = []

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    resp = driver.get(url_list)
    s = random.randint(2, 11)
    time.sleep(s)
    base_source = driver.page_source
    base_soup = BeautifulSoup(base_source, 'html.parser')
    cars_should_be = int((base_soup.find("span", {"class":"result-count"}).text.strip())[1:-1])
    count_cars = []
    url_list_class = base_soup.find_all("div", class_="auto-lists en")
    for j in url_list_class:
        
        link = j.find_all('a', href=True)
        for i in link:
            url=[i['href']]
            results_url.append(url)
        
        description = j.find_all("div", class_="announcement-title")
        for i in description:
            Description = i.text.strip()
            Make_model = Description.split(',')[0]
            Brand = Make_model.split(" ",1)[0]
            Model = Make_model.split(" ",1)[1]


            results_base.append({'Brand':Brand, 'Model':Model})
        price_list = j.find_all("div", class_="announcement-pricing-info")
        for k in price_list:
            pricee = k.text.strip()
            price = pricee.split('€')[0]
            results_p.append(price)
    return results_url, results_base, results_p