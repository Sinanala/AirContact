import requests
from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser

"""limanlar = ['LTAF','LTAG','LTCP','LTCO','LTAP','LTAC','LTAE','LTAD','LTAB','LTAI','LTFG',
	           'LTFO','LTBD','LTBF','LTFD','LTCU','LTBH','LTAY','LTCC','LTBU','LTCA','LTCD',
	           'LTCE','LTBI','LTBY','LTAJ','LTCB','LTCW','LTDA','LTFC','LTFJ','LTFM','LTBJ',
	           'LTCF','LTAL','LTAU','LTAN','LTBZ','LTAT','LTCN','LTCR','LTCK','LTAZ','LTCB',
               'LTFO','LTFH','LTCL','LTCM','LTAR','LTBU','LTAW','LTCG','LTCS','LTBO','LTCI',
	           'LTAS','LTCJ','LTCV','LTCT']
for i in range(len(limanlar)):
    URL="https://flightaware.com/live/airport/"+limanlar[i]"""


URL="https://flightaware.com/live/airport/LTAC"
response=requests.get(URL)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")

table=soup.find_all("table",attrs={"data-type":"arrivals"})

class MyHTMLParser(HTMLParser):
  
        
    def handle_data(self,data):
        print("veriler :",data)
            
table=str(table)           
parser=MyHTMLParser()

parser.feed(table)

#print(table)
