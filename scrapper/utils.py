import requests
from bs4 import BeautifulSoup

import urllib.request


def get_picture(image_name, url):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Chrome')
    filename, headers = opener.retrieve(url, image_name)
    return filename


def get_num_of_nights(url, destination_selector, num_of_nights_selector):
    """
    Get number of night number from destinations card.
    """
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    num_of_nights = {}
    for destination in soup.select(destination_selector):
        url = destination.get('href')
        night = destination.select(num_of_nights_selector)[0]
        num_of_nights[url] = night.get_text().split(' ')[0]

    return num_of_nights


def get_destination_picture(url, destination_selector):
    """
    Get picture of destination.
    """
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    pictures = {}
    for destination in soup.select(destination_selector):
        url = destination.get('href')
        image = destination.select('img')[0]
        pictures[url] = image.get('src')

    return pictures


def get_agency_destination_urls(url, destination_selector):
    """
    Get all destinations from given url.

    Args:
        url(string)
        destination_selector(string): css selector of destination div

    Returns
        list: list of destination urls
    """
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')

    destination_urls = []
    for destination in soup.select(destination_selector):
        url = destination.get('href')
        destination_urls.append(url)

    return destination_urls


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
        dict: destination data
    """
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')
    data = {}

    data['title'] = _get_first_value(soup, selector.title)
    data['price'] = _get_first_value(soup, selector.price)
    data['description'] = _get_first_value(soup, selector.travel_plan)

    for key, value in data.items():
        data[key] = _clean_data(value)

    return data
