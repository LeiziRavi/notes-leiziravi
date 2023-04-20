def alphabetize(original_list = []):
    """Pass any list in square brackets, displays a string with items sorted"""
    # Inside the function make a working copy of the list passed in.
    sorted_list = original_list.copy()
    # Sort the working copy.
    sorted_list.sort()
    # Make a new empty string for output 
    final_list = ''
    # Loop through sorted list and append name and comma and space.
    for name in sorted_list:
        final_list += name + ', '
    # Knock of last comma space if final list is long enough 
    final_list = final_list[:-2]
    # return the alphabetized list.
    return final_list

random_list = ['McMullen','Keaser','Maier','Wilson','Yudt','Gallagher','Jacobs']
alpha_list = alphabetize(random_list)
print(alpha_list)