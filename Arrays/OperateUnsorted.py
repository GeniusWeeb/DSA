#Time complexity -> Linear , since this is unsorted array

#region Unsorted methods
def FindElement(list_ , n):
    size = len(list_)
    for x in range(size):
        if list_[x]== n:
            return x
    return -1       

def InsertElementUnsorted(arr , pos , elem):
    size = len(arr) -1
    #size and start from size-1 and step -1 every iteration    
    for i in range(size-1,pos-1,-1):
        if(arr[i] == -1):
            continue
        arr[i+1] = arr[i] 

    
    arr[pos-1] = elem
    return arr
 
def DeleteElement(item,arr):
    size = len(arr)
    
    pos = FindElement(arr,item) 
    if pos == -1:
        return -1
    
    for i in range(pos,size-1):
        arr[i] =  arr[i+1]
    
    return 1 


#endregion
#region Sorted methods
#------->Binary Search -> Keep splitting into 2 and reach the correct mid element
#Time Complexity -> O(log n) -> n/2 -> log of base 2 divided n to reach 1 element
def FindElementSorted(arr, item , low, high):
    if high < low: # no more elements to search
        return -1
    mid = int(( high + low ) / 2  )
    print("mid index is " , mid)
    if arr[mid] == item:
        return mid-1 #Found at position index-1
    if item > arr[mid]:
        return FindElementSorted(arr,item,mid+1,high)
    
    if item < arr[mid]: 
        return FindElementSorted(arr,item,low,mid-1) 
    
    return -1
    
#endregion
#region General Problems
#Linear time -> 2 pointer apprach
def ReverseArray(arr):
    size = int(len(arr))
    start = 0
    end = size -1  
    while start < end :
        
         temp = arr[start]
         arr[start] = arr[end]
         arr[end] = temp
         start+=1
         end-=1
        
    print("Reversed Array is " , arr)      

global_list = [] 

#differnet between return recusive and normal call recursive
def ElementLeaders(arr,pos=0):
    size = len(arr)-1 
    if(pos > size):
        return
    max = arr[pos]  # default 0 element
    for index in range(pos, size):
        
        if max < arr[index+1] or index+1 > size:
            return ElementLeaders(arr,index+1)
    
    global_list.append(max)
    return ElementLeaders(arr,pos+1)        

def ElementLeadersAlternate(arr):
    size = len(arr)
    for i in range(size):
        for j in range (i+1, size):
            if arr[i]<arr[j]:
                break
        global_list.append(arr[i])    

#element whose freuquency is > n/2
def MajorityElement():
    pass

#Time -> O(n^2)
def OddOccurence(arr):
    size  = len(arr)
    
    for index in range( 0 , size):
        count = 0
        for jIndex in range(size):
            if(arr[index] == arr[jIndex]):
                count+=1
        if(count % 2 != 0):#Odd
            print("oddly occuring number is " , arr[index])
            return  


#Kadane Algorithm -> Interesting
# for positive sum
def SubArraySum(arr):
    size = len(arr)
    Fmax  = -1e8
    maxHere = 0
    startElement = 0
    endElement = 0
    s= 0
    
    for x in range(size):
        if(x+1 == size):
            break
        
        maxHere += arr[x]
        
        if maxHere > Fmax:
            Fmax = maxHere
            startElement= s
            endElement= x
        
        
        #Interesting part
        if maxHere < 0:
            maxHere = 0
            s+=1
            
                 
    print(f"Array is {startElement} and {endElement}")
    return Fmax       
                
            
           

def PairSum(arr ,sumX):
    size  = len(arr)
    flag  = False
    for index in range(size):
        for jindex in range(index+1, size):
            if(arr[index]+arr[jindex] == sumX):
                print(f"Found Sum, pairs are  {arr[index]} and { arr[jindex]}")
                flag = True
              #  return
    if flag is True:
        return
    print("No sum pair found")
#endregion
if __name__ == '__main__':
  #  l = [16, 17, 4, 3, 5, 2] 
    l =  [-2, -3, 4, -1, -2, 1, 5, -3]
    lsorted =  []

   # item =input("enter a number to delete->   ")
   # ReverseArray(l)
   # ElementLeaders(l)
   # PairSum(l,-2)
   # OddOccurence(l)
    max =  SubArraySum(l)
    print("MAX IS " , max)
   

 




