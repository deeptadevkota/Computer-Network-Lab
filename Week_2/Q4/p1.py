import requests

try:

    url = input('Enter a valid url: ')

    r = requests.get(url)
    print('\n')

    print('STATUS CODE:')
    print(r.status_code)
    print('\n')

    print('HEADERS:')
    print(r.headers)
    print('\n')

    print('HISTORY:')
    print(r.history)
    print('\n')

    print('ENCODING:')
    print(r.encoding)
    print('\n')

    print('REASON:')
    print(r.reason)
    print('\n')

    print('COOKIES:')
    print(r.cookies)
    print('\n')

    print('ELAPSED:')
    print(r.elapsed)
    print('\n')

    print('REQUEST:')
    print(r.request)
    print('\n')
   

except requests.ConnectionError:
    print("failed to connect")