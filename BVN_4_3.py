# Tham số RSA
p, q, e = 17, 23, 5
n = p * q
phi = (p - 1) * (q - 1)

print(f"n = {n}, phi(n) = {phi}")

# Thông điệp
plaintext = "Toan"
ascii_vals = [ord(ch) for ch in plaintext]
print("ASCII:", ascii_vals)

# Mã hóa RSA:
cipher = [pow(m, e, n) for m in ascii_vals]
print("Ciphertext:", cipher)
