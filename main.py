def strip_spaces(username):
    new_username = ""
    
    for current_char in username:
        if current_char == " ":
            pass
        else:
            new_username += current_char

    return new_username


def lowercase(username):
    new_username = ""
    
    for current_char in username.lower():
        new_username += current_char

    return new_username


def remove_special_chars(username):
    new_username = ""
    
    for current_character in username:
        if current_character.isalnum():
            new_username += current_character

    return new_username



def sanitize_username(username):
    return lowercase(remove_special_chars(strip_spaces(username)))



def main():
    print(sanitize_username("123"))


if __name__ == "__main__":
    main()
