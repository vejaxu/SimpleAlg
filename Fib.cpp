#include <iostream>
int fib(int n){
    if(n < 1){
        return -1;
    }
    if(n == 1 || n == 2){
        return 1;
    }
    else{
        int s1 = 1;
        int s2 = 1;
        for(int i = 3; i <= n; i ++){
            s2 = s1 + s2;
            s1 = s2 - s1;
        }
        return s2;
    }
}


int main(){
    int n;
    std::cin >> n;
    std::cout << fib(n) << std::endl;
}