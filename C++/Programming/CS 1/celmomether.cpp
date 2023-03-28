#include <stdio.h>
#include <algorithm>
#include "temps.h"
#include <iostream>

using namespace std;

void print_stars(int number){
	// Printing stars, getting on input only one arg
	for (int i = 0; i < abs(number); i++)
	{
		cout<<"*";
	}
}

void print_spaces(int num_spaces){
	// Printing spaces, getting on input only one arg
	for (int i = 0; i < abs(num_spaces); i++)
	{
		cout << " ";
	}
}

int determine_min_temrepature(const int arr[], int  ArrayLength){
  	// Finding min value to evaluate number of tabs
  	int min_temperature = 0;
  	for (int i = 0; i < ArrayLength; i++)
	{
   		if (arr[i] != no_value) {
			min_temperature = min(min_temperature, arr[i]);
   		}
  	}
	return min_temperature;
}

int main(int argc, char **argv)
{
	int ArrayLength = sizeof(temperatures) / sizeof(int);
	int min_temperature = determine_min_temrepature(temperatures, ArrayLength);
	int curr_state = 0;

	for (int i = 0; i < ArrayLength; i++)
	{
		
		if (temperatures[i] != no_value) curr_state = temperatures[i];

		print_spaces(max(min_temperature, (min_temperature - curr_state)));
		print_stars(min(curr_state, 0));
		cout << "|";
		print_stars(max(curr_state, 0));

		cout << endl;
	}

	return 0;
}