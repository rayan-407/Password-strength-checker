
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
