#Sample Test program to track prices on Amazon for a given product and send email for price drop


#import urllib.request

#importing requests library module
import requests

#Importing BeautifulSoup library
#BeautifulSoup is used for parsing and extracting data from HTML webpages
from bs4 import BeautifulSoup

#input the URL of the product to scrape web pages
URL = 'https://www.amazon.com/dp/B07FPP6TB5/ref=gwd_dc_tve_cm?pf_rd_p=7d3126cc-ba3f-41cc-8f4a-dc96bd30fa11&pf_rd_r=K7Y5FJBRWB4QY21EM7FK'

#Configure a "User-Agent", which is a unique identifier for every device accessing a webpage
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

#Get requests of the webpage
page = requests.get(URL, headers)

#Parse the contents of the webpage, input is "contents of the page"
soup = BeautifulSoup(page.content, 'html.parser')

# print("Printing status code response of the webpage",page.status_code)
# print("START OF HTML PARSE WITHOUT PRETTIFY")
# p = print("Printing contents of the page without Prettify", soup)
# print("END OF HTML PARSE WITHOUT PRETTIFY")
# print("START OF HTML PARSE WITH PRETTIFY")
# #Display contents of the page as list using "prettify" method in "BeautifulSoup"
# #prettify method from BeautifulSoup will convert a BS- BeautifulSoup?? Parse tree to a unicode string
# q = print("Printing contents of the page using Prettify", soup.prettify)
# print("END OF HTML PARSE WITH PRETTIFY")

# #Testing to check both contents WITH and WITHOUT PRETTIFY are same, (contents are same)
# if p==q:
#     print("Both texts are same, there's no difference with PRETTIFY")

#Find the first tag with the id="productTitle" with the "find" method, use "find_all" to find list of all tags
print("Product Title is ", soup.find(id="productTitle"))

#Find the first tag with the id="price_inside_buybox" with the "find" method
print("Product Price inside Buybox is ", soup.find(id="price_inside_buybox"))


#print(soup.find_all(id="productTitle"))

