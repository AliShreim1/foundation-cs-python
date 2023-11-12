import requests
from bs4 import BeautifulSoup# learned from youtube (https://youtu.be/0uiPOxUcLgg?feature=shared)
import json

def addTab(dictionary:dict,list:list):
    title=input('Enter the title of the new tab')
    url=input('Enter the url of the page')
    dictionary[title]=url
    list.append(title)

def closeTab(list:list,index):
    if(index>len(list) or isinstance(index,int)):
        list.pop()
    else:
        list.pop(index-1)

def displyContent(list:list,dictionary:dict,index):
    tab=None
    if(index>len(list) or not isinstance(index,int)):
        tab=list[len(list)-1]
    else:
        tab=list[index-1]
    url=dictionary[tab]
    content=requests.get(url)
    soup=BeautifulSoup(content.text,'lxml')
    return soup

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

def saveAsJsonFile(filepath,dictionary,openTabs):
    file=filepath
    content=[]
    for i in range(len(openTabs)):
        content.append(displyContent(openTabs,dictionary,i).prettify())
    with open(file,'w') as jfile:
        json.dump(dictionary,jfile)
        json.dump(openTabs,jfile)
        for i in content:
            json.dump(i,jfile)
    print('save is done')

def stop():
    exit()


openTabs=[]
tabs={}

while(True):
    print("Menu:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    choice=input('Enter a number \n')
    if choice == "1":
        addTab(tabs,openTabs)
    elif choice == "2":
        index=int(input('enter the index'))
        closeTab(openTabs,index)
    elif choice == "3":
        index=int(input('enter the index'))
        displyContent(openTabs,tabs,index)
    elif choice == "4":
        printTheTitles(openTabs)
    elif choice == "5":
        index=int(input('enter the index'))
        createNestedTabs(tabs,index)
    elif choice == "6":
        clearOpenTabs(openTabs)
    elif choice == "7":
        path = input("Enter file path to save tabs: ")
        saveAsJsonFile(path,tabs,openTabs)
    elif choice == "8":
        print('.')
    elif choice == "9":
        stop()
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")