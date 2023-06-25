# Movie Sorting

The solution provides two functions, `sort_by_year` and `sort_by_title`, to sort a list of movie objects based on their year and title, respectively.

## Function: `sort_by_year(arr)`

This function sorts the list of movie objects based on their year in ascending order.

### Parameters

- `arr`: A list of movie objects. Each movie object should have the following properties:
    - `title`: The title of the movie (string).
    - `year`: The release year of the movie (integer).
    - `genres`: A list of genres associated with the movie (list of strings).

### Returns

The function returns a new list of movie objects sorted by their year in ascending order.

## Function: `sort_by_title(arr)`

This function sorts the list of movie objects based on their title, ignoring any leading "A"s, "An"s, or "The"s.

### Parameters

- `arr`: A list of movie objects. Each movie object should have the following properties:
    - `title`: The title of the movie (string).
    - `year`: The release year of the movie (integer).
    - `genres`: A list of genres associated with the movie (list of strings).

### Returns

The function returns a new list of movie objects sorted by their title, ignoring any leading "A"s, "An"s, or "The"s.
