#include<iostream>
#include<vector>
using namespace std;

void countSort(vector<float>& arr)
{
    int n=arr.size();

    int maxVal=arr[0];

    for(int i=1;i<n;i++) maxVal=max(maxVal,(int)arr[i]);  //finding max value

    vector<int> countArr(maxVal+1,0);       //creating count array

    for(int i=0;i<n;i++) countArr[(int)arr[i]]++;       //storing frequency

    for(int i=1;i<=maxVal;i++) countArr[i]+=countArr[i-1];   //prefix sum

    vector<int> outputArr(n);

    for(int i=n-1;i>=0;i--)   //traversing from end comparing with count array index and placing in output array with -1 index and decrementing count array value by 1
    {
        outputArr[countArr[(int)arr[i]]-1]=(int)arr[i];
        countArr[(int)arr[i]]--;
    }

    for(int i=0;i<n;i++) arr[i]=(float)outputArr[i];  //copying to original array

}
int main()

{
    vector<float> arr = {64, 25, 12, 22, 11,23};
    countSort(arr);
    cout << "Sorted array: \n";
    for(float num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}