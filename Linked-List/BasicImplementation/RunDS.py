from linkedList import *

if __name__ == "__main__":
    linkedList = DoubleLinkedList()
    linkedList.AddNewNodeAtStart(3)
    linkedList.AddNewNodeAtStart(4)
    linkedList.AddNewNodeAtStart(99)
    linkedList.AddNewNodeAtStart(24)
    
    print("----------------------------------------------------")

    linkedList.ShowAllNodes()
    
    print(f"Current head is {linkedList.head.data}")
    
    linkedList.RemoveLastNode()






