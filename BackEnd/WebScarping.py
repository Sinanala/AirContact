import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://sinan:taha.0539@cluster0.owcbj1e.mongodb.net/?retryWrites=true&w=majority")
mydatabase=myclient["airContact"]
liste6=[]
def webScarping(URL):
    response=requests.get(URL)
    html_icerigi=response.content
    soup=BeautifulSoup(html_icerigi,"html.parser")
    table=soup.find_all("table",attrs={"data-type":"arrivals"})

    liste=[]
    class MyHTMLParser(HTMLParser):

        
        def handle_data(self, data):
            #print(data,end="")
            data=data.split(' ')
            liste.append(data)
        

    table=str(table)
    parser=MyHTMLParser()
    parser.feed(table)
    liste=liste[19:]

    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
    def remove_from_list(the_list):
        liste5=[]
        for value in the_list:
            if(len(value[0])!=3):
                liste5.append(value)
            if(value[0]=='Van'):
                liste5.append(value)
                
        return liste5



    liste2=remove_values_from_list(liste,['', ''])
    liste2=remove_values_from_list(liste2,[')'])
    liste2=remove_values_from_list(liste2,['+03'])
    liste2=remove_values_from_list(liste2,['('])
    liste2=remove_values_from_list(liste2,['EET'])
    liste2=remove_values_from_list(liste2,['CET'])
    liste2=remove_from_list(liste2)
    
    liste4=[]
    

    for i in range(0,len(liste2),5):
        liste3=[]
        if(len(liste2)-i<5):
            break
        liste3.append(liste2[i][0])
        liste3.append(liste2[i+1][0])
        liste3.append(liste2[i+2][0])
        liste3.append(liste2[i+3][0])
        liste3.append(liste2[i+4][0])
        liste4.append(liste3)   
    for i in liste4:
        fligts={
        "Kimlik":"",
        "Tip":"",
        "Nereden":"",
        "Kalkış":"",
        "Varış":""
    }
        fligts["Kimlik"]=i[0]
        fligts["Tip"]=i[1]
        fligts["Nereden"]=i[2]
        fligts["Kalkış"]=i[3]
        fligts["Varış"]=i[4]
        liste6.append(fligts)
        
