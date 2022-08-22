/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    char ch;
    std::cin >> ch;
    if ((65<=ch)&&(ch<=90)){
        std::cout <<ch<<" "<< "is Upper case letter" << std::endl;
    }
    else if((97<=ch)&&(ch<=122)){
        std::cout <<ch<<" "<< "is Lower case letter" << std::endl;
    }
    else if ((48<=ch)&&(ch<=57)){
        std::cout <<ch<<" "<< "is Numeric" << std::endl;
    }
}

