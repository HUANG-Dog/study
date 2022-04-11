import urllib.request
#导入网页url
url = 'https://detail.tmall.com/item.htm?id=654559896211&sku_properties=5919063:6536025;122216431:27772'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
print(html)