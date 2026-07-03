# Password-strength-checker
IT IS MY FIRST PROJECT OF  MY INTERNSHIP. PASSWORD STRENGTH CHECKER
# Password Strength Checker
# Project 1

def check_password_strength(password):
    """
    Ye function password ki strength check karta hai
    aur result return karta hai
    """
    
    # Initialize variables
    length = len(password)
    has_number = False
    has_symbol = False
    has_uppercase = False
    
    # Special characters ki list
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    
    # Password ke har character ko check karo
    for char in password:
        # Check for numbers (0-9)
        if char.isdigit():
            has_number = True
        
        # Check for uppercase letters (A-Z)
        if char.isupper():
            has_uppercase = True
        
        # Check for symbols
        if char in symbols:
            has_symbol = True
    
    # Kitne features hain count karo
    features_count = 0
    if has_number:
        features_count += 1
    if has_symbol:
        features_count += 1
    if has_uppercase:
        features_count += 1
    
    # Strength determine karo
    if length >= 8 and features_count >= 3:
        strength = "Strong 💪"
        message = "Bohat mazboot password!"
    elif length >= 6 and features_count >= 2:
        strength = "Medium 👍"
        message = "Acha password hai, mazeed improve kar sakte hain"
    else:
        strength = "Weak ⚠️"
        message = "Kamzor password! Length aur complexity badhayein"
    
    # Detailed feedback
    feedback = {
        "strength": strength,
        "message": message,
        "length": length,
        "has_number": has_number,
        "has_symbol": has_symbol,
        "has_uppercase": has_uppercase,
        "features_count": features_count
    }
    
    return feedback

def display_result(result):
    """
    Result ko khoobsurat tareeqe se display karta hai
    """
    print("\n" + "="*50)
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("="*50)
    print(f"📝 Password Length: {result['length']}")
    print(f"🔢 Numbers: {'✅ Yes' if result['has_number'] else '❌ No'}")
    print(f"🔣 Symbols: {'✅ Yes' if result['has_symbol'] else '❌ No'}")
    print(f"🔠 Uppercase: {'✅ Yes' if result['has_uppercase'] else '❌ No'}")
    print(f"📊 Features Count: {result['features_count']}/3")
    print("-"*50)
    print(f"⭐ Strength: {result['strength']}")
    print(f"💬 {result['message']}")
    print("="*50 + "\n")

# Main program
def main():
    print("="*50)
    print("👋 Welcome to Password Strength Checker")
    print("="*50)
    print("\nPassword mein ye features hone chahiye:")
    print("✅ Minimum 8 characters")
    print("✅ At least one number (0-9)")
    print("✅ At least one symbol (!@#$%^&* etc.)")
    print("✅ At least one uppercase letter (A-Z)")
    print("\n" + "-"*50)
    
    while True:
        # User se password lena
        password = input("\n🔑 Enter password (or 'quit' to exit): ")
        
        # Exit condition
        if password.lower() == 'quit':
            print("\n👋 Goodbye! Stay safe! 🛡️")
            break
        
        # Password check karna
        if len(password) == 0:
            print("❌ Password empty nahi ho sakta! Please try again.")
            continue
        
        result = check_password_strength(password)
        display_result(result)
        
        # Improvement suggestions
        if result['strength'] != "Strong 💪":
            print("💡 Improvement Tips:")
            if result['length'] < 8:
                print(f"   - Length {result['length']}/8: Mazid characters add karein")
            if not result['has_number']:
                print("   - Add at least one number (0-9)")
            if not result['has_symbol']:
                print("   - Add at least one symbol (!@#$%^&*)")
            if not result['has_uppercase']:
                print("   - Add at least one uppercase letter (A-Z)")
            print()

# Program run karna
if __name__ == "__main__":
    main()
