def count_words(text):
    words=text.split()
    return len(words)

def count_letters(text):
    # Convert any uppercase letters to lowercase letters, we don't want duplicates.
    lowered_string=text.lower()
    letters_dict={}
    for i in lowered_string:
        if i in letters_dict.keys():
            continue
        letters_dict[i]= lowered_string.count(i)
    return letters_dict

def sort_counted_letters(letters_dict):
    sorted_list=[]
    key_pass_so_far=[]
    for i in letters_dict:
        max=0
        key_to_max=None
        for j in letters_dict:
            if j in key_pass_so_far:
                continue
            if letters_dict[j]>max:
                max=letters_dict[j]
                key_to_max=j
        sorted_list.append([key_to_max,max])
        key_pass_so_far.append(key_to_max)
    return sorted_list



def print_report(book_path,word_count,sorted_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for i in sorted_letters:
        if i[0].isalpha():
            print(f"The {i[0]} character was found {i[1]} times")
    print(f"--- End report ---")



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count=count_words(text)
    sorted_letters=sort_counted_letters(count_letters(text))
    #print(sorted_letters)
    print_report(book_path,word_count,sorted_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()        

main()