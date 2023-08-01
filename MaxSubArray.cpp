//最大子数组
#include <iostream>
int Find_Max_Crossing_Subarray(int A[], int low, int mid, int high){
    int left_sum = A[mid];
    int sum = 0;
    int max_left = mid;
    for(int i = mid; i >= low; i--){
        sum += A[i];
        if(sum >= left_sum){
            left_sum = sum;
            max_left = i;
        }
    }
    int right_sum = A[mid+1];
    int sum_right = 0;
    int max_right = mid+1;
    for(int j = mid+1; j < high; j++){
        sum_right += A[j];
        if(sum_right >= right_sum){
            right_sum = sum_right;
            max_right = j;
        }
    }
    return max_left, max_right, left_sum+right_sum;
}


int Find_Max_Subarray(int A[], int low, int high){
    if(low == high){
        return(low, high, A[low]);
    }
    else{
        int mid = (low + high) / 2;
        int left_low, left_high, left_sum = Find_Max_Subarray(A, low, mid);
        int right_low, right_high, right_sum = Find_Max_Subarray(A, mid+1, high);
        int cross_low, cross_high, cross_sum = Find_Max_Crossing_Subarray(A, low, mid, high);
        if(cross_sum >= right_sum && cross_sum >= left_sum){
            return cross_low, cross_high, cross_sum;
        }
        else if(right_sum >= cross_high && right_sum >= left_sum){
            return right_low, right_high, right_sum;
        }
        else{
            return left_low, left_high, left_sum;
        }
    }
}


int main(){
    int A[] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    std::cout << Find_Max_Subarray(A, 0, 15) << std::endl;
    int B[] = {1, -4, 3, -4};
    std::cout << Find_Max_Subarray(B, 0, 3) << std::endl;
    return 0;
}