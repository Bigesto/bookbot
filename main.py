def main():
    book = get_text(path)
    letters_dict = how_many_letters_each(book)
    print(f"--- Begin report of {path} ---")
    print(f"{counting_words(book)} words found in the document.\n")
    sort_letters_by_quantity(letters_dict)
    print("--- End report ---")
    


path = 'books/frankenstein.txt'

def get_text(path):
    with open(path, "r") as f:
        return f.read()

def counting_words(text):        
    words = text.split()
    return len(words)

def explore_text(text):
    words = text.split()
    word_count = len(words)
    print(f"This text has {word_count} words. Enter a number between 0 and {word_count-10}")
    
    while True:
        position = input("Enter a starting position (or 'q' to quit): ")
        if position.lower() == 'q':
            break
        try:
            position = int(position)
            if position < 0:
                print(f"Please enter a number between 0 and {word_count}")
                continue
            percentage = round((position/word_count)*100, 1)
            print(f"Words {position} to {position+10}: {words[position:position+10]} \nYou're at {percentage}% of the book.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit")

def how_many_letters_each(text):
    alphabet = list("abcdefgijklmnopqrstuvwxyz")
    lower_text = text.lower()
    text_in_letters = list(lower_text)

    final_dictionnary = {}
    for letter in alphabet:
        final_dictionnary[letter] = 0
        for l in text_in_letters:
            if l == letter:
                final_dictionnary[letter] += 1
   
    return final_dictionnary

def sort_letters_by_quantity(dict):
    dict_list = []
    for character, count in dict.items():
        dict_list.append({"char": character, "num": count})
    
    dict_list.sort(reverse=True, key=lambda x: x["num"])
    
    for char_dict in dict_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times.")


    

# Execute the main function
if __name__ == "__main__":
    main()