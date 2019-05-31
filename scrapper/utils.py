import re

import requests
from bs4 import BeautifulSoup

import urllib.request


def get_picture(image_name, url):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Chrome')
    filename, headers = opener.retrieve(url, image_name)
    return filename


def get_destination_picture(scrapper):
    """
    Get picture of destination.
    """
    response_html = requests.get(scrapper.offers_url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    pictures = {}
    for destination in soup.select(scrapper.destination):
        try:
            url = destination.select(scrapper.destination_url)[0].get('href')
        except IndexError:
            url = destination.get('href')
        image = destination.select('img')[0]
        pictures[url] = image.get('src')

    return pictures


def get_num_of_nights(scrapper):
    """
    Get number of night number from destinations card.
    """
    response_html = requests.get(scrapper.offers_url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    num_of_nights = {}
    for destination in soup.select(scrapper.destination):
        try:
            url = destination.select(scrapper.destination_url)[0].get('href')
        except IndexError:
            url = destination.get('href')
        try:
            night = destination.select(scrapper.num_of_nights)[0]
            number = re.findall('\d+', night.get_text())[0]
        except IndexError:
            number = 0
        num_of_nights[url] = number

    return num_of_nights


def get_price(scrapper):
    response_html = requests.get(scrapper.offers_url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    prices = {}
    for destination in soup.select(scrapper.destination):
        try:
            url = destination.select(scrapper.destination_url)[0].get('href')
        except IndexError:
            # Fix for when destination is already a element
            url = destination.get('href')
        price = destination.select(scrapper.price)
        prices[url] = _get_price(price[0].get_text())

    return prices


def get_title(scrapper):
    response_html = requests.get(scrapper.offers_url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    titles = {}
    for destination in soup.select(scrapper.destination):
        try:
            url = destination.select(scrapper.destination_url)[0].get('href')
        except IndexError:
            # Fix for when destination is already a element
            url = destination.get('href')
        title = destination.select(scrapper.title)
        titles[url] = _clean_data(title[0].get_text())

    return titles


def get_agency_destination_urls(scrapper):
    """
    Get all destinations from given url.

    Args:
        url(string)
        destination_selector(string): css selector of destination div

    Returns
        list: list of destination urls
    """
    response_html = requests.get(scrapper.offers_url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    destination_urls = []
    for destination in soup.select(scrapper.destination):
        try:
            url = destination.select(scrapper.destination_url)[0].get('href')
        except IndexError:
            url = destination.get('href')
        destination_urls.append(url)

    return destination_urls


def _get_price(string):
    if string is not None:
        try:
            return re.findall('\d+.?,?\d+', string)[0].replace('.', ' ').replace(',', '').replace(' ', '')
        except IndexError:
            return 0.00
    else:
        return 0.00


def _get_first_value(soup, selector):
    try:
        value = soup.select(selector)[0].get_text()
    except IndexError:
        try:
            value = soup.select(selector).get_text()
        except AttributeError:
            value = None
    return value


def _clean_data(data):
    if data is None:
        return

    #data = data.replace('\n', '')
    return ' '.join(data.split())


def get_destination_data(url, selector):
    """
    Get data about destination.

    Args:
        url(string)
        selector(obj)

    Returns:
        destination data
    """
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')
    data = _clean_data(_get_first_value(soup, selector.travel_plan))
    if data is None:
        data = 'Forbidden access!'
    return data
