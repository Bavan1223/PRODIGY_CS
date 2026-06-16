def check_password_strength(password):

    score = 0

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:

        if char.islower():
            has_lower = True

        elif char.isupper():
            has_upper = True

        elif char.isdigit():
            has_digit = True

        else:
            has_special = True

    if len(password) >= 8:
        score += 1

    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if score <= 2:
        strength = "Weak"

    elif score == 3:
        strength = "Medium"

    elif score == 4:
        strength = "Strong"

    else:
        strength = "Very Strong"

    print("\nPassword Analysis")
    print("-----------------")
    print("Length:", len(password))
    print("Contains Lowercase:", has_lower)
    print("Contains Uppercase:", has_upper)
    print("Contains Numbers:", has_digit)
    print("Contains Special Characters:", has_special)
    print("Strength:", strength)


password = input("Enter password: ")
check_password_strength(password)