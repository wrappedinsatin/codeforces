word = input()

if len(word) > 10:
    mid = str(len(word) - 2)
    print(word[0] + mid + word[-1])
else:
    print(word)
