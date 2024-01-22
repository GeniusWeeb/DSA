
from JustANode import Node
class Linked :

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
        self.current = None
        self.previous = None
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
            
