URL = 'https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE'
URL_1 = 'https://google.ru/?wmid=242&92c84d0f8c034531ace41792bd8bcc05'

def divider(url):
    try:
        return url.split('clickid=')[1].split('&')[0]
    except IndexError:
        return 'There is no clickid in current URL'

print(divider(URL_1))