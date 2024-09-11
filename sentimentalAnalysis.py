from numpy import double


def sentimentalAnalysis(filename):
    # Implement your code here

    strengthlist = {}
    with open("wordwithStrength.txt", 'r', encoding='utf-8') as file:
        for line in file:
            word, strength = line.split()
            strengthlist[word] = float(strength)
    sentimental = 0
    with open(filename, 'r', encoding='utf-8') as file:
        review = file.read()
        words = review.split()
        for word in words:
            if word in strengthlist:
                sentimental += strengthlist[word]
    return sentimental
    pass
