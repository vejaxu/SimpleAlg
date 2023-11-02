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