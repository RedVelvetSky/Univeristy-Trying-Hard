	int num_spaces = abs(min_temperature);
		int left_stars = max(curr_state, 0);
		int right_stars = max(-curr_state, 0);
		int num_right_spaces = max(num_spaces - left_stars - right_stars - 1, 0);

		print_spaces(num_spaces);
		print_stars(left_stars);
		cout << "|";
		print_stars(right_stars);
		print_spaces(num_right_spaces);