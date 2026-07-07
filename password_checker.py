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
