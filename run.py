import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')
@app.route('/detik-populer')
def detik():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    html = requests.get(url, params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(html.text, 'html.parser')
    berita_populer = soup.find_all(attrs={'class': 'grid-row list-content'})
    judul = soup.find_all(attrs={'class': 'media__title'})
    images = soup.find_all(attrs={'class': 'media__image'})
    return render_template('detik-scraper.html', images = images)

@app.route('/idr-rates')
def idr():
    url = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = url.json()
    return render_template('idr-rates.html', datas = json_data.values())


if __name__ == '__main__':
    app.run(debug=True)




