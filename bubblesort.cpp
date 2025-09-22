#include<iostream>
#include<vector>
using namespace std;

void bubbleSort(vector<float>& arr)
{
    int n=arr.size();
    bool swapped;
    do{
        swapped=false; 
        for(int i=0;i<n-1;i++)
        {
            if(arr[i]>arr[i+1])  // if the current is greater than the next then swap
                                // this will push the largest element to the end in each iteration
            {
                swap(arr[i],arr[i+1]);
                swapped=true;
            }
        }
    }while(swapped); 
}

int main(){

vector<float> arr = {64.5, 25.1, 12.3, 22.4, 11.0};
cout<<"Unsorted array: \n";
for(float num : arr)
    cout << num << " ";
cout << endl;
bubbleSort(arr);
cout << "Sorted array: \n";
for(float num : arr)
    cout << num << " ";
cout << endl;
return 0;

}