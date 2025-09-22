#include<iostream>
#include<vector>
using namespace std;

void selectionSort(vector<float>& arr)
{
    int n=arr.size();
    for(int i=0;i<n-1;i++)
    {
        int minIndex=i;
        // loop to find the index of the minimum element
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[minIndex])
            {
                minIndex=j;
            }
        }
        // then swap the found minimum element with the first element
        swap(arr[i],arr[minIndex]);
    }
}
int main()

{
    vector<float> arr = {64.5, 25.1, 12.3, 22.4, 11.0};
    selectionSort(arr);
    cout << "Sorted array: \n";
    for(float num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}