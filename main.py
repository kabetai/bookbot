import string

def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = word_count(file_contents)
    character_counts = count_characters(file_contents)
    dict_list = convert_dict_into_dict_list(character_counts)
    dict_list.sort(reverse=True, key=sort_by_num_descending)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    for character_count in dict_list:
        print(f"The {character_count['character']} character was found {character_count['count']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(contents):
        words = contents.split()
        return len(words)

def count_characters(text):
    alphabet = string.ascii_lowercase
    lower_text = text.lower()
    character_counts = {}
    for character in alphabet:
        c_count = lower_text.count(character)
        character_counts[character] = c_count
    return character_counts

# convert dictionary into list of dictionaries (objects)
# so it has meanful fields that can by sorted by
def convert_dict_into_dict_list(dict_counts):
    dict_list = [] 
    for key,value in dict_counts.items():
        dl = {}
        dl["character"] = key
        dl["count"] = value
        dict_list.append(dl)
    return dict_list


# return value to compare when sorting from dictionary item
def sort_by_num_descending(dict):
    return dict["count"]

main()


