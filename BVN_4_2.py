def shift_char(ch, k):
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + k) % 26 + base)
    elif 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + k) % 26 + base)
    else:
        return ch  # giữ nguyên ký tự không chữ cái

def encrypt(plaintext, use_position_as_k=True, k_list=None):
    ciphertext_chars = []
    n = len(plaintext)
    for i, ch in enumerate(plaintext):
        if k_list is not None:
            # lấy k từ danh sách (lặp lại khi hết)
            k = k_list[i % len(k_list)]
        elif use_position_as_k:
            k = i + 1  # số thứ tự bắt đầu từ 1
        else:
            k = 0
        ciphertext_chars.append(shift_char(ch, k))
    return ''.join(ciphertext_chars)

def decrypt(ciphertext, use_position_as_k=True, k_list=None):
    plaintext_chars = []
    for i, ch in enumerate(ciphertext):
        if k_list is not None:
            k = k_list[i % len(k_list)]
        elif use_position_as_k:
            k = i + 1
        else:
            k = 0
        plaintext_chars.append(shift_char(ch, -k))
    return ''.join(plaintext_chars)

# Ví dụ sử dụng:
P = "TenCuaBan"  # Plaintext theo yêu cầu: TenCuaBan
C = encrypt(P)   # dùng k = STT (1,2,3,...)
print("Plaintext:", P)
print("Ciphertext (k = STT):", C)

