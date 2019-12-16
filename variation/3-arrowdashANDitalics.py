import io
import re
import codecs
with io.open('temp.txt', 'r', encoding='utf8') as f:
    text = f.read()





# Replace __ with </i>

    text = re.sub(ur'__(.+?)__', ur'"<em>\1</em>"', text)
# Replace [[Chapter 54<-54]] with 54
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)
    text = re.sub(ur'\[\[Chapter\s(\d)\d\<\-(\d\d)\]\]', ur'\2', text)

# Remove square brackets from chapters [[Chapter 54]]
    text = re.sub(ur'\[\[', ur'', text)
    text = re.sub(ur'\]\]', ur'', text)





with codecs.open('temp2.txt', 'w', "utf-8") as file:

    file.write(text)
    file.close()
