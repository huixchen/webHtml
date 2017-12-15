import requests

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    r = requests.get(url)
    html = r.content
    html_doc = str(html, 'utf-8')

    return html_doc


def main():
    print(download_page(DOWNLOAD_URL))



if __name__ == '__main__':
    main()



