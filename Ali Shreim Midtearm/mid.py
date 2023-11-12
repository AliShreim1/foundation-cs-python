import requests
from bs4 import BeautifulSoup# learned from youtube (https://youtu.be/0uiPOxUcLgg?feature=shared)

def addTab(dictionary:dict):
    title=input('Enter the title of the new tab')
    url=input('Enter the url of the page')
    dictionary[title]=url

def closeTab(list:list,index):
    if(index>len(list) or isinstance(index,int)):
        list.pop()
    else:
        list.pop(index-1)

def displyContent(list:list,dictionary:dict,index):
    tab=None
    if(index>len(list) or isinstance(index,int)):
        tab=list[len(list)-1]
    else:
        tab=list[index-1]
    url=dictionary[tab]
    content=requests.get(url)
    print(content.text)

def printTheTitles(list:list):
    for i in list:
        if isinstance(i,list):
            for j in i:
                print(j+" ")
        else:
            print(i+"\n")


def createNestedTabs(dictionary:dict,index):
    x=0
    key=None
    for  i in dictionary.keys():
        if(x==index-1):
            key=i
            break
        else:
            x+=1
    d={}
    while(True):
        title=input('enter a title,you can enter stop to stop \n')
        if(title=='stop'):
            break
        url=input('enter the url \n')
        d[title]=url
    dictionary[key]=d

def clearOpenTabs(list:list):
    list.clear()



            






