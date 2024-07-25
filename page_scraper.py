from bs4 import BeautifulSoup
import requests
import os
import json
import re

class Scraper:
    def __init__(self, category, url) -> None:
        '''
        creates a Scraper object that scrapes the webpage from provided url
        '''
        self.category = category
        self.output_file = f'{os.getcwd()}/json_files/{url.split("/")[-1]}.json'
        self.business = re.sub(r'[^a-zA-Z0-9\s]', " ", url.split("/")[-1])
        self.response = requests.get(url)
        self.status = self.response.status_code
        self.text = ""

    def getPageInfo(self):
        '''
        extract page information in paragraphs
        '''
        soup = BeautifulSoup(self.response.content, 'html.parser')
        res = soup.find_all('div', {'class':'business-entry'})
        for r in res:
            paragraph = r.find_all('p')
            info = "\n".join([p.getText().strip() for p in paragraph])
            self.text += info
        # return self.text
    
    def savePageInfo(self):
        scraped_info = {
            'category': self.category,
            'business': self.business,
            'information': self.text
        }
        json_object = json.dumps(scraped_info)
        with open(self.output_file, 'w+') as out:
            json.dump(scraped_info, out)
        return "Saved"



