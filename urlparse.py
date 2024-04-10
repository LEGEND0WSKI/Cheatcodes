links = [
    'www.google.com',
    'www.youtube.com',
    'www.wikipedia.com',
    'www.facebook.com',
    'www.twitter.co.in',
    
]

for link in links:
    print(link.removeprefix('www.').split('.')[0])
