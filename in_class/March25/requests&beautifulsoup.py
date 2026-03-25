# To understand the code in this file, please refer to the slides in Lecture21-HTMLRequestsBeautifulSoup.pptx
# You must:
# pip install requests
# pip install beautifulsoup4

import requests
import bs4
import re

URL = 'https://cs111.byu.edu'
response = requests.get(URL)
if response.status_code == requests.codes.ok: # 200 == ok, 404 == not found
    print(f"status_code = {response.status_code}")

print(response.text)


text = """
<html>
  <head>
     <title>Hello world!</title>
  </head>
  <body>
    <h1>Hello world!</h1>
    <h2>Hello world!</h2>
    <p>This is a simple <em>Hello World</em> web page.</p>
    <p>This paragraph has a link to the <a
       href="https://cs111.byu.edu">CS 111 Homepage</a> in it.</p>
    <p>This paragraph has link to the <a
       href="https://cs111.byu.edu/staff">CS 111 Staff page</a> in it.</p>
  </body>
</html>
"""

soup = bs4.BeautifulSoup(text,"html.parser")
print(soup.title)
print(soup.h1)

print(soup.p)
print(soup.find_all('p'))
anchors = soup.find_all('a')
for anchor in anchors:
    print(anchor.attrs)
    print(anchor.attrs['href'])

print(soup.a)
print(soup.a.name)
print(soup.a.attrs)
print(soup.a.attrs['href'])
print(soup.a.string)

for item in soup.body.children:
    print(type(item))
    if (isinstance(item,bs4.Tag)):
        print(item.name)

print(soup.a.parent)
for parent in soup.a.parents:
    print(parent.name)

tags = soup.find_all(re.compile(r'h\d'))
for tag in tags:
    print(tag.name)

strings = soup.find_all(string=re.compile(r'[Hh]ello'))
for string in strings:
    print(string)

strings = soup.body.find_all(string=re.compile(r'CS'))
for string in strings:
    print(string)

print(soup.body)
print(soup.body.prettify())