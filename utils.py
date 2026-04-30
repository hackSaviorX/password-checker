import string

def check_length(password):
    return len(password) >= 8

def has_upper(password):
    return any(c.isupper() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_symbol(password):
    return any(c in string.punctuation for c in password)

def is_common(password, common_list):
    return password.lower() in common_list


def calculate_strength(password, common_list):
    score = 0

    if check_length(password):
        score += 1
    if has_upper(password):
        score += 1
    if has_lower(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_symbol(password):
        score += 1
    if not is_common(password, common_list):
        score += 1

    return score
