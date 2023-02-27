from bs4 import BeautifulSoup
import requests
 
import time
from random import randint

import pyttsx3

def clean(d):
    while ('<' in d) and ('>' in d):
        c = ""
        i=0
        while d[i] != '<':
            i+=1
        while d[i] != '>':
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while ('[' in d) and (']' in d):
        #print('[' in d)
        c = ""
        i=0
        while d[i] != '[':
            i+=1
        while d[i] != ']':
            #print('jh')
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while ('{' in d) and ('}' in d):
        c=""
        i=0
        while d[i] != '{':
            i+=1
        while d[i] != '}':
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while (not '<' in d) and ('>' in d):
        c=""
        i=0
        while d[i] != '>':
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while (not '[' in d) and (']' in d):
        c=""
        i=0
        while d[i] != ']':
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while (not '{' in d) and ('}' in d):
        c=""
        i=0
        while d[i] != '}':
            c+=d[i]
            i+=1
        c+=d[i]
        d=d.replace(c,'')
    while ('{' in d) and (not '}' in d):
        i=0
        while d[i] != '{':
            i+=1
        d=d[:i]
    while ('<' in d) and (not '>' in d):
        i=0
        while d[i] != '<':
            i+=1
        d=d[:i]
    d=d.replace('\xa0','').replace('\n','').replace('-',' to ').replace('_P','').replace('←\n','')
    return d
        

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[randint(0,len(voices)-1)].id)

# get URL

class engine():
    def __init__(self):
        self.eng=pyttsx3.init()
        voices = self.eng.getProperty('voices')
        self.eng.setProperty('voice', voices[randint(0,len(voices)-1)].id)
    def say(self,text):
        self.eng.say(text)
    def runAndWait(self):
        self.eng.runAndWait()

while True:
    eng = engine()
    page = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(page.content, 'html.parser')

    r=randint(0,len(soup.find_all('p'))-1)

    try:
        d=str(soup.find_all('p')[r]).split('.')#[randint(1,len(str(soup.find_all('p')[r]).split('.'))-1)]
        #print([d])
        d=clean(d)
        while d=='':
            r=randint(0,len(soup.find_all('p'))-1)
            #print('Main')
            d=str(soup.find_all('p')[r]).split('.')#[randint(1,len(str(soup.find_all('p')[r]).split('.'))-1)]
            #print([d])
            d=clean(d)
        print([d])
        eng.say(d)
    except:
        d=str(soup.find_all('p')[r])
        #print([d])
        d=clean(d)
        while d=='':
            r=randint(0,len(soup.find_all('p'))-1)
            d=str(soup.find_all('p')[r])
            #print([d])
            d=clean(d)
        print([d])
        eng.say(d)

    eng.runAndWait()
    print('\n')
    del(eng)
