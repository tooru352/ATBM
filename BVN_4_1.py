def MaHoa(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if c != ' ':
            so = ord(c) - 65
            so = (so + key) % 26
            ciphertext += chr(so + 65)
        else:
            ciphertext += c
    return ciphertext

# def GiaiMa(ciphertext, key):
#     plaintext = ""
#     for c in ciphertext:
#         if c != ' ':
#             so = ord(c) - 65
#             so = (so - key + 26) % 26
#             plaintext += chr(so + 65)
#         else:
#             plaintext += c
#     return plaintext

def main():
    p = (input("Nhap chuoi can ma hoa:")).upper()
    key = int(input("Nhap khoa ma hoa:"))
    c = MaHoa(p, key)
    print("Chuoi sau khi ma hoa:", c)
    # print("Chuoi sau khi giai ma:", GiaiMa(c, key))
    
if __name__ == "__main__": #entry point
    main()