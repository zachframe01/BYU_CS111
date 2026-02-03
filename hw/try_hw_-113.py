def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)

check_age(-1)