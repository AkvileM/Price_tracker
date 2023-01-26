import pandas as pd
import numpy as np
import re
from random import randrange
from typing import List, Dict, Optional
from pydantic import BaseModel
from scrapers.base import extract_base_info
from scrapers.cars_scrape import extract_car_details

results_url = []
results_base = []
results_p = []
all_results = []
for page in range(1,40):
    url_list = f"https://en.autoplius.lt/ads/used-cars?page_nr={page}"
    all_results = extract_base_info(url_list)
    results_url.extend(all_results[0])
    results_base.extend(all_results[1])
    results_p.extend(all_results[2])

df1 = pd.DataFrame(results_url)
df1.columns = ['Url']
df2 = pd.DataFrame.from_dict(results_base)
df3 = pd.DataFrame(results_p)
df3.columns = ['Price']
results = (df1.join(df2)).join(df3)
results.to_csv("test1.csv")

links = results['Url']

cars_details = []
for link in links:
    cars_details.append(extract_car_details(link))

add_pd = pd.DataFrame.from_dict(cars_details)

all_results = results.join(add_pd)
all_results.to_csv('cars.csv')