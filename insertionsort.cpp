#include<iostream>
#include<vector>
using namespace std;

void insertionSort(vector<float>& arr)
{
    int n=arr.size();
    
    for(int i=1;i<n;i++)
    {
        float key=arr[i];
        int j=i-1; //j is the index behind the current index i

        // if the behind inedx is greater than the current one then swap
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key; //place the key at its correct position
    }
}

int main(){

vector<float> arr = {64.5, 25.1, 12.3, 22.4, 11.0};
cout<<"Unsorted array: \n";
for(float num : arr)
    cout << num << " ";
cout << endl;
insertionSort(arr);
cout << "Sorted array: \n";
for(float num : arr)
    cout << num << " ";
cout << endl;
return 0;

}