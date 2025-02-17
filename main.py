def main ():
    book="books/frankenstein.txt"
    text=get_book_text(book)
    num_words=get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print (f"--- Begin report of {book} ---")
    print (f"{num_words} words found in the document")
    print ()
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["num"]} times")
    print ("--- End report ---")

    #ount=0
        #print (file_contents)
    #rint (count_words(file_contents))
    #print (count_characters(file_contents))
    #ook_report(book, count_words(file_contents), count_characters(file_contents))
    
    #for c, n in count_characters(file_contents):
    #     if count != 0:
    #        dic_string += ", "
    #    else:
    #        count += 1
    #    dic_string += f"'{c}' : {n}"
    #print (f"'{'{dic_string} '}'")

def get_num_words(book_text):
    words = book_text.split()
    counter=0
    for word in words:
        counter +=1
    return counter


def sort_on(dict):
    return dict["num"] 


def chars_dict_to_sorted_list(chars_count):
    sorted_count = []
    for char in chars_count:
        sorted_count.append({"char" : char, "num" : chars_count[char]})
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count


def get_chars_dict(book_text):
    chars = {}
    lowered_string = book_text.lower()    
    for char in lowered_string:
        if char not in chars:
            chars[char] = 1
        else:  
            chars[char] += 1
    return chars


def    get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()
