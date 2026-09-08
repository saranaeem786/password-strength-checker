import re
import hashlib
import requests

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. ! @ # $)")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


def check_breach(password):
    # Hash the password using SHA-1 (required by the HaveIBeenPwned API)
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Query the API using only the first 5 characters (privacy-safe — full password/hash is never sent)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Could not check breach status (API error)"

    hashes = (line.split(":") for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return f"FOUND in {count} known data breaches!"

    return "Not found in known breaches"


# --- Test it ---
if __name__ == "__main__":
    test_passwords = ["password123", "P@ssw0rd!2024", "123456"]

    for pw in test_passwords:
        print(f"--- Checking: {pw} ---")
        strength, feedback = check_strength(pw)
        print("Strength:", strength)
        if feedback:
            print("Suggestions:")
            for f in feedback:
                print("-", f)

        breach_result = check_breach(pw)
        print("Breach check:", breach_result)
        print()