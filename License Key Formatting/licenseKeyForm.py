def licenseKeyFormatting(S, k):
    if len(S) == 12000 or k <= 0 or len(S) == '':
        return ''
    
    
    k_count = 0
    clean_s = ''
    for i in range(1, len(S) + 1):
        if S[-i] != '-':
            print(S[-i])
            k_count += 1
            clean_s = clean_s + S[-i].upper()
            if k_count == k:
                clean_s = clean_s + '-'
                k_count = 0
    
    for i in range(1, k_count):
        if S[-i] != '-':
            clean_s = clean_s + S[-i].upper()
    
    if clean_s[-1] == '-':
        clean_s = clean_s[:-1]
        
    return clean_s[::-1]
    
if __name__ == '__main__':
    print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(licenseKeyFormatting("2-5g-3-J", 2))
        
    
    
