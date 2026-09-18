import secrets
import string
import math

class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.chars = self.letters + self.digits
    
    def generate(self, length=16):
        if length < 8 or length > 128:
            print("Length must be between 8 and 128")
            return None
        
        password = ''.join(secrets.choice(self.chars) for _ in range(length))
        entropy = length * math.log2(len(self.chars))
        
        return password, round(entropy, 2)

# Main
gen = PasswordGenerator()

print("\n=== PASSWORD GENERATOR ===\n")
length = int(input("Enter password length (8-128): "))

result = gen.generate(length)
if result:
    password, entropy = result
    print(f"\nPassword: {password}")
    print(f"Entropy:  {entropy} bits")
    print(f"Security: {'STRONG ✓' if entropy >= 80 else 'WEAK ❌'}\n")