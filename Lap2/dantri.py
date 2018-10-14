#1. Download web
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel


url = "https://dantri.com.vn/"
#1.1 Open connection
conn = urlopen(url)
#1.2 Download raw data
raw_data = conn.read()
#1.3 Decode data
webpage_text = raw_data.decode("utf-8")
#1.4 Save text
#Cach luu data
#          w => write
#           b => binary
# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close()
# print(len(webpage_text))
# print(webpage_text)


#2.Extract ROI
#2.1 Convert text to soup
soup= BeautifulSoup(webpage_text,"html.parser") #parser nhan biet trang nay dang html
ul = soup.find("ul","ul1 ulnew")
li_list = ul.find_all("li")
li = li_list[0]

new_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]
    # print(title)
    # print(link)
    news = {
        "Title" : title,
        "Link" : link,
    }
    new_list.append(news)
print(*new_list,sep="\n")
# print(ul.prettify())
# print(soup.prettify())




#3.Extract Data



#4.Save Data
pyexcel.save_as(records=new_list, dest_file_name="dantri.xlsx")