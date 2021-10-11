import requests

try:

    url = input('Enter a valid url: ')

    r = requests.get(url)

    print('STATUS CODE:')
    print(r.status_code)
    print('HEADERS:')
    print(r.headers)
    print('HISTORY:')
    print(r.history)
    print('\n')
    print('ENCODING:')
    print(r.encoding)
    print('REASON:')
    print(r.reason)
    print('COOKIES:')
    print(r.cookies)
    print('ELAPSED:')
    print(r.elapsed)
    print('REQUEST:')
    print(r.request)

   

except requests.ConnectionError:
    print("failed to connect")


# https://www.google.com/
