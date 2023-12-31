import requests
from bs4 import BeautifulSoup
import json #importing json library
#learned how to scrap html from greeksforgreeks
tab={}#this dictionry will conains the title,url,content,nestedtabs
list=[]#this list will contains all the added tabs
def main():#o(1)
    while True:# here the while loop stops only when we imply break in this case i but break after exit option in case the user finsh fron an option the menu will displyed again 
      print("---------------------------")
      display_menu()
      print("-"*20)
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
    title=input("Type a title : ")
    url=input("Type a url : ")

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
        print("added Succefully ")
          # Each tab we make as a dic should listed in a list to save all tabs in a one list to be able to call them buy there indeces 
    else : 
       print("Invailed url")    
def close_tab():#O(1)
    # Taking index from the user and checking if the index provided buy comaring the index buy the len -1 of the list
    #if the index isn;t provided we delete last opened tab buy using -1 wich acces the last index of the list 
    #else we pop the index given from the list
    try: #trying the code and test it
        index=int(input("Enter the index of the tab you want to close : "))
    except ValueError:#handling the error if its found
       print("Error: Please enter a valid integer.") 
    else:#if there is no error it will run correctely
       if len(list)==0:#cheaking if the list is  empty 
          print("There are no tabs added")
       elif index >len(list)-1 :#cheaking if the index the user enter is provided
         print("The index You entered is not provided the last tast tab u added will be deleted ")
         list.pop(-1)
         print(list[-1]["Title"],"Deletd Succefully") 
       else :
          list.pop(index)
          print(list[index]["Title"],"Deletd Succefully")
def switch_tab():#O(1)
    try:
        index=int(input("enter the index of the tab you want to display:"))
    except ValueError:
        print("Error : please enter a valied integer")  
    else :
        if len(list)==0:#cheaking if the list is not empty 
            print("There is no tabs added")
        elif index >len(list)-1 :# cheaking if the index in the list
            print("The index You entered is not provided the last tast tab u added will be displayed : ")
            print(display_content(-1))
        else:
            print(display_content(index))#make a method to display the content and use it here         
def display_all_tabs():#O(n)
    if len(list) == 0 :
        print("There is no tabs opened to display") 
    else:
        for i in range(len(list)):#iterating over the list 
            print(list[i]["Title"])#printing the title of each tab in the list 
            if len(list[i]["nested_tab"]) >= 1:#cheaking if there any nested tab 
                print("\t -",list[i]["nested_tab"][0]["Title"])#printing the title of the nested tab
def open_nested_tab():#O(n)
    try: #trying the code and test it
        index=int(input("Enter the index of the tab you want to close : "))
    except ValueError:#handling the error if its found
       print("Error: Please enter a valid integer.")     # taking the index of the tab he wants to add in then taking the from the user the info of this nested tab                                                                  
    else :
        if len(list)==0:#cheaking if the list is not empty 
            print("There is no tabs added")
        elif index >len(list)-1 :
            print("There is no tab in such index ")
        else:
            title=input("Type a title : ")
            url=input("Type a url : ")
            if url.startswith("https"):
                req=requests.get(url)#requesting to get the url 
                content=BeautifulSoup(req.content,"html.parser")#declaring variable content that contains the content of the url
                #create a new dictiony to take the content od the nested tab
                nested_tab={"Title":title,
                "url" :url ,
                "content" : content.prettify()#getting the html code
                }
                list[index]["nested_tab"].append(nested_tab)# access by the index we take the tab we want then we access the nested tab to store the info in it as a new tab   
                print("added Succefully ")
            else:
                print("Invailed url")
def clear_all_tabs():#O(1)
    if len(list)==0:
        print("There no tabs already")
    else :
        list.clear()#simple build in function to clear all tabs
        print("All tabs deleted!")
def save_tabs():
    # used to learn from youtube channel "finxter"
    if len( list) == 0:
      print("There are no tabs to save")
    else:
        try:
           file = input("Enter the file path: ")  # Taking the file path from the user

           with open(file, "w") as file:  # Opening the file path as a file "w" for writing in it
                json.dump(list, file)#save the list into the file 
           print("Saved Successfully")
        except FileNotFoundError:
             print("Error: File path not found or incorrect") 
def import_tabs():
    try:   
      file=input("The file path : ")
    
      with open(file,"r")as file:#reding a file 
         data=json.load(file)#variable data to load the data of the file 
         list.extend(data)# i was facing error by appending in athor function because of the format of the list so i used extend instead of append its simply take the tab from the file not the whole list
      print("Imported Succesfully ")
    except FileNotFoundError :#cheack if the path is found
          print("Error : File path is uncorrect ")
def display_content(i):#O(1)
    #accessing the content
    return list[i]["content"]

main()
