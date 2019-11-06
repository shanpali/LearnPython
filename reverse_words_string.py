# its mostly done by the use of slicing technique
def reverse_words_1(line):
    return ' '.join(word[::-1] for word in line.split(" "))


def reverse_words_2(line):
    words = line.split(" ")
    reversed = [word[::-1] for word in words]
    reversed_line = " ".join(reversed)
    return reversed_line


print(reverse_words_1("abc xyz mnp"))
