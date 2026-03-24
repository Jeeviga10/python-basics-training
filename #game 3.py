score = 0

answer = input("Capital of India? ")
if answer.lower() == "delhi":
    score += 1

answer = input("2 + 2 = ? ")
if answer == "4":
    score += 1

print("Your score:", score)
