from flask import request, jsonify
from config import app, cache
from bs4 import BeautifulSoup
import requests


@app.route('/search')
@cache.cached(timeout=30, query_string=True)
def search_gifs():
    query = request.args.get('q')
    url = 'https://www.skvot.com/search?text={}'.format(query)
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        response = 'No response'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html')
        items_data = []
        items_elements = soup.find_all('a', class_='top-item top-item--min')

        for item in items_elements:
            title = item.find('div', class_='top-item__title').text
            category = item.get('data-category-g')
            brand = item.get('data-brand')
            price = item.find('div', class_='top-item__price').get('data-price')
            url = 'https://www.skvot.com' + item.get('href')
            id = item.get('data-id')
            items_data.append({
                'Title': title,
                'Category': category,
                'Brand': brand,
                'Price': price,
                'Url': url,
                'id': id
            })
        return jsonify(items_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
