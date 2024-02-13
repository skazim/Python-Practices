#include <iostream>
using namespace std;
string thermostat(int temp, int low, int high){

    string state = "";
    if (temp < low){
        state = "Turn on heater";
    }
    else if(temp > high){
        state = "Turn on cooler";
    }
    else{
        state = "Do nothing";
    }
    return state;
}
int main() {
    string state = "";
    state = thermostat(25,20,27);
    cout << "" << state;
    return 0;
}