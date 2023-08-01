//扑克牌排序
#include <iostream>
void Insertion_sort(int A[], int n){
    for(int i = 1; i < n; i++){
        int key = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] > key){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = key;
    }
}


void Insertion_sort_reverse(int A[], int n){
    for(int i = 1; i < n; i++){
        int key = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] < key){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = key;
    }
}


int main(){
    int A[] = {2, 5, 4, 1, 3, 9, 8, 7, 6};
    Insertion_sort(A, 9);
    for(int i = 0; i < 9; i++){
        std::cout << A[i] << ' ';
    }
    std::cout << std::endl;
    
    Insertion_sort_reverse(A, 9);
    for(int i = 0; i < 9; i++){
        std::cout << A[i] << ' ';
    }
    std::cout << std::endl;
    return 1;
}