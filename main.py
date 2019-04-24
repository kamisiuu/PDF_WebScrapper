# 
# AUTHOR: KAMIL LIPSKI
#
# This programs downloads all the pdf files from an website

import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
urlpage = requests.get('https://wiki.hiof.no/index.php/ModelingCPS').text
soup = BeautifulSoup(urlpage, 'html.parser')
for link in soup.select("a[href$='.pdf']"):
    filename = os.path.join('filer/', link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(urlpage, link['href'])).content)
        print(link)
        time.sleep(4)
exit(0)





