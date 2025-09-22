#include<iostream>
#include<vector>
using namespace std;

void merge(vector<float>& arr, int left, int mid, int right){


    int n1=mid-left+1;
    int n2=right-mid;

    //create temp arrays for each half
    vector<float> L(n1);
    vector<float> R(n2);

    //storing data in em
    for(int i=0;i<n1;i++)
        L[i]=arr[left+i];
    for(int j=0;j<n2;j++)
        R[j]=arr[mid+1+j];

    int i=0,j=0;
    int k=left;

    while(i<n1 && j<n2)
    {
        //swapping swapping conditionssss
        if(L[i]<=R[j])
        {
            arr[k]=L[i];
            i++;
        }
        else
        {
            arr[k]=R[j];
            j++;
        }
        k++;
    }

    // remaining elements
    while(i<n1)
    {
        arr[k]=L[i];
        i++;
        k++;
    }

    while(j<n2)
    {
        arr[k]=R[j];
        j++;
        k++;
    }
}


void mergeSort(vector<float>& arr,int left,int right)
{
    if(left>=right) return; //base case

    int mid=left+(right-left)/2;

    mergeSort(arr,left,mid); //left half
    mergeSort(arr,mid+1,right); //right half

    //merge the two halves
    merge(arr,left,mid,right);

}

int main(){

vector<float> arr = {64.5, 25.1, 12.3, 22.4, 11.0};
int n=arr.size();

mergeSort(arr,0,n-1);

cout << "Sorted array: \n";
for(float num : arr)
    cout << num << " ";
cout << endl;

return 0;

}