from stats import count_words
from stats import count_character_frequency
from stats import return_sorted_dict
import sys

def get_book_text(filepath):
    rtr_string = ""
    with open(filepath) as f:
        rtr_string = f.read()
    return(rtr_string)

def main():
    #print(sys.argv)

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        #print(book_path)


    line = ""
    char_list = []
    char_dict = {}
    word_count = 0
    book_contents = get_book_text(book_path)
    word_count = count_words(book_contents)
    char_dict = count_character_frequency(book_contents)
   #print(char_dict)
   #print(f"{word_count} words found in the document")
    sorted_char_list = return_sorted_dict(char_dict)
    #print(sorted_char_list)

    #final output:
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    index = 0
    
    for x in sorted_char_list: 
        for key, value in x.items(): #remembe you still have to itterate through key/value
          print(f"{key}: {value}")
 
    print("============= END ===============")

main()
