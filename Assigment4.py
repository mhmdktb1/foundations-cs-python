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
      self.items.pop[-1]
      self.size-=1
       
def ispalindrome():
   pass
