#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>

std::string piglatin(std::string input){
	char arr[6]={'a', 'e', 'i', 'o', 'u', 'y'};
	std::string value, temp;
	
	if (std::find(std::begin(arr), std::end(arr), input.at(0)) != std::end(arr))
	{
		value = input+"yay";
	}
	else{
		int i = 0;
		while (!(std::find(std::begin(arr), std::end(arr), input.at(i)) != std::end(arr))){
			temp += input.at(i);
			i++;
		}
		input.erase(input.begin(), input.begin()+i);
		value = input.append(temp)+"ay";
	}

	return value;
}
int main(){	
	std::string input, word;
	std::vector<std::string> sentence;
	
	
	while(getline(std::cin,input)){
		
		if(!input.empty()){
			std::stringstream stream(input);
			std::string whole;
			while(!stream.eof()){
				stream >> word;
				whole += piglatin(word)+" ";
			}
			sentence.push_back(whole);	
		}
		else
			break;		
	}
	for(int i = 0; i <sentence.size();i++){
		std::cout<<sentence[i]<<"\n";
	}
	return 0;
}

