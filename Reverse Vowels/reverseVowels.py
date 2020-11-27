def reverseVowels(string):
    if string == None:
        return None
    if string == "":
        return ""
    
    vowels = ['A','E','I','O','U']
    vowels_list = []
    vowels_index = []
    
    for index, char in enumerate(string):
        if char in vowels:
            vowels_list.append(char)
            vowels_index.append(index)
    

    vowels_list.reverse()
    
    for i, index in enumerate(vowels_index):
        string = string[:index] + vowels_list[i] +string[index+1:]
    
    return string

if __name__ == '__main__':
    print(reverseVowels("ALPHABET"))
    print(reverseVowels("BEBECO"))
    print(reverseVowels("AEIOU"))
    
