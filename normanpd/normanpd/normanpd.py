#-*- coding: utf-8 -*-
import sqlite3
import PyPDF2 
import re
import urllib.request

conn = sqlite3.connect('normanpd.db')
c = conn.cursor()

def fetchincidents():
    response=urllib.request.urlopen('http://normanpd.normanok.gov/content/daily-activity')
    html=response.read().decode('utf-8')
    fileReg=re.findall(r'/filebrowser_download/657/\d\d\d\d-\d\d-\d\d%20Daily%20Incident%20Summary.pdf',html)
    return(fileReg)
    



###########Create the database

def createdb():
    #conn.execute(''' Drop Table incidents''')  
    c.execute(''' Create Table incidents (
                        id Integer,
                        number Text,
                        date_time Text,
                        location Text,
                        nature Text,
                        ORI Text)''')

##############Fetch all the data and put it in the database

def extractincidents():
    
    ID=0
    ###############Go get url data and extract locations of the incident files
    
    for href in fetchincidents():
        x=[]
        urllib.request.urlretrieve('http://normanpd.normanok.gov'+href,"File.pdf")
        pdfFileObj=open('File.pdf','rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        for page in pdfReader.pages:
            for line in page.extractText().strip().splitlines():
                x.append(line)            
        length=len(x)  
        x=x[5:length-1]
        
    #############parse the pdf and look for desired data    
        
        dictLocX=0
        dictLocY=5
        
        while dictLocY < len(x):
            
            ############### we look for the first column of current line and the first column of the next line to be a date format
            ############## the length between the to potitions has to be 5 or we iterate 1 by 1 unitl we find teh correct pattern
    
            if (re.match(r'.*?:[0-5][0-9]$',x[dictLocX]) and re.match(r'.*?:[0-5][0-9]$',x[dictLocY])):
                ID=ID + 1
                c.execute("Insert Into incidents (id,number,date_time,location,nature,ORI) values (?,?,?,?,?,?)",
                                (ID,x[dictLocX + 1],x[dictLocX],x[dictLocX + 2],x[dictLocX + 3],x[dictLocX + 4]))
                conn.commit()
                dictLocX=dictLocX +5
                dictLocY=dictLocY +5
            else:
                dictLocX=dictLocX + 1
                dictLocY=dictLocY + 1
         
##############db Status            
def status():
    for row in c.execute('Select max(id) from incidents'):
        print('Number of line:')
        print(row)
        print('5 Random Lines:')
    for row in c.execute('Select * from incidents order by random() limit 5'):
        print(row)
    
    conn.execute(''' Drop Table incidents''')    
    conn.close() 
 


