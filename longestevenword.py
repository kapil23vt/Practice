import sys

def longestEvenWord(sentence):
    list1 = sentence.split()

    for s in list1[:]:
        if (len(s) % 2 != 0):
            list1.remove(s)

    return max(list1)


if __name__ == '__main__':
    result = longestEvenWord("Kapil Kale")
    print(result)