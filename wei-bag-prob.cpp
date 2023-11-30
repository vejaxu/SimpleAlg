#include <iostream>
using namespace std;
#include <vector>


void wei_bag_prob(){
    vector<int> weight = {1, 3, 4};
    vector<int> value = {15, 20, 30};
    int bagWeight = 4;

    vector<vector<int>> dp(weight.size() + 1, vector<int>(bagWeight + 1, 0));
    for(int j = bagWeight; j >= weight[0]; j --){
        dp[0][j] = dp[0][j- weight[0]] + value[0];
    }

    for(int i = 1; i < weight.size(); i ++){ //物品
        for(int j = 0; j <= bagWeight; j ++){ //背包容量
            if(j < weight[i]){ //超重，肯定不取
                dp[i][j] = dp[i-1][j];
            }
            else{ //否则，则需要比较取与不取哪个价值更大
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
            }
        }
    }
    cout << dp[weight.size() - 1][bagWeight] << endl;
}


int main(){
    wei_bag_prob();
}

/* #include <iostream>
#include <vector>

using namespace std;

int main(){
    int M, bagsize;
    cin >> M >> bagsize;
    
    vector<int> weight(M, 0);
    for(int i = 0; i < M; i ++){
        cin >> weight[i];
    }
    
    vector<int> value(M, 0);
    for(int i = 0; i < M; i ++){
        cin >> value[i];
    }
    
    vector<vector<int>> dp(M, vector<int> (bagsize + 1, 0));
    
    //初始化背包容量不断增加
    for(int j = weight[0]; j <= bagsize; j ++){
        dp[0][j] = value[0];
    }
    
    //背包容量为0
    for(int i = 0; i < M; i ++){
        dp[i][0] = 0;
    }
    
    for(int i = 1; i < M; i ++){ //第一行我们已经初始化好了
        for(int j = 0; j <= bagsize; j ++){
            if(j < weight[i]){
                dp[i][j] = dp[i-1][j];
            }else{
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
            }
        }
    }
    
    cout << dp[M-1][bagsize];
    return 0;
} */