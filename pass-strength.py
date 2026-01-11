import re
import getpass

def password_strength(password):
    # Initialize score and feedback list base on length, uppercase, lowercase, digits, special characters
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("weak: password must be at least 8 characters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("weak: password must contain digits")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("weak: password must contain upper characters")
    
    if any(char.islower() for char in password):
        score += 1
    else: 
        feedback.append("weak: password must contain lower characters")

    if re.search(r'[!@#$%^&*()_+{}\'":\';.<>/]', password):
        score += 1
    else:
        feedback.append("weak: password must contain a special character")
#check strength level based on score:
    if score == 5:
        strength = "VERY STRONG"
    elif score == 4:
        strength = "STRONG"
    elif score == 3:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return strength, feedback
        


def password_checker():
    print("^-_-^ welcome to password strength checker ^-_-^")

    while True:
        password = getpass.getpass("enter your password to check: (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("thank you for using password strength checker")
            break

        strength, feedback =password_strength(password)

        print(f"\nYour password strength is: {strength}")
        if feedback:
            print("Suggestions to improve:")
        for item in feedback:
            print(item)
        print("-_-" * 40)

if __name__ == "__main__":
    password_checker()