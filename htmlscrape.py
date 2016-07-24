import requests
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'From': 'youremail@domain.com'  # This is another valid field
}


#storing response
response = requests.get('https://pokevision.com', headers=headers)
#creating lxml tree from response body

#print(response.text.encode("utf-8"))
tree = html.fromstring(response.text.encode("utf-8"))

#Finding all anchor tags in response
print(tree.xpath('script').tag)