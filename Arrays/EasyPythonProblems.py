def FindThreeLargestNumbers(arr):
    size = len(arr)
    largestCount = 3
    count = 0
    maxStored = -9999999999
    for index in range(size-1):
        if(arr[index] > arr[index+1]):
            temp = arr[index+1]
            arr[index+1] = arr[index]
            arr[index]= temp
               

  
    for index in range(size-1 ,0 ,-1 ):
        if(count == largestCount):
            break
    
        if(maxStored != arr[index]):
            count+=1
            maxStored = arr[index]
            print(arr[index])
            
      
   
arr = [10, 4, 3, 50,23 , 23,50, 90, 90]
FindThreeLargestNumbers(arr)   
    