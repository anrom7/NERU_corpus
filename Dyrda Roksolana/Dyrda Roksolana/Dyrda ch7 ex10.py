# Dyrda Roksolana, AL-13, ch7, ex10

import nltk
import nltk.chunk
from nltk.corpus import conll2000 #3 типи чанку: NP chunks; VP chunks; and PP chunks
f1 = nltk.RegexpParser("")
sentences = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
grammar = r"NP: {<[CDJNP].*>+}"# пошук тегів, котрі починаються з літер, що характеризують фрази іменникового виразу 
f1 = nltk.RegexpParser(grammar)
print f1.evaluate(sentences)
class BigramChunker(nltk.ChunkParserI):
    def __init__(self, sentences1): 
        data = [[(x,y) for w,x,y in nltk.chunk.tree2conlltags(sent)]
                      for sent in sentences1]
        self.tagger = nltk.BigramChunker(data)# Зміна імя класу на BigramChunker,  модифікація  лінії для будування BigramTagger а не UnigramTagger

   # Метод парсингу для чанкування нових речень
    def parse(self, sentence): 
        l_tags = [p for (w,p) in sentence]
        tagged_l_tags = self.tagger.tag(l_tags)
        chunktags = [chunktag for (p, chunktag) in tagged_l_tags]
        conlltags = [(w, p, chunktag) for ((w,p),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

sentences = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
sentences1 = conll2000.chunked_sents('train.txt', chunk_types=['NP'])           
# ми можемо вдосконалити виконання NP chunker.	
