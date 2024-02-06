#include <iostream>
using namespace std;

// g++ -o input.out inputExample.cpp; ./input.out
int main() {
    int x, y , z;
    int sum=0;
    double avg=0.0;
    int prd=0;
    cout << "Enter first input ";
    cin >> x;

    cout << "Enter second input";
    cin >> y;

    cout << "Enter third input";
    cin >> z;
    
    sum = x+y+z;
    avg = sum/3.0;
    prd = x* y*z;

    cout << "The sum is: " << sum;
    cout << "\nThe average is:  " << avg;
    cout << "\nThe product is:  " << prd;


    return 0;
}