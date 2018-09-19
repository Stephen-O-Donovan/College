from docx import Document
from docx import opc
import subprocess as sp

wordLoc = 'C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.exe'

def Convert( readFile ):

    writeFile = readFile[:-5] + 'c' + '.docx'
    
    dic = {'\\ne':'\u2260', '\pm':'\u00B1', '\quarter':'\u00BC', '\half':'\u00BD',
           '\\null':'\u00F8', '\spi':'\u03C0', '\sigma':'\u03A3',
           '\le':'\u2264', '\ge':'\u2265' , '\\nfty':'\u221E',
           '\sqrt':'\u221A', '\in':'\u2208'}
    try:
        d = Document(readFile)
        for p in d.paragraphs:
            inline = p.runs
            for i in range(len(inline)):
                for key, value in dic.items():
                    if key in inline[i].text:
                        print('Found key %s, replacing with value %s' % (key, value))
                        inline[i].text = inline[i].text.replace(key,value)
        
    except opc.exceptions.PackageNotFoundError:
        return print('*** Convert: PackageNotFoundError -- Could not open file %s for reading' % readFile)
    except FileNotFoundError:
        return print('*** Convert: FileNotFoundError -- Could not open file %s for reading' % readFile)
    try:
        d.save(writeFile)
    except IOError:
        return print('*** Convert: IOError -- Could not open file %s for writing' % writeFile)
    print('Successfully converted file %s to file %s' % (readFile, writeFile))
    try:
        sp.Popen([wordLoc, readFile])
        sp.Popen([wordLoc, writeFile])
    except FileNotFoundError:
        return print('*** Convert: FileNotFoundError -- Could not locate %s' % wordLoc)
