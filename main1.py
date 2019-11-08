import urllib.parse
import urllib.request
import bs4 as soup
import speech_recognition as sr
from retry import retry

def wikisearch(a):
    spl=a.split(" ")
    quer=""
    for i in spl:
        quer=quer+i+"_"
    url="https://en.wikipedia.org/wiki/"+ quer
    raw_data=urllib.request.urlopen(url).read()
    ripe_data=soup.BeautifulSoup(raw_data,"html.parser")
    data=ripe_data.find_all('p')
    invalid=a + " may refer to:"
    for para in data:
        print(para.text)
        if(para.text== invalid):
            print("Please elaborate your search")

def getvoice():
    @retry(Exception,delay=0)
    def rerunThis():
        rec=sr.Recognizer()
        with sr.Microphone() as source:
            aud=rec.listen(source)
        ret=rec.recognize_google(aud)
        return ret
    retret=rerunThis()
    return retret

while(1):
    fil=open("history.txt","a")
    search=getvoice()
    print(search)


    if(search=="EXIT"):
        break
    else:
        fil.write(search+"\n")
        fil.close()
        try:
            wikisearch(search)
        except Exception as e: print("Something Went Wrong -",e)
#MODIFIED AND OPTIMIZED BY Agrim2411
#hope it gets merged

