import requests
from bs4 import BeautifulSoup
import json #importing json library
#learned how to scrap html from greeksforgreeks
tab={}
list=[]
def main():#o(1)
    while True:# here the while loop stops only when we imply break in this case i but break after exit option in case the user finsh fron an option the menu will displyed again 
      print("---------------------------")
      display_menu()
      print("---------------------------")
      choice = input("Enter your choice from 1 to 9 : ")
      if choice == '1':
         open_tab()
      elif choice == '2':
         close_tab()
      elif choice == '3':
         switch_tab()
      elif choice == '4':
         display_all_tabs()
      elif choice == '5':
         open_nested_tab()
      elif choice == '6':
         clear_all_tabs()
      elif choice == '7':
         save_tabs()
      elif choice == '8':
         import_tabs()
      elif choice == '9':
         print("Exiting program  :(  See u ")
         break #the break keyword which stops the while true looping
      else: # if the user choose a number else than we mentioned the menu will displayed agin with an error message 
          print("Number should be in range of 1_9 ")
def display_menu():#O(1)
    #printing the menu 
    print("Welcome to the Tab Manager!")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
def open_tab():#O(n)
    title=input("web's name u want to add : ")
    url=input("The url of this title : ")

    if  url.startswith("https"): #cheak if the url stating by https it will reply error message
        req=requests.get(url)#requesting to get the url 
        content=BeautifulSoup(req.content,"html.parser")#declaring variable content that contains the content of the url
        tab={"Title":title,
          "url" :url ,
           "content" : content.prettify(),#getting the html code
           "nested_tab":[] #creating a list to contains the nested tab
         }
         #I take from the user the title and the url and then ad the to a dictonary 
        list.append(tab)
          # Each tab we make as a dic should listed in a list to save all tabs in a one list to be able to call them buy there indeces 
    else : 
       print("Invailed url")    
def close_tab():#O(1)
    # Taking index from the user and checking if the index provided buy comaring the index buy the len -1 of the list
    #if the index isn;t provided we delete last opened tab buy using -1 wich acces the last index of the list 
    #else we pop the index given from the list
    index=int(input("Enter the index of the tab you want to close : "))
    if len(list)==0:#cheaking if the list is  empty 
        print("There are no tabs added")
    elif index >len(list)-1 :#cheaking if the index the user enter is provided
       print("The index You entered is not provided the last tast tab u added will be deleted ")
       list.pop(-1)
       print(list[-1]["Title"],"Deletd Succefully") 
    else :
        list.pop(index)
        print(list[index]["Title"],"Deletd Succefully")
def switch_tab():
    
    index=int(input("enter the index of the tab you want to display:"))
    if len(list)==0:#cheaking if the list is not empty 
        print("Ther is no tabs added")
    elif index >len(list)-1 :# cheaking if the index in the list
        print(display_content(-1))
    else:
        print(display_content(index))#maked a method to display the content and use it here         
def display_all_tabs():
    for i in range(len(list)):#iterating over the list 
        print(list[i]["Title"],end = ",")#printing the title of each tab in the list 
        if len(list[i]["nested_tab"]) >= 1:#cheaking if there any nested tab 
            print("and its nested tab ",end = ":")
            print(list[i]["nested_tab"][0]["Title"])#printing the title of the nested tab
def open_nested_tab():
    index=int(input("The index of the tap you want to add in it nested tabs"))
    # taking the index of the tab he wants to add in then taking the from the user the info of this nested tab                                                                  
    if len(list)==0:#cheaking if the list is not empty 
        print("Ther is no tabs added")
    elif index >len(list)-1 :
        print("there is no tab in such index ")
    else:
         title=input("web's name u want to add : ")
         url=input("The url of this title : ")
         req=requests.get(url)#requesting to get the url 
         content=BeautifulSoup(req.content,"html.parser")#declaring variable content that contains the content of the url

         nested_tab={"Title":title,
          "url" :url ,
           "content" : content.prettify(),#getting the html code
           "nested_tabs":[] 
        }
         list[index]["nested_tab"].append(nested_tab)# access by the index we take the tab we want then we access the nested tab to store the info in it as a new tab   
def clear_all_tabs():
    list.clear()#simple build in function to clear all tabs
def save_tabs():
    file=input("The file path : ")#taking the file path from the user
    with open(file,"w")as file:#opening the file path as a file "w" for writing in it , 
     json.dump(list,file)
def import_tabs():
       
     file=input("The file path : ")
    
     with open(file,"r")as file:
         data=json.load(file)#variable data to load the data of the file 
         list.extend(data)# i was facing error by appending in athor function because of the format of the list so i used extend instead of append its simply take the tab from the file not the whole list
def display_content(i):
    #accessing the content
    return list[i]["content"]

