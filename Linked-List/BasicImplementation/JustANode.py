
class Node:
    next= None
    data= None
           
    def __init__(self, value):
        self.data = value
        self.next = None



class DoubleNode(Node):
    def __init__(self, value):
        super().__init__(value) #same as base.Function()
        self.prev =  None
    
    
    
                        