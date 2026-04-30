from utils import calculate_strength

def load_common_passwords():
    with open("common_passwords.txt", "r") as file:
        return set(line.strip() for line in file)

def rate_password(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def main():
    common_passwords = load_common_passwords()
    
    password = input("Enter a password: ")
    score = calculate_strength(password, common_passwords)
    
    print(f"Password strength: {rate_password(score)} (Score: {score}/6)")

if __name__ == "__main__":
    main()
