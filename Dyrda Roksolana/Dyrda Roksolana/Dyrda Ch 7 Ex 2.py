
# Roksolana Dyrda, AL-13
# Ch7,task 2
#Regular expression–based NP chunker
import nltk
sentence=[("Katy", "NNP"), ("draws", "VBD"), ("rain", "JJ"), ("big", "JJ"), ("clouds", "NNS"), ("on", "IN"), ("the", "DT"), ("board","NN")]
grammar = "NP: {<DT>*<JJ>*<NN.*>+}" # створення граматики чанкеру
cp = nltk.RegexpParser(grammar)#створення chunk parser з використанням граматики 
result = cp.parse(sentence)#тестування chunk parser на реченні
print result
