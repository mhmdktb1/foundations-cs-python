def main():
    while True:# here the while loop stops only when we imply break in this case i but break after exit option in case the user finsh fron an option the menu will displyed again 
      display_menu()
      choice = input("Enter your choice from 1 to 9: ")
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
         print("Exiting the Tab Manager. Goodbye!")
         break #the break keyword which stops the while true looping
      else: # if the user choose a number else than we mentioned the menu will displayed agin with an error message 
          print("Exiting program  :(  See u ")
def display_menu():
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
def open_tab():
    pass
def close_tab():
    pass
def switch_tab():
    pass
def display_all_tabs():
    pass
def open_nested_tab():
    pass
def clear_all_tabs():
    pass
def save_tabs():
    pass
def import_tabs():
    pass




