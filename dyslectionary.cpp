#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void process(vector<string>&words){
    int maxlength = 0;
    for(auto word : words){
        if(word.length()>maxlength){
            maxlength = word.length();
        }
    }

    for(auto& word: words){
        reverse(word.begin(),word.end());
    }
    sort(words.begin(), words.end());
    for(auto& word: words){
        reverse(word.begin(),word.end());
    }

    for(auto& word : words){
        string temp;
        temp.resize(maxlength - word.length(),' ');
        temp += word;
        swap(word, temp);
        cout << word << endl;
    }
}


int main(){
    std::string word;
    std::vector<string> words;
    while(std::getline (std::cin, word)){
        if(word == ""){
            process(words);

            cout << endl;
            words.clear();
            continue;
        }

        words.push_back(word);
    }
    process(words);
}
