import glob
import re
path = 'Chapter '+'*.txt'
files = sorted(glob.glob(path),key=lambda name: int(name[8:-4]))
with open('/Users/u440230/Desktop/TwinePython/temp.txt', 'w') as outfile:
     for name in files:
         with open(name) as infile:
             for line in infile:
                 outfile.write('<h1>'+name[0:name.find('.')]+'</h1>\n')
                 outfile.write('<pre>'+line+'</pre>\n\n')
