import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from .models import Product
import urllib3

requests.packages.urllib3.disable_warnings()


def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = 'https://www.newegg.com/p/pl?d=video+card&N=100006662'
    content = session.get(url, verify=True).content
    # html parser
    page_soup = soup(content, "html.parser")
    # grabe each product
    products = page_soup.findAll("div", {"class": "item-container"})
    for item in products:
        try:
            title = item.findAll("a", {"class": "item-title"})
            product_name = title[0].text
            produc_url = title[0]["href"]

            image_sorce = item.findAll("a", {"class": "item-img"})
            image_product = image_sorce[0].img["src"]
            try:
                price_products = item.findAll("li", {"class": "price-current"})
                price_product = price_products[0].strong.text
            except IndexError:
                break
        except IndexError:
            break

        try:
            new_product = Product()
            new_product.urls = produc_url
            new_product.product_description = product_name
            new_product.image = image_product
            new_product.price = price_product
            new_product.save()
        except:
            print('exists alrealdy')

    return redirect("../")


def display(request):
    result = Product.objects.all()[::-1]
    item = set(result)
    context = {
        'object_list': item,
    }
    return render(request, "index.html", context)
