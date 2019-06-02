#include <vector>
#include <iostream>
using namespace std;
int number=0;

class Solution {
public:
    int Pairs(vector<int>& nums) {
        int n=nums.size(),i=0;
        int arr[n+1];
        for(vector<int>::iterator itr=nums.begin();itr!=nums.end();++itr){
            arr[i++]=*itr;
        }
        divide_merge(arr,0,n-1);
        return number;
    }
    void pair_counting(int array[],int low,int mid,int high){
        int i=low,j=mid;
        while(i<=mid){
            while(j<=high){
                if(array[i]>2*array[j])  ++number;
                ++j;
            }
            ++i;
            j=mid;
        }
    }
    void divide_merge(int array[],int low,int high){
        int mid;
        if(low>=high) return;
        mid=(high+low)/2;
        divide_merge(array,low,mid);
        divide_merge(array,mid+1,high);
        pair_counting(array,low,mid,high);
    }
};