URL = 'https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE'

def divider(url):
    try:
        return url.split('clickid=')[1].split('&')[0]
    except IndexError:
        return 'There is no clickid in current URL'

if __name__ == '__main__':
    print(divider(URL))