#include "temps.h"
#include <cstdlib>
#include <iostream>
using namespace std;



void print_stars(int n) {  //from the classwork
  for (int i = 0; i < abs(n); i++) {
    cout << "*";
  }
}

void print_spaces(int a, int b) {  //same to printing of stars, but prints needed amount of spaces 
  int qos = abs(a) - abs(b);    //qos stands for "quantity of spaces"
  for (int i = 0; i < qos; i++)
  {
    cout << " ";
  }

}


void print_line() {    //cause now it looks nicer)
  cout << "|";
}


int Extremum_points_min(int a) {  //finds minimal value of an array and returns it
  int min_t = 0;
  for (int i = 0; i < a; i++) {
    if (temperatures[i] != no_value) {
      min_t = min(min_t, temperatures[i]);
    }
  }
  return min_t;
}

void Cases_with_no_value(int tmp, int a) {
  if (tmp > 0) {
    print_spaces(a, 0);
    print_line();
    print_stars(tmp);
    cout << endl;
  }
  else {
    print_spaces(a, tmp);
    print_stars(tmp);
    print_line();
    cout << endl;
  }
}

void Print_everything(int a, int c) {

  int tmp = 0;    //temporary container

  for (int i = 0; i < c; i++)    //iterating through array
  {
    if (temperatures[i] != no_value) {
      if (temperatures[i] > 0) {
        tmp = temperatures[i];
        print_spaces(a, 0);
        print_line();
        print_stars(temperatures[i]);
        cout << endl;
      }
      else {
        tmp = temperatures[i];
        print_spaces(a, tmp);
        print_stars(temperatures[i]);
        print_line();
        cout << endl;
      }

    }
    else {
      Cases_with_no_value(tmp, a);
    }
  }
}





int main()
{
  int Len = sizeof(temperatures) / sizeof(temperatures[0]);
  int temp1 = Extremum_points_min(Len);
  Print_everything(temp1, Len);
  return 0;
}