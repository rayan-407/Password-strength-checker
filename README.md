def check_password(password):

    length = len(password)
    
    has_num = False
    
    has_sym = False
    
    has_upper = False
    
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    
    for ch in password:
    
        if ch.isdigit():
        
            has_num = True
            
        if ch in symbols:
        
            has_sym = True
            
        if ch.isupper():
        
            has_upper = True   
            
    features = 0
    
    if has_num:
    
        features += 1
        
    if has_sym:
    
        features += 1
        
    if has_upper:
    
        features += 1
        
    if length >= 8 and features >= 3:
        return "Strong"
    elif length >= 6 and features >= 2:
        return "Medium"
    else:
        return "Weak"
        
def main():

    print("="*40)
    
    print("PASSWORD STRENGTH CHECKER")
    
    print("="*40)
    
    print("\nRules:")
    
    print("- Minimum 8 characters")
    
    print("- At least 1 number (0-9)")
    
    print("- At least 1 symbol (!@#$%^&*)")
    
    print("- At least 1 uppercase (A-Z)")
    
    print("\n" + "-"*40)
    
    while True:
    
        pwd = input("\nEnter password (or 'quit' to exit): ")
        
        if pwd.lower() == "quit":
        
            print("\nGoodbye!")
            
            break
            
        if len(pwd) == 0:
        
            print("Password cannot be empty!")
            
            continue
            
        result = check_password(pwd)
        
        print("\n" + "="*40)
        
        print("RESULT")
        
        print("="*40)
        
        print(f"Password: {'*' * len(pwd)}")
        
        print(f"Length: {len(pwd)} characters")
        
        print(f"Strength: {result}")
        
        if result == "Weak":
        
            print("\nSuggestions:")
            
            if len(pwd) < 8:
            
                print("- Make it at least 8 characters")
                
            if not any(ch.isdigit() for ch in pwd):
            
                print("- Add a number (0-9)")
                
            if not any(ch in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for ch in pwd):
            
                print("- Add a symbol (!@#$%^&*)")
                
            if not any(ch.isupper() for ch in pwd):
            
                print("- Add uppercase letter (A-Z)")
                
        elif result == "Medium":
        
            print("\nTip: Add more features to make it Strong")
            
        
        print("="*40)
        

if __name__ == "__main__":
    main()
# 🔐 Password Strength Checker

A simple yet effective Python CLI tool that evaluates password strength based on real security criteria — length, character variety, and common weaknesses — and gives actionable suggestions to improve weak passwords.

> First project of my Cybersecurity Internship  🚀

## 🧠 How It Works

The tool checks each password against 4 key security criteria:
- ✅ Minimum length (8+ characters)
- ✅ Contains at least 1 number (0-9)
- ✅ Contains at least 1 special symbol (!@#$%^&* etc.)
- ✅ Contains at least 1 uppercase letter (A-Z)

Based on how many of these are met, the password is rated:
- 🔴 **Weak**
- 🟡 **Medium**
- 🟢 **Strong**

If the password is weak, the tool gives **specific suggestions** on what to add to make it stronger.

## ▶️ How to Run

```bash
python password_checker.py
```

Then just enter a password when prompted. Type `quit` to exit.

## 🛠️ Built With
- Python 3

## 📌 Why This Project
Weak passwords remain one of the top causes of account compromise. This project was a hands-on way to translate password security concepts (length, entropy-boosting characters, common patterns) into working code.

## 🔮 Future Improvements
- Check against known breached password lists (Have I Been Pwned API)
- Add a GUI or web interface
- Password strength meter (visual bar)

---
👤 Built by [Muhammad Rayan](https://github.com/rayan-407)
