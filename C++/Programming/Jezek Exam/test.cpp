#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;


int main(int argc, char **argv)
{

double a = 3987;
double b = 4365;
double c = 4472;
double r1 = pow(a, 12) + pow(b, 12);
double r2 = pow(c, 12);
bool ans = r1 == r2;
if (ans == true){
cout << "Equals";
}
else{
    cout << "Dont";
}

return 0;

}