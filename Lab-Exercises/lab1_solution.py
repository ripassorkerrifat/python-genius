name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_developer = input("Are you a developer? (yes/no): ").strip().lower() == "yes"

if age < 18:
    tier = "Tier 3: Guest"
elif is_developer:
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Access"

print(f"Final Profile Summary: {name}, you have been assigned to {tier}.")
