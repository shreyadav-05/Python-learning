# Age Group Categorization
# Classify a person's age group: Child (<13), Teenager (13-19) Adult (20-59), Senior (60+).

age = int(input("enter the person age:"))
if age <= 12:
    print("the person is a child")
elif age <= 19:
    print("the person is a teenager")
elif age <= 59:
    print("the person is a adult")
else:
    print("the person is a senior")

