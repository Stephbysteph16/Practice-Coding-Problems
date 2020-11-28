def licenseKeyFormatting(S, K):
    if len(S) == 12000 or K <= 0 or len(S) == '':
        return ''

    k_count = 0
    clean_s = ''
    last_pointer = 0
    for i in range(1, len(S) + 1):
        if S[-i] != '-':
            k_count += 1
            clean_s = clean_s + S[-i].upper()
            if k_count == K:
                clean_s = clean_s + '-'
                k_count = 0

    if clean_s != "" and clean_s[-1] == '-':
        clean_s = clean_s[:-1]

    return clean_s[::-1]
