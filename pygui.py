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
app.addLabelEntry("Search word")
app.setLabelBg("l1", "Green")
app.addNumericEntry("csvnumb")
app.setEntryDefault("csvnumb", "Set Number of CSV objects")
app.setFont(20) #app.addLabelSecretEntry("")
csvoarray=["download-url"]
options=["download-url", "view-url","structure-url", "Method-X-ray-Diffraction", "Resolution-1.5A","Residue-Count","Macromocule","Ligands","Search-Match-Score","Citation-title","pdbx-description","struct-title","key-words",""]
csvitem="CSV-item-"
def press(button):
    if button == "Exit":
        app.stop()
    elif button == "Set-CSV-#":
        csvnumb=app.getEntry("csvnumb")
        one=0
        while one < csvnumb and one < len(options) :
            try:
                app.addLabelOptionBox(csvitem+str(one),options)
            except:
                print("Already have a "+csvitem+str(one))
            one=one+1
    elif button == "Set-CSV-options":
        var=True
        numbe=0
        while var:
            try:
                app.getEntry("csvitem"+str(numbe))
            
    elif button == "Search"
        word = app.getEntry("Search word")
        print("Search word:"+word) #, "Pass:", pwd)
        strg=numm(word)
        print(str(strg))
app.addButtons(["Search","Set-CSV-#","Set-CSV-options", "Exit"], press)
app.addLabelOptionBox(csvitem+"0",options)
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
        app.addLabel("l1",searchTotal+str(thing))
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
