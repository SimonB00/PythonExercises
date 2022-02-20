#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <cstdlib>

std::vector<char> gen_password(int length) {
    std::vector<char> symbols = {'~','`','!','@','#','$','%','^','&','*','(',')',
    '_','-','+','=','{','[','}',']','|','/',':',';','"','<',',','>','.','?'};
    std::vector<char> letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z'};
    std::vector<char> Letters = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    std::vector<char> password = {};

    for(int i = 0; i < length; ++i) {
        int randNum = rand()%4 + 1;
        
        if(randNum == 1) {
            int s = rand()%29;
            password.push_back(symbols[s]);
        } else if(randNum == 2) {
            int l = rand()%26;
            password.push_back(letters[l]);
        } else if(randNum == 3) {
            int L = rand()%26;
            password.push_back(Letters[L]);
        } else if(randNum == 4) {
            int n = rand()%10;
            password.push_back(n);
        }
    }  

    return password; 
}

int main() {
    std::cout << "How long should your password be?" << '\n';
    int length;
    std::cin >> length;
    auto it = gen_password(length).begin();
    auto last = gen_password(length).end();
    
    for(; it != last; ++it) {
        std::cout << *it;
    }
    std::cout << '\n';
}