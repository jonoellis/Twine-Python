from bs4 import BeautifulSoup, Tag
page = open('/Users/u440230/Desktop/TwinePython/temp3.html')
soup = BeautifulSoup(page.read(),"html5lib")

for tag in soup.find_all('comment'):
    tag.replaceWith('')

with open('/Users/u440230/Desktop/TwinePython/out.html', "w") as file:
    file.write(str(soup))
