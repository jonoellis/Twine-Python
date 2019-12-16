import sys
from bs4 import BeautifulSoup

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def remove_postfix(text, postfix):
    if text.endswith(postfix):
        return text[:-len(postfix)]
    return text

page = open(sys.argv[1])
soup = BeautifulSoup(page.read(),"lxml")
chapters = soup.find_all('tw-passagedata')
for chapter in chapters:
    title = chapter.get('name')
    content = chapter.contents
    content = str(content)
    content = remove_prefix(content,'[u\'')
    content = remove_prefix(content,'[u\"')
    content = remove_postfix(content,'\"]')
    content = remove_postfix(content,'\']')

    with open(title+'.txt','w') as oFile:
        oFile.write(content)
        oFile.close()
