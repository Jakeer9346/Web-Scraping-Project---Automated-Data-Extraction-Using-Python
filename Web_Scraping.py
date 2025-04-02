import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=apple&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=apple%7CMobiles&requestId=f8e5f8f1-fb1a-4097-841d-68ad55a3dff0")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:12]:
    d=i.get_text
    name.append(d)
print(name)


prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:12]:
    d=i.get_text
    price.append(d)
print(price)


ratings=soup.find_all('div' ,class_="XQDdHH")
rate=[]
for i in ratings[0:12]:
    d=i.get_text()
    rate.append(float(d))
print(rate)


images=soup.find_all('img' ,class_="DByuf4")
image=[]
for i in images[0:12]:
    d=i['src']
    image.append(d)
print(image)
#print(df)
data={"Names":name,
      "Prices":price,
      "Rateings":rate,
      "images":image
     }
#print(data)
df = pandas.DataFrame(data)
#print(df)
df.to_csv("mobiles_data.csv")


