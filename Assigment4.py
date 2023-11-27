user=input("Type your name : ")
class Node():
  def __init__(self,value):
    self.value=value
    self.next=None
class Linkedlist():
  def __init__(self):
    self.size=0
    self.head=None
    self.tail=None
  def addnode(self):
     value=eval(input("Enter a numerical value : "))
     node=Node(value)
     if self.size ==0: 
         self.head=node
         self.tail=node   
         self.size+=1
     else:
         self.tail.next=node
         self.tail=node
         self.size+=1
  def display(self):
     print('The size : ',self.size)
     current=self.head
     if self.size ==0: 
         print('The linked list is empty')
     else :
         while current != None:
             print(current.value,end=" ")
             current=current.next
  def searchdel(self):
       print("The size :",self.size)
       if self.size < 1:
          print('The linked list is empty')
       else:
          val=eval(input("Enter a value to delete : "))
          current=self.head
          pointer=current
          while current is not None:
            if current.value == val:
              if self.size==1 :
                self.head=self.tail=None
                self.size-=1
                break
              elif self.head.value==val:
                self.head =self.head.next
                current=self.head
                pointer=current
                self.size-=1
              elif current.value == val:
                pointer.next=current.next
                current=current.next
                self.size-=1
            else:
                pointer=current
                current=current.next
class stack():
   def __init__(self):
      self.items=[]
      self.size=0
   def add(self):
     s=input("enter a string : ")
     self.items=list(s)
     self.size+=len(s)
   def pop(self):
      poped=self.items.pop()
      self.size-=1
      return poped 
   def clear(self):
      self.items.clear()
class Queue():
   def __init__(self):
      self.head=None
      self.rear=None
      self.size=0
   def display(self):
        current = self.head
        while current:
            print(current.value.name, end=" ")
            current = current.next
        print()

   def enqueue(self,student):
       current=self.head
       node=Node(student)
       if self.size==0:
          self.head=node
          self.size+=1
       else:
             current=self.head
             previous = None
             while current :
                 if node.value.attitude ==  current.value.attitude:
                   if node.value.final == current.value.final:
                      if node.value.mid == current.value.mid:
                          node.next = current
                          if previous:
                             previous.next = node
                          else:
                             self.head = node
                          self.size += 1
                          break
                      elif node.value.mid > current.value.mid:
                          node.next = current
                          if previous:
                             previous.next = node
                          else:
                             self.head = node
                          self.size += 1
                          break
                      else :
                          previous = current
                          current = current.next
                   elif node.value.final > current.value.final:
                      node.next = current
                      if previous:
                         previous.next = node
                      else:
                         self.head = node
                      self.size += 1
                      break
                   else:
                      previous = current
                      current=current.next
                 elif node.value.attitude == True:
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    self.size += 1
                    break
                 elif node.value.attitude is False:
                     node.next=None
                     while current.next is not None:
                          current=current.next  
                     current.next=node
                     self.size+=1
                     break
                 else :
                    previous = current
                    current=current.next 
   def dequeu(self):
    if self.size == 0:
        print("Your Queue is Empty! Enqueue first.")
    elif self.size == 1:
        print("We are removing:", self.head.value.name)
        self.head = None
        self.size -= 1
    else:
        if self.head is not None:
            print("We are removing:", self.head.value.name)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
        else:
            print("Unexpected error: self.head is None.")
class Student():
   def __init__(self,name,mid,final,attitude):
    self.name=name
    self.mid=mid
    self.final=final
    self.attitude=attitude
