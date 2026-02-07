"""OneStop-CyberShop  Simple CLI Utility. see README for additional info"""

import hashlib       
from pathlib import Path

logo = """


  ▄▄▄▄                 ▄▄▄▄    ▄                           ▄▄▄         █                     ▄▄▄▄  █                          
 ▄▀  ▀▄ ▄ ▄▄    ▄▄▄   █▀   ▀ ▄▄█▄▄   ▄▄▄   ▄▄▄▄          ▄▀   ▀ ▄   ▄  █▄▄▄    ▄▄▄    ▄ ▄▄  █▀   ▀ █ ▄▄    ▄▄▄   ▄▄▄▄         
 █    █ █▀  █  █▀  █  ▀█▄▄▄    █    █▀ ▀█  █▀ ▀█         █      ▀▄ ▄▀  █▀ ▀█  █▀  █   █▀  ▀ ▀█▄▄▄  █▀  █  █▀ ▀█  █▀ ▀█        
 █    █ █   █  █▀▀▀▀      ▀█   █    █   █  █   █   ▀▀▀   █       █▄█   █   █  █▀▀▀▀   █         ▀█ █   █  █   █  █   █        
  █▄▄█  █   █  ▀█▄▄▀  ▀▄▄▄█▀   ▀▄▄  ▀█▄█▀  ██▄█▀          ▀▄▄▄▀  ▀█    ██▄█▀  ▀█▄▄▀   █     ▀▄▄▄█▀ █   █  ▀█▄█▀  ██▄█▀        
                                           █                     ▄▀                                              █            
                                           ▀                    ▀▀                                               ▀                                

"""


def show_menu():
    print(logo)
    print("Welcome to OneStop-CyberShop 1.0 Simple CLI Utility")
    #menu options.
    print("1) Create SHA-256 checksum for text")
    print("2) Create SHA-256 checksum for a file")
    print("3) Compare two checksums")
    print("4) Build logins from names file")
    print("Q) Quit")

#ask user whether to return to the main menu or quit
def ask_back_or_quit() :
    user = input("Press Enter to return to the menu, or Q to quit: ")
    #normalize the input (trim spaces, make lower-case).
    user = user.strip().lower()
    if user == 'q':
        return 'quit'
    return 'back'

#compute SHA-256 hash of a text string
#return a hex digest
def sha256_of_text():
    #convert the string to bytes.
    data = text.encode('utf-8')
    #compute the digest.
    digest = hashlib.sha256(data).hexdigest()
    return digest

#ask user for text, hash it with SHA-256
# display result
def option_hash_text():
    print("--- SHA-256 for Text ---")
    text = input("Enter text to hash: ")
    #if user enters empty string, inform them
    if text == "":
        print("You entered an empty string.")
        print("Empty strings could be hashed, but this might not be what you wanted.")
        #options at this stage
        print("what would you like to do?")
        print("  C) Continue (hash empty string)")
        print("  B) Back to main menu")
        #we keep asking until we get a valid answer
        while True:
            choice = input("Your choice (C or B): ").strip().lower()
            if choice == 'b':
                return 'back'
            if choice == 'c':
                break
            #if user doesn't enter b or c, ask again.
            print("Please type C to continue or B to go back.")

    #if text entered is a valid string, compute SHA-256 digest
    digest = sha256_of_text(text)
    print(f"SHA-256: {digest}")
    #call ask_back_or_quit() to go back or quit.
    return ask_back_or_quit()


# this is the program entry point
def main():
    while True:
        show_menu()
        #normalise user choice
        choice = input("Choose an option: ").strip().lower()
        if choice == '1':
            #call option_hash_text
            result = option_hash_text()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        if result == 'quit':
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
