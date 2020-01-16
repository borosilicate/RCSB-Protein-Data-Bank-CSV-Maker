from appJar import gui
import urllib.request, urllib.parse, urllib.error
import subprocess
from bs4 import BeautifulSoup
import re
import csv

app=gui()
app.addLabel("title","RCSB-Protein-Data-Bank-CSV-Maker")
app.setLabelBg("title", "Green")
app.setFont(12)
searchTotal="Search Total is "
thing="0"
app.addLabel("l1",searchTotal+thing)
app.addLabelEntry("Search word")
app.setLabelBg("l1", "Green")
app.addNumericEntry("csvnumb")
app.setEntryDefault("csvnumb", "Set Number of CSV objects")
app.addLabelEntry("File-name")
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
                options[0],options[one]=options[one],options[0]
                app.addLabelOptionBox(csvitem+str(one),options)
                options[0],options[one]=options[0],options[one]
            except:
                print("Already have a "+csvitem+str(one))
            one=one+1
    elif button == "Write-File":
        var=True
        numbe=0
        while var:
            try:
                csvtoarray[numbe]=app.getEntry("csvitem"+str(numbe))
            except:
                print("Write Files All items added up to "+str(numbe))
            numbe=numbe+1
        
    elif button == "Search":
        word = app.getEntry("Search word")
        print("Search word:"+word) #, "Pass:", pwd)
        strg=numm(word)
        print(str(strg))
    elif button == "Help":
        helpMessage="This is a program to create a csv file from the rCSB database.\n"
        helpMessage+="Search will return the quantity of lines to write.\n"
        helpMessage+="Write-File will write to the name set in the blank or default.csv if blank.\n"
        helpMessage+="Write-File will take multiple arguments in a blank and seperate them by comma"
        helpMessage+="Set-CSV-# will add blanks to the csv file unfortunaly they can not be removed.\n"
        helpMessage+="Exit and Help are self explanatory..."
        app.infoBox("RCSB-Protein-Data-Bank-CSV-Maker",helpMessage , parent=None)
app.addButtons(["Search","Write-File","Set-CSV-#","Exit","Help"], press)
app.addLabelOptionBox(csvitem+"0",options)
def numm(querry,write=False):
    html = urllib.request.urlopen("http://www.rcsb.org/pdb/search/navbarsearch.do?f=&q="+querry).read()
    qrid=None
    thing="Still Not working"
    if html is not None:
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('a'):
            #print(link.get('href'))
            if("qrid=" in str(link.get('href')) ):
                #print(link.get('href'))
                qrid=re.sub(r'.*qrid=', '', str(link.get('href'))).strip()
                print("qrid="+qrid)
                #qrid=link.get('href').strip('http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid=')
    if qrid is not None:
        print("in not none qrid==",qrid)
        #http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid=4BEA411F
        html2 = urllib.request.urlopen("http://www.rcsb.org/pdb/results/results.do?tabtoshow=Current&qrid="+qrid).read()
        soup2 = BeautifulSoup(html2, 'lxml')
        #<span id="getResultSizeValue">28590</span>
        count=soup.find_all('a',class_='Current')
        count=str(count).split()[4] 
        print("soup.find_all(resultsize id)",str(thing))
        app.setLabel("l1",searchTotal+str(count))
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
