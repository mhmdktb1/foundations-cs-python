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
            print(current.value, end=" ")
            current = current.next
        print()

   def enqueue(self,value):
       
       node=Node(value)
       if self.size==0:
        self.head=node
        self.rear=node
        self.size+=1
        print("Added to the Q:",value )
       else:
          self.rear.next=node
          self.rear=node
          self.size+=1
          print("Added to the Q:",value )

   def dequeu(self):
    if self.size == 0:
        print("Your Queue is Empty! Enqueue first.")
    elif self.size == 1:
        print("We are removing:", self.head.value)
        self.head = None
        self.size -= 1
    else:
        if self.head is not None:
            print("We are removing:", self.head.value)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
        else:
            print("Unexpected error: self.head is None.")

def ispalindrome():
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
   st.clear
   list1.clear   
