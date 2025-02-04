# Example dictionary
grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# Using enumerate to loop through the dictionary
for index, (key, value) in enumerate(grades.items()):
    print(f"{index}: {key} has a grade of {value}")