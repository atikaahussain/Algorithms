# TC -> o(n^2)
def bubbleSort(arr):    
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# TC -> o(n^2)
def insertionsort(arr): 
    n=len(arr)
    
    for i in range(1,n):
        
        key =arr[i]
        j=i-1
        
        while j>=0 and arr[j]>arr[i]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
 
#TC -> O(n^2)       
def SelectionSort(arr):
    
    n=len(arr)
    for i in range(n):  
        minindex=i
        
        for j in range (i+1,n):
            if arr[j]<minindex:
                minindex=j
        
        arr[i],arr[minindex]=arr[minindex],arr[i]
       
# TC -> O(n log n) SC -> O(n)
def merge(arr,left,right,mid):
    n1=mid-left+1
    n2=right-mid
    L=[]
    R=[]
    for i in range(n1):
        L.append(arr[left+i])
        
    for i in range(n2):
        R.append(arr[mid+1+i])
    
    i,j,k=0,0,left
    
    while i<n1 and j<n2:
        
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
      
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
           
def mergesort(arr,left,right):
    if left>=right:
        return
    
    mid=(right+left)//2
    mergesort(arr,left,mid)
    mergesort(arr,mid+1,right)
    
    merge(arr,left,right,mid)

# Time Complexity: O(N+M) SC-> O(N+M)
def countsort(arr):
    n=len(arr)
    maxval=max(arr)
    
    countarr= [0]*(maxval+1)
    
    for v in range(n):
        countarr[arr[v]]+=1
    
    for i in range(1,maxval+1):
        countarr[i]+=countarr[i-1]
    
    outputarr=[0]*n
    
    for i in range(n-1,-1,-1):
        outputarr[countarr[arr[i]]-1]=arr[i]
        countarr[arr[i]]-=1
    
    for i in range(n):
        arr[i]=outputarr[i]

def countingsortforradix(arr,exp):
    countarr= [0]*10
    for v in range(0,n):
        countarr[(arr[v]//exp)%10]+=1
    for i in range(1,10):
        countarr[i]+=countarr[i-1]
    outputarr=[0]*n
    for i in range(n-1,-1,-1):
        outputarr[countarr[(arr[i]//exp)%10]-1]=arr[i]
        countarr[(arr[i]//exp)%10]-=1
    for i in range(n):
        arr[i]=outputarr[i]
    
def radixsort(arr):
    
    maxval=max(arr)
    exp=1
    while maxval//exp>=1:
        countingsortforradix(arr,exp)
        exp*=10

def partitionFunc(arr,low,high):
    pivot=arr[high]
    
    i=low-1
    
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
def quicksort(arr,low,high):
    if low<high:
        partindex=partitionFunc(arr,low,high)
        quicksort(arr,low,partindex-1)
        quicksort(arr,partindex+1,high)

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    n=len(arr)
    # bubbleSort(arr)
    # insertionsort(arr)
    # SelectionSort(arr)
    # mergesort(arr,0,n-1)
    # countsort(arr)
    # radixsort(arr)
    # quicksort(arr,0,n-1)
    
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")