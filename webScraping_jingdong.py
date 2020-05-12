import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# website_link is the website URL in string format


def web_linker(address):
    my_url = address
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    return page_html


def converterSoup(webHTML):
    page_soup = soup(webHTML, "html.parser")
    return page_soup


if __name__ == '__main__':
    address = "http://bjwsz.jichu.chaoxing.com/"
    webHTML = web_linker(address=address)
    jdSoup = converterSoup(webHTML=webHTML)
    print(jdSoup)
    # spacer = jdSoup.findAll("div", class_='spacer')
    # print(spacer)
    # print(jdSoup)
