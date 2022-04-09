import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
domains_list = [f'https://www.jobspider.com/job/resume-search-results.asp/words_Software%2BEngineer/searchtype_1/',]
# f'https://www.jobspider.com/job/resume-search-results.asp/words_Data+science/searchtype_1/',
# f'https://www.jobspider.com/job/resume-search-results.asp/',]

href_list = []
for domain in domains_list:
	for j in range(1,12):
		url = domain+f'page_{j}'
		driver = webdriver.Chrome(executable_path="/home/shavak/resume_scraped_data/chromedriver")
		driver.get(url)
		time.sleep(5)
		for i in range(2,52):
			href_local = driver.find_elements(By.XPATH,f'/html/body/form/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/center/table/tbody/tr/td/center/font/table/tbody/tr[{i}]/td[6]/a')[0]
			attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', href_local)
			href_list.append('https://www.jobspider.com'+attrs['href'])
			print('https://www.jobspider.com'+attrs['href'])

# with open('job_spider_resumes_page_link.txt','a') as f:
# 	for element in href_list:
# 		f.write(element + "\n")

df = pd.DataFrame(columns = ['url'])
df['url'] = href_list
df.to_csv('job_spider_resumes_page_link_software_engineer_resumes.csv')




