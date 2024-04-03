def word_count(word):
    words = word.split()
    return len(words)
#print (word_count("hi  there"))  # Output: 2"

def char_count(string):
    count=string.count("a")
    print(count)
# char_count()


def capital_text(cool):
    case =cool.capitalize()
    print (case)
# capital_text()

def reverse_text(rev):
    print(rev[::-1])
# reverse_text()