def shift_char(ch, k):
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + k) % 26 + base)
    elif 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + k) % 26 + base)
    else:
        return ch  # giữ nguyên ký tự không chữ cái

def encrypt(plaintext, k=0):
    ciphertext_chars = []
    for ch in plaintext:
        ciphertext_chars.append(shift_char(ch, k))
    return ''.join(ciphertext_chars)

def decrypt(ciphertext, k=0):
    plaintext_chars = []
    for ch in ciphertext:
        plaintext_chars.append(shift_char(ch, -k))
    return ''.join(plaintext_chars)

# --- Ví dụ sử dụng ---
P = "TenCuaBan"
k = 9  # dịch cố định 9
C = encrypt(P, k)
print("Plaintext:", P)
print("Ciphertext (k = 9):", C)

