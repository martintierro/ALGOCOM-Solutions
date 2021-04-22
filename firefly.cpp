#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(){
    int cave_length, cave_height;
    cin >> cave_length >> cave_height;
    vector<int> sum_top(cave_height, 0); 
    vector<int> sum_bottom(cave_height, 0);

    for(int i = 0; i<cave_length; i++){
        int temp;
        cin >> temp;
        if (i % 2 == 0){
            sum_top[temp-1] ++;
        }
        else{
            sum_bottom[cave_height-temp]
        }
    }
}