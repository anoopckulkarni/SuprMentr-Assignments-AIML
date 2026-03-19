name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior"

print("\n--- Personalized Message ---")
print("Hi " + name + "!")
print("You are", age, "years old, which makes you", category + ".")
print("It's awesome that you enjoy", hobby + "!")
print("Have a good rest of the day")