for i in range(52):
        if i == 0:
         webScarping("https://flightaware.com/live/airport/LTAF")
         mycollections=mydatabase["Adana"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 1:
         webScarping("https://flightaware.com/live/airport/LTCP")
         mycollections=mydatabase["Adıyaman"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 2:
         webScarping("https://flightaware.com/live/airport/LTCO")
         mycollections=mydatabase["Agrı"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 3:
         webScarping("https://flightaware.com/live/airport/LTAP")
         mycollections=mydatabase["Amasya"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 4:
         webScarping("https://flightaware.com/live/airport/LTAC")
         mycollections=mydatabase["Ankara"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 5:
         webScarping("https://flightaware.com/live/airport/LTAI")
         mycollections=mydatabase["Antalya"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 6:
         webScarping("https://flightaware.com/live/airport/LTFG")
         mycollections=mydatabase["Gazipasa"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 7:
         webScarping("https://flightaware.com/live/airport/LTFO")
         mycollections=mydatabase["Rize-Artvin"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 8:
         webScarping("https://flightaware.com/live/airport/LTBD")
         mycollections=mydatabase["Aydın"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 9:
         webScarping("https://flightaware.com/live/airport/LTBF")
         mycollections=mydatabase["Balıkesir"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 10:
         webScarping("https://flightaware.com/live/airport/LTFD")
         mycollections=mydatabase["EdremitKorfez"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 11:
         webScarping("https://flightaware.com/live/airport/LTCU")
         mycollections=mydatabase["Bingol"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 12:
          webScarping("https://flightaware.com/live/airport/LTBH")
          mycollections=mydatabase["Canakkale"]
          x=mycollections.insert_many(liste6)
          liste6=[]
         
        if i== 13:
         webScarping("https://flightaware.com/live/airport/LTAY")
         mycollections=mydatabase["Denizli"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 14:
         webScarping("https://flightaware.com/live/airport/LTCC")
         mycollections=mydatabase["Diyarbakir"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 15:
         webScarping("https://flightaware.com/live/airport/LTBU")
         mycollections=mydatabase["Corlu"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 16:
          webScarping("https://flightaware.com/live/airport/LTCA")
          mycollections=mydatabase["Elazıg"]
          x=mycollections.insert_many(liste6)
          liste6=[]
         
        if i== 17:
         webScarping("https://flightaware.com/live/airport/LTCD")
         mycollections=mydatabase["Erzincan"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 18:
         webScarping("https://flightaware.com/live/airport/LTCE")
         mycollections=mydatabase["Erzurum"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 19:
         webScarping("https://flightaware.com/live/airport/LTAJ")
         mycollections=mydatabase["Gaziantep"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 20:
         webScarping("https://flightaware.com/live/airport/LTCB")
         mycollections=mydatabase["Ordu-Giresun"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 21:
         webScarping("https://flightaware.com/live/airport/LTCW")
         mycollections=mydatabase["Hakkari"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 22:
         webScarping("https://flightaware.com/live/airport/LTDA")
         mycollections=mydatabase["Hatay"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 23:
         webScarping("https://flightaware.com/live/airport/LTFC")
         mycollections=mydatabase["Isparta"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 24:
         webScarping("https://flightaware.com/live/airport/LTFJ")
         mycollections=mydatabase["Isabiha"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 25:
         webScarping("https://flightaware.com/live/airport/LTFM")
         mycollections=mydatabase["Istanbul"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 26:
         webScarping("https://flightaware.com/live/airport/LTBJ")
         mycollections=mydatabase["Izmır"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 27:
         webScarping("https://flightaware.com/live/airport/LTCF")
         mycollections=mydatabase["Kars"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 28:
         webScarping("https://flightaware.com/live/airport/LTAL")
         mycollections=mydatabase["Kastamonu"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 29:
         webScarping("https://flightaware.com/live/airport/LTAU")
         mycollections=mydatabase["Kayseri"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 30:
         webScarping("https://flightaware.com/live/airport/LTAN")
         mycollections=mydatabase["Konya"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 31:
         webScarping("https://flightaware.com/live/airport/LTBZ")
         mycollections=mydatabase["Kutahya"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 32:
         webScarping("https://flightaware.com/live/airport/LTAT")
         mycollections=mydatabase["Malatya"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 33:
         webScarping("https://flightaware.com/live/airport/LTCN")
         mycollections=mydatabase["Kahramanmaras"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 34:
         webScarping("https://flightaware.com/live/airport/LTCR")
         mycollections=mydatabase["Mardin"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 35:
         webScarping("https://flightaware.com/live/airport/LTCK")
         mycollections=mydatabase["Mus"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 36:
         webScarping("https://flightaware.com/live/airport/LTAZ")
         mycollections=mydatabase["Nevsehir"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 37:
         webScarping("https://flightaware.com/live/airport/LTFH")
         mycollections=mydatabase["Samsun"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 38:
         webScarping("https://flightaware.com/live/airport/LTCL")
         mycollections=mydatabase["Siirt"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 39:
         webScarping("https://flightaware.com/live/airport/LTCM")
         mycollections=mydatabase["Sinop"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 40:
         webScarping("https://flightaware.com/live/airport/LTAR")
         mycollections=mydatabase["Sivas"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 41:
         webScarping("https://flightaware.com/live/airport/LTAW")
         mycollections=mydatabase["Tokat"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 42:
         webScarping("https://flightaware.com/live/airport/LTCG")
         mycollections=mydatabase["Trabzon"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 43:
         webScarping("https://flightaware.com/live/airport/LTCS")
         mycollections=mydatabase["Sanlıurfa"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 44:
         webScarping("https://flightaware.com/live/airport/LTBO")
         mycollections=mydatabase["Usak"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 45:
         webScarping("https://flightaware.com/live/airport/LTBO")
         mycollections=mydatabase["Van"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i== 46:
         webScarping("https://flightaware.com/live/airport/LTAS")
         mycollections=mydatabase["Zonguldak"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 47:
         webScarping("https://flightaware.com/live/airport/LTCJ")
         mycollections=mydatabase["Batman"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
        if i == 48:
         webScarping("https://flightaware.com/live/airport/LTCV")
         mycollections=mydatabase["Sırnak"]
         x=mycollections.insert_many(liste6)
         liste6=[]       

        if i == 49:
         webScarping("https://flightaware.com/live/airport/LTCT")
         mycollections=mydatabase["Igdır"]
         x=mycollections.insert_many(liste6)
         liste6=[]
         
       
         
        
    
    
    
        


    
