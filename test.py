try:
   score1 = float(input("Enter first test score: "))
   score2 = float(input("Enter second test score: "))
   score3 = float(input("Enter third test score: "))

if score1 < 0 or score2 < 0 or score3 < 0:
    print("Error: Score must be between 0 and 100. PLEASE TRY AGAIN.")
    elif score1 > 100 or score2 > 100 or score3 > 100:
        print("Error: Score must be between 0 and 100. PLEASE TRY AGAIN.")
    else:
        average = (score1 + score2 + score3) / 3
print("\n----RESULTS----")
print(f"Test Score 1: {score1}")
print(f"Test Score 2: {score2}")
print(f"Test Score 3: {score3}")
print(f"Average Score: {average:.2f}")
            except ValueError:
                print("Error: Invalid input. Please ente a numeric value.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
