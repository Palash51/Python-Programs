from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


filtered_sentence = []
def text_cleanup(text):
    new = ""
    for i in text:
        if i not in "1234567890-->'\"?,.!/;:@#$%﻿I":
            new += i
    
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(new)
    filtered_sentence = []
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    print filtered_sentence
    
#strng = "pal@#$%as!h pa!.ti@#d,:a!r"
strng = open('Suit.srt').read()
text_cleanup(strng)




#example_sentence = "This is an example showinging off stop word filteration."

#example_sentence = open('Suit.srt').read()
#stop_words = set(stopwords.words("english"))

#print(stop_words)

#words = word_tokenize(example_sentence)

#filtered_sentence = []

#for w in words:
 #   if w not in stop_words:
  #      filtered_sentence.append(w)


print filtered_sentence
