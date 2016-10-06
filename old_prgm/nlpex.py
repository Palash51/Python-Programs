#from nltk.tokenize import sent_tokenize, word_tokenize
'''
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#print(sent_tokenize(EXAMPLE_TEXT))
#print(word_tokenize(EXAMPLE_TEXT))


for i in word_tokenize(EXAMPLE_TEXT):
    print(i)
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sentence = "This is an example showinging off stop word filteration."

#example_sentence = open('Suit.srt').read()
stop_words = set(stopwords.words("english"))

#print(stop_words)

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)


print filtered_sentence