class Graph():
    def __init__(self):
        self.numvertix=0
        self.matrix=[[0]*self.numvertix for _ in range(self.numvertix)]
    def AddV(self):
        self.numvertix+=1
        self.matrix=[[0]*self.numvertix for _ in range(self.numvertix)]
        print(f"Vertix '{self.numvertix-1}' added succesfully ")
    def AddE(self):
       while True:
         edge1=int(input("The first vertix : "))
         edge2=int(input("The second vertix : "))
         if edge1 or edge2 <= self.numvertix-1:
            break
         else:
            print("Those edjes dosnt exist reenter them ")

       self.matrix[edge1][edge2]=1
    def RemoveV(self):
       while True:
          
         v=int(input(" The vertix number : "))
         if v<=self.numvertix-1:
            break
         else:
            print("Vertix doesnt exist ! Renter please ")
       self.matrix.pop(v)
       self.numvertix-=1
    def RemoveE(self):
       while True:
         edge1=int(input("The first vertix : "))
         edge2=int(input("The second vertix : "))
         if edge1 or edge2 <= self.numvertix-1 :
            break
         elif self.matrix[edge1][edge2]==0:
            print("there already No edje here ! Renter another edje ")
         else:
            print("Those vertices dosnt exist Enter vailid ones ! ")
       
       self.matrix[edge1][edge2]=0
    def degree(self):
       X=int(input("Enter an integer : "))
       for row in range(len(self.matrix)):
         s=sum(self.matrix[row])
         if s>=X:
            print(row,end=", ")               
    def dis(self):
        for i in self.matrix:
          print('  '.join(map(str,i)))
queue=Queue()
def Queue_menu():
      while True:
         print("--------------------------")
         print("a. Add a student")
         print("b. Interview a student")

         print("d. Return to the main menu")
         print("--------------------------")
         choice = input("Enter your choice: ")

         if choice == 'a':
            name = input("Enter student name: ")
            mid = int(input("Enter midterm grade (0-100): "))
            final = int(input("Enter final grade (0-100): "))
            attitude = input("Does the student have a good attitude? (True/False): ").lower()
            if attitude == 'true':
               attitude=True
            elif attitude=='false':
               attitude=False

            student = Student(name, mid, final, attitude)
            queue.enqueue(student)
            print(f"{student.name} added to the queue.")

         elif choice == 'b':
            queue.dequeu()
         elif choice == 'c':
            main()
         else:
            print("Invalid choice. Please enter a, b, or c .")
g=Graph()
def Graph_menu():
   while True:
      
      print("-----------------------")
      print("a. Add vertex \nb. Add edge \nc. Remove vertex \nd. Remove edge \ne. Display vertices with a degree of X or more. \nf. Return to main menu")
      print("-----------------------")
      option=input('Type your choice : ')
      if option=='a':
         g.AddV()
      elif option=='b':
         g.AddE()
      elif option=='c':
         g.RemoveV()
      elif option=='d':
         g.RemoveE()
      elif option=='e':
         g.degree()
      elif option=='f':
         main()
l=Linkedlist()
def Linkedlist_menu():
    while True:
        print("---------------------------")
        print("1. Add Node")
        print("2. Display Nodes")
        print("3. Search for & Delete Node")
        print("4. Exit")
        print("---------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            l.addnode()
        elif choice == '2':
            l.display()
        elif choice == '3':
            l.searchdel()
        elif choice == '4':
            main()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
def ispalindrome():
   print("----------------")
   list1=[]
   st=stack()
   st.add()
   mid=st.size//2
   for i in range(mid):
      char=st.pop()
      list1.append(char)
   if len(list1)==st.size:
      if st.items==list1:
         print("palindrome")
      else:
         print("Not palindrome")
   else:
      if st.items[:mid]==list1:
         print('palindrome')
      else:
         print("Not palindrome")
   print("----------------")
   st.clear
   list1.clear  
def main():
   count=0
   
   while count<5:
    print("Welcome back",user)
    print("-------------------------------")
    print("1. Singly Linked List")
    print("2. Check if Palindrome")
    print("3. Priority Queue")
    print("4. Evaluate an Infix Expression")
    print("5. Graph")
    print("6. Exit")
    print("--------------------------------")
    choice = input("Enter the number of your choice (1-6): ")

    if choice == '1':
        Linkedlist_menu()
    elif choice == '2':
        ispalindrome()
    elif choice == '3':
        Queue_menu()
    elif choice == '4':
        print("This feature wil be added soon :)")
    elif choice == '5':
        Graph_menu()
    elif choice == '6':
        print("Goodbye",user,"see you soon !")
        break
    else:
        count+=1
        print("Invalid choice. Please enter a number between 1 and 6.")
main()        