def get_mark(student):
    while True:
        try:
            mark = float(input(f"Enter marks for {student}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Score must be between 0 and 100. PLEASE TRY AGAIN.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

Student1 = get_mark("Student 1")
Student2 = get_mark("Student 2")
Student3 = get_mark("Student 3")
average = (Student1 + Student2 + Student3) / 3
print("\n----RESULTS----")
print(f"Student 1: {Student1}")
print(f"Student 2: {Student2}")
print(f"Student 3: {Student3}")
print(f"Average Score: {average:.2f}")