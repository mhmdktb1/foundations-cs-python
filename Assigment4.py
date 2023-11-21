class Node():
  def __init__(self,value):
    self.value=value
    self.next=None
class Linkedlist():
  def __init__(self):
    self.size=0
    self.head=None
    self.tail=None
  def addnode(self,value):
    node=Node(value)
    if self.size ==0: 
      self.head=node
      self.tail=node   
      self.size+=1
    else:
      self.tail.next=node
      self.tail=node
      self.size+=1
 s