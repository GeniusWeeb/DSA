
from JustANode import Node , DoubleNode

### Util class for all kind of Linked List


#Sequential data structure -> Entry via head only 
#Search time complexity for anything other than head or tail is Linear else constant for them.

class Linked :
      def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
        self.current = None
        self.previous = None
        
        

#node only points in front
class SingleLinked(Linked) :
    def __init__(self):
        super().__init__()
#Inserting the node at the begining    

    #Time complexity -> O(1)
    def AddNodeAtStart(self,value):
        n =  Node(value)
        
        #Add the node here
        if self.head == None:  #List is empty,  and this is the first entry
           self.tail = self.head = n
            
        else: # considering there are only 2 elements and this new node is the 2nd one
            n.next=  self.head  # head.next currently is Null , 
            self.head = n
            
        self.size+=1
        print( f"Added new node with data-> {value} , size is {self.size} ")
           
    #Time complexity -> O(1)        
    def AddLastNode(self,value):
        n = Node(value)        
        
        
        #Pretty much if head is None .tail is gonna be nu\ll
        if self.head == None:
            self.head =n  
        
        else:
            self.tail.next = n
            self.tail = n                    
            n.next = None
    
        self.size+=1       
    
    #Remvoes the first element from the Linked list1
    #Time complexity of O(1)
    def RemoveFirst(self):

        if self.head == None:
            return "This List is Empty"
        #Means there is just 1 element in the whole list    
        if self.head == self.tail:
            self.head = self.tail = None
        #More than 1 element in the Linked List    
        else :
            self.head = self.head.next
    
        self.size-=1        

    #Time complexity -> Linear -> O(n)
    def RemoveLast(self):  
        #Empty
       
        if self.head == None:
            return

       #1 element Remove O(1)
        if self.head == self.tail:
            self.head = self.tail = None    
            return 
        
        self.current = self.head
           
      #2 O(n) -> Linear Complexity  
        while(self.current.next != None): #if you do self.current == null -> you bascially arrive at a null pointer
            self.previous =  self.current
            self.current =  self.current.next
      #want this to break when we encounter the last element

            if self.current == self.tail :  #Not usefull but still a check for the final element
                self.previous.next = None
                self.tail = self.previous
    
        self.size-=1  
     
    #Time complexity -> Linear -> O(n)       
    #We need to add a Find and contain  
    def ContainsElement(self, value):
        self.current = self.head   
             
        while(self.current != None):  #important so we dont skip the last element
            if self.current.data == value:
                return True
            self.current = self.current.next            
     
        return False        
    #Gets the position
    def SearchAndGetPosition(self, value):
        pos = 0
        self.current = self.head
        
        while(self.current is not None):
            
            if value == self.current.data:
                return pos+1
            
            self.current =  self.current.next
            pos+=1
        
        return None       

    #Time complexity -> Linear -> O(n)
    def ShowAllNodes(self):
        self.current = self.head
        while(self.current is not None):
            print(f"{self.current.data} and next is {self.current.next}")
            self.current = self.current.next
            self.DrawThisNode(self.current.data)


# Node has previous node pointer as well
class DoubleLinkedList(Linked):  
    def __init__(self):
        super().__init__()  
        
    #Add the node at the start  -> O(1)          
    def AddNodeAtStart(self, value):
        node = DoubleNode(value)
        
        if self.head is None:
            self.head = node 
            self.head.prev  = None
            return
        
        #more than 1 element
        self.head.prev = node
        node.next = self.head  # we are assigning the node present at the head of the List to the next pointer
        self.head = node
        self.head.prev = None
        
        self.size+=1
        
    #Add the node at the end -> O(1) after the tail is defined but
    #In general terms additions at the end is Linear Time O(n)
    def AddNewNodeAtTheEnd(self,value):
        
        newNode = DoubleNode(value)
    
        #if the head is None ,empty List just add the node    
        if self.Head is None:
            self.AddNewNodeAtStart(value)
            return
   
        self.current = self.head

        while self.current.next is not None:
            self.previous = self.current
            self.current = self.current.next

        #break when the next pointer says null        
        
        self.current.next = newNode
        self.tail = newNode  #tail now contains the default implment of the node , i.e all None
        self.tail.next = None
        self.tail.prev = self.current
       
        
        self.size+=1
        
    
    def RemoveFirstNode(self):
        
        if self.head is None:   
            return "Empty List ! nothing to remove"
        if self.head.next is None: #1 element
            self.head = None
            print("Removed element")
        
        #More than 1 element , just break the Link
        self.head = self.head.next 
        self.head.prev = None    
            
    def RemoveLastNode(self):
        
        if self.head == None:
           return 
        
        if self.head.next is None : # 1 element
            self.head = None
            self.size -=1
            return
        
        self.current = self.head
        
        while self.current.next is not None:
            self.previous = self.current
            self.current = self.current.next  
            
        self.tail= self.previous
        self.tail.next = None
        self.size-=1           
        print(f"Remove last node , current last node is {self.tail.data} and its previous element is {self.tail.prev.data}" )
        
    #Just iterate and print 
    def ShowAllNodes(self):
        
        self.current = self.head
        while self.current is not None: 
            print(f"node is ->{self.current.data}")
            self.current = self.current.next 


#The last element is poting to the first element
class CircularLinkedList(Linked):
    
    def __init__(self):
        super().__init__()
    
    
    def AddNodeAtStart(self, value):    
        #just to have best of both in case, we go for the doubly linkned circular list    
        new_node = DoubleNode()
        if self.head is None:   
            self.head = new_node = self.tail  
            self.head.next = new_node 
            self.tail.next = new_node
            return
        
        #add new element, connec the next of current head to this
       #Circular
        new_node.next =self.head       
        self.tail.next = new_node 
        self.head.next = new_node
        self.head = new_node
        

        #Computation mostly same 
        #Never has null , last node points to HEAD so always iterate till there
            
    
    
        
