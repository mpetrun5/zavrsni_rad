import requests
from bs4 import BeautifulSoup


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

    data = data.replace('\n', '')
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

    data['title'] = _clean_data(data['title'])
    data['price'] = _clean_data(data['price'])
    data['description'] = _clean_data(data['description'])
    return data
