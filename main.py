with open("C:/xampp/htdocs/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

def count(file_contents):
    words = file_contents.split()
    return len(words)

def characters(file_contents):
    chars = {}
    for c in file_contents:
        lower = c.lower()
        if lower in chars:
            chars[lower] += 1
        else: 
            chars[lower] = 1
    return chars
        
def sort_on(d):
    return d["num"]

def conv_dict_to_list(dictionary):
    sorted = []
    for chars in dictionary:
        sorted.append({"char": chars, "num": dictionary[chars]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

words = count(file_contents)    
book_dict = characters(file_contents)
new = conv_dict_to_list(book_dict)


print("Book report of Frankenstein")
print(f"{words} words found in the document")
print()
for item in new:
    if not item["char"].isalpha():
        continue
    print(f"The '{item['char']}' was found {item['num']} times")

print("End")
