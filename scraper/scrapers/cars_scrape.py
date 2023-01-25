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

def extract_car_details(link:str) -> Optional[List[Dict]]:

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    t = random.randint(3, 6)
    driver.get(link)
    time.sleep(t)
    base_source1 = driver.page_source
    base_soup1 = BeautifulSoup(base_source1, 'html.parser')
    u = random.randint(2, 4)
    time.sleep(u)
    car_info = base_soup1.find_all("div", class_="parameter-row")
    labels = []
    values = []

    for group in base_soup1.find_all("div", class_='parameter-row'):
        labels.append([label.text.strip() for label in group.find_all("div", class_='parameter-label')])
        values.append([value.text.strip() for value in group.find_all("div", class_='parameter-value')])

    labels = [''.join(ele) for ele in labels][1:]
    values = [''.join(ele) for ele in values][1:]
    car_detail = {labels[k]: values[k] for k in range(len(labels))}

    return car_detail