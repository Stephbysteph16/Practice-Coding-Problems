
def numUniqueEmails(emails):
    
    cleaned_emails = []
    for email in emails:
        clean = removeDots(email)
        clean = removePlus(clean)
        cleaned_emails.append(clean)

    cleaned_emails = set(cleaned_emails)
    print(cleaned_emails)
    return len(cleaned_emails)

def removeDots(email):
    i = 0
    for char in email:
        if char == "@":
            break
        if char == ".":
            email = email[:i] + email[i+1:]
        else:
            i += 1

    return email


def removePlus(email):
    at_index = email.find("@")
    plus_index = email.find("+")
    localName = email[:at_index]
    if plus_index >= 0:
        localName = localName[:plus_index]

    return localName + email[at_index:]
