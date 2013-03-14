 import nltk
 from nltk.corpus import brown
 words_tagged=brown.tagged_words(categories='news')
 fd=nltk.FreqDist(words_tagged)
 word_list=fd.keys()
 word_list.reverse()
 words_to_change=word_list[:3000]
 words_to_change_list=[]
 for w in words_to_change:
	words_to_change_list.append(w[0])
	sents_train=brown.tagged_sents(categories='news')
	sent_with_changes=[]
	sent_one=[]
	counter=0
	for sent in sents_train:
		for word in sent:
			if word[0] in words_to_change_list:
				sent_one.append(('UNK',word[1]))
				counter=counter+1
				else:
                                   sent_one.append(word)
					sent_with_changes.append(sent_one)
					sent_one=[]

print counter,' words were changed to UNK in training sentences.'
words_to_tag=brown.words()[:3000]
Bigram_tagger=nltk.BigramTagger(sents_train)
Bigram_tagger_with_changes=nltk.BigramTagger(sent_with_changes)
Bigram_tagger.tag(brown.sents()[66])
Bigram_tagger_with_changes.tag(brown.sents()[66])

print 'Accuracy Bigram_tagger (on brown sents): %4.1f%%' % (
	  100.0 * Bigram_tagger.evaluate(brown.tagged_sents()[:6000]))
print 'Accuracy Bigram_tagger_with_changes (on brown sents): %4.1f%%' % (
	 100.0 * Bigram_tagger_with_changes.evaluate(brown.tagged_sents()[:6000]))

Bigram_tagger.tag(words_to_tag)
Bigram_tagger_with_changes.tag(words_to_tag)
print 'Accuracy Bigram_tagger (on 3000 words): %4.1f%%' % (
	100.0 * Bigram_tagger.evaluate(brown.tagged_sents()[:6000]))
print 'Accuracy Bigram_tagger_with_changes (on 3000 words): %4.1f%%' % (
	 100.0 * Bigram_tagger_with_changes.evaluate(brown.tagged_sents()[:6000]))

Unigram_tagger=nltk.UnigramTagger(sents_train)
Unigram_tagger_with_changes=nltk.UnigramTagger(sent_with_changes)
Unigram_tagger.tag(brown.sents()[66])
Unigram_tagger_with_changes.tag(brown.sents()[66])

print 'Accuracy Unigram_tagger (on brown sents): %4.1f%%' % (
	100.0 * Unigram_tagger.evaluate(brown.tagged_sents()[:6000]))
print 'Accuracy Unigram_tagger_with_changes (on brown sents): %4.1f%%' % (
	100.0 * Unigram_tagger_with_changes.evaluate(brown.tagged_sents()[:6000]))

Unigram_tagger.tag(words_to_tag)
Unigram_tagger_with_changes.tag(words_to_tag)
print 'Accuracy Unigram_tagger (on 3000 words): %4.1f%%' % (
	100.0 * Unigram_tagger.evaluate(brown.tagged_sents()[:6000]))
print 'Accuracy Unigram_tagger_with_changes (on 3000 words): %4.1f%%' % (
	100.0 * Unigram_tagger_with_changes.evaluate(brown.tagged_sents()[:6000]))

				else: 
