#include<iostream>
#include<vector>
using namespace std;

int partition(vector<float>& arr, int low, int high)
{
    int pivot=arr[high]; 
    int i=low-1; //index before the low

    for(int j=low;j<high;j++)
    {
        if(arr[j]<pivot)    //if current < pivot
        {
            i++;            //inc index of smaller element
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return i+1;            // partitioning index
}
    

void quickSort(vector<float>& arr,int low,int high)
{
    int partIindex;
    if(low<high){
        partIindex=partition(arr,low,high); //partitioning index
        quickSort(arr,low,partIindex-1); //left half
        quickSort(arr,partIindex+1,high); //right half
    }
}
int main()

{
    vector<float> arr = {64.5, 25.1, 12.3, 22.4, 11.0};
    quickSort(arr,0,arr.size()-1);
    cout << "Sorted array: \n";
    for(float num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}