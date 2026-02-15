"""OneStop-CyberShop  Simple CLI Utility by Emilio Bottiglia. See README for additional info"""
"""v1.2 - See Changelog.md for details"""

import hashlib       
from pathlib import Path
from time import sleep

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
    print("Welcome to OneStop-CyberShop 1.2 Simple CLI Utility by Emilio Bottiglia")
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
    user_choice = user.strip().lower()
    if user_choice == 'q':
        return 'quit'
    return 'back'

#compute SHA-256 hash of a text string
#return a hex digest
def sha256_of_text(text):
    #convert the string to bytes.
    data = text.encode('utf-8')
    #compute the digest.
    digest = hashlib.sha256(data).hexdigest()
    return digest

#compute SHA-256 hash of a file, read file in small chunks
#return a hex digest
def sha256_of_file(file_path):
    # create a hash object
    hash_object = hashlib.sha256()
    #pen the file in binary mode
    with open(file_path, 'rb') as f:
        #read chunks until the file ends
        while True:
            #read a chunk of bytes
            chunk = f.read(4096)
            # Step 3b: If chunk is empty, we reached end-of-file.
            if not chunk: #chuck empty,file ended
                break
            #add the chunk to the hash calculator.
            hash_object.update(chunk)
    #convert the final hash to a hex string
    return hash_object.hexdigest()

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
        #keep asking until we get a valid answer
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
    #call ask_back_or_quit() to go back or quit
    return ask_back_or_quit()

#ask user for a file path, hash it with SHA-256
# display result
def option_hash_file():
    print("--- SHA-256 for File ---")

    #keep asking until we get a valid path
    while True:
        file_path = input("Enter file path to hash: ")

        #emove double quotes from the ends
        remove_double_q = file_path.strip('"')

        #remove single quotes from the ends
        remove_single_q = remove_double_q.strip("'")

        #create a Path object
        path_obj = Path(remove_single_q)

        #validate it exists and is a file
        if path_obj.is_file():
            break

        #if invalid loop again
        print("File not found. Please check the path and try again.")

    #exception handling
    try:
        #ompute the file SHA-256
        digest = sha256_of_file(remove_single_q)

        print(f"SHA-256: {digest}")

        #lack of access
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")

        # other input/output problems.
    except OSError as e:
        print(f"Error: Could not read the file ({e}).")

    #call ask_back_or_quit() to go back or quit
    return ask_back_or_quit()

#compare two checksums provided by user
def option_compare_hashes():
    print("--- Compare Checksums ---")
    print("Enter two checksums separated by a colon (:)")
    print("Example: abc123:abc123")

    #keep asking until input is valid
    while True:
        get_checksum = input("Checksums: ")

        #check colon
        if ":" not in get_checksum:
            print("Please include a colon -> : between the two checksums.")
            continue

        #split left and right checksum
        split_string = get_checksum.split(":", 1)
        #befor colon
        left_checksum = split_string[0]
        #after colon
        right_checksum = split_string[1]

        #normalize both sides
        left_checksum = left_checksum.strip().lower()
        right_checksum = right_checksum.strip().lower()

        #check both sides exist
        if left_checksum == "" or right_checksum == "":
            print("Please consider both checksum values cannot be empty. Try again.")
            continue
        #compare and print output
        if left_checksum == right_checksum:
            print("Result: MATCH")
        else:
            print("Result: NOT MATCH")
        #exit the loop after a valid comparison
        break
    #call ask_back_or_quit() to go back or quit
    return ask_back_or_quit()


def main():
    while True:
        show_menu()
        #normalize user choice
        choice = input("Choose an option: ").strip().lower()

        if choice == '1':
            #call option_hash_text.
            #result hold value of "return ask_back_or_quit()"
            result = option_hash_text()

        elif choice == '2':
            result = option_hash_file()

        elif choice == '3':
            result = option_compare_hashes()

        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            sleep(1)
            continue

        if result == 'quit':
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
