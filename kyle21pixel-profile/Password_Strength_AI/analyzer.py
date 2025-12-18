
import re
import math

def calculate_entropy(password):
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32
    
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

def check_strength(password):
    entropy = calculate_entropy(password)
    print(f"[*] Password: {password}")
    print(f"[*] Entropy: {entropy:.2f} bits")
    
    if entropy < 28:
        return "Very Weak 🔴"
    elif entropy < 36:
        return "Weak 🟠"
    elif entropy < 60:
        return "Reasonable 🟡"
    elif entropy < 128:
        return "Strong 🟢"
    else:
        return "Very Strong 🔵"

def main():
    print("--- AI Password Strength Analyzer ---")
    passwords = ["123456", "password", "MyDogName", "Correct-Horse-Battery-Staple", "Tr0ub4dor&3"]
    
    for p in passwords:
        strength = check_strength(p)
        print(f"[>] Verdict: {strength}\n")

if __name__ == "__main__":
    main()
