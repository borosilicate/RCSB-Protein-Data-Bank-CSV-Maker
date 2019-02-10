from appJar import gui
import urllib.request, urllib.parse, urllib.error
import subprocess
from bs4 import BeautifulSoup
import re
app=gui()
app.addLabel("title","RCSB-Protein-Data-Bank-CSV-Maker")
app.setLabelBg("title", "Green")
searchTotal="Search Total is "
thing="0"
app.addLabel("l1",searchTotal+thing)
app.setLabelBg("l1", "Green")
app.addLabelEntry("Search word")
app.setFont(20)
#app.addLabelSecretEntry("")
app.addLabelSpinBox("options", ["", "Orange", "Pear", "kiwi"])

def press(button):
    if button == "Exit":
        app.stop()
    else:
        word = app.getEntry("Search word")
        print("User:", word) #, "Pass:", pwd)
        strg=numm(word)
        print(str(strg))
app.addButtons(["Search", "Exit"], press)

def numm(querry):
    html = urllib.request.urlopen("http://www.rcsb.org/pdb/search/navbarsearch.do?f=&q="+querry).read()
    qrid=None
    thing="Still Not working"
    if html is not None:
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('a'):
            print(link.get('href'))
            if("qrid=" in str(link.get('href')) ):
                qrid=re.sub(r'\w+qrid=', '', str(link.get('href')))
                #qrid=link.get('href').strip('http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid=')
    if qrid is not None:
        print("qrid==",qrid)
        #http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid=4BEA411F
        html2 = urllib.request.urlopen("http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid="+qrid).read()
        soup = BeautifulSoup(html2, 'lxml')
        #<span id="getResultSizeValue">28590</span>
        thing=soup.find_all(id="getResultSizeValue")
        print(str(thing))
        app.addLabel("l1",searchTotal+thing)
        for tag in soup.find_all(thing):
            print(str(tag))
        print(str(thing)+" YES WORKING!!!")
    else:
        print("ERROR No qrid= value found ERROR")
    #front="curl http://www.rcsb.org/pdb/search/navbarsearch.do?f=&q="
    #return_code= subprocess.call([front, shell=True])
    #app.addLabelEntry("Found",str(thing))
    return thing




app.go()
