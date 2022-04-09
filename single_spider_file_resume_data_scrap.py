from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
from tqdm import tqdm
import os
import re
def convert_html_form_to_text_format(url):
	file_name = 'spider_resumes_software/' + url[30:-5] + '.txt'
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'lxml')
	resume_type = soup.find_all(["h1"])[0].text.strip()
	with open(file_name,'w') as f:
		# f.write(resume_type+'\n')
		counter=0
		for tags in soup.find_all(["td"]):
			temp = tags.text.strip()
			if counter==20:
				f.write(temp.strip() + '\n')
			counter+=1
	with open(file_name,'r+') as sourceFile:
		sourceFileContents = sourceFile.read()
		modified_text = re.sub(r'\n\s*\n', '\n\n', sourceFileContents)
		sourceFile.write(modified_text)


df = pd.read_csv('job_spider_resumes_page_link_software_engineer_resumes.csv')
for i in tqdm(df['url']):
	convert_html_form_to_text_format(i)

# convert_html_form_to_text_format('https://www.jobspider.com/job/view-resume-83353.html')
