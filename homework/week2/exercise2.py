
def letter_count (word, letter):
    count = 0
    for x in word:
        if x.lower() == letter.lower():
            count = count + 1
    return count

print(letter_count("Bananas", "n"))
print(letter_count("Tarantula", "t"))