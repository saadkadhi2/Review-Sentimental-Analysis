import os
import sentimentalAnalysis as sa


posFolder = '../Data/pos'
negFolder = '../Data/neg'

# Process positive files
files = os.listdir(posFolder)
for file in files:
    if file.endswith('.txt'):
        sent_score = sa.sentimentalAnalysis(os.path.join(posFolder, file))
        print(file)
        print(f"Groundtruth: Positive, sentimental score: {sent_score}")

# Process negative files
files = os.listdir(negFolder)
for file in files:
    if file.endswith('.txt'):
        sent_score = sa.sentimentalAnalysis(os.path.join(negFolder, file))
        print(file)
        print(f"Groundtruth: Negative, sentimental score: {sent_score}")
