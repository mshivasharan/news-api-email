import requests
from send_email import send_email

api_key = '885767a5d7604471b7ee16eb62ea64da'
url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=885767a5d7604471b7ee16eb62ea64da'

request = requests.get(url)
content = request.json()

body = ''
for article in content['articles']:
    # try:
    body = body + article['title'] + '\n' + article['description'] + 2*'\n'


body = body.encode('utf-8')
send_email(message=body)
    # send_email(article['description'])

    # print(type(article['title']))
    # except TypeError:
    #     print('error')