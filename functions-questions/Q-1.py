#Reverse Words in a Sentence
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("you are the best"))
