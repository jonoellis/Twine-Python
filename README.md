# Twine-Python
Twine is a great tool for creating non-linear stories, but not for creating a book with the chapters in order. These Python scripts fix that by taking all of your linked chapters (named "Chapter 1", "Chapter 23", "Chapter 132", etc) and splits them into multiple text files, sorts them and puts them back into a single HTML document. 

Steps:
* Copy your Twine source file to a folder with your Python scripts - on a Mac this seems to be stored at /Users/USER/Documents/Twine/Stories/STORY.html 
* Run the following three scripts: 
```
python 1-split.py STORY.html 
python 2-merge.py 
python 3-recode.py 
```
* Your new document will be created as ```out.html```
