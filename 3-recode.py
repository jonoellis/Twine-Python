import io
with io.open('temp.txt', 'r', encoding='utf8') as f:
    text = f.read()
    text = text.encode().decode('unicode-escape')
with io.open('out.html', 'w', encoding='utf8') as f:
    html_str="<html><head><style>\n@media print {\npre {page-break-after: always;}\n}</style></head><body>"
    f.write(unicode(html_str))
    f.write(text)
