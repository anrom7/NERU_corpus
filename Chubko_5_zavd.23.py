import nltk
 from nltk.corpus import brown
 patterns = [
	(r'.*ing$', 'VBG'), # gerunds
	 (r'.*ed$', 'VBD'), # simple past
	(r'.*es$', 'VBZ'), # 3rd singular present
	(r'.*ould$', 'MD'), # modals
	(r'.*\'s$', 'NN$'), # possessive nouns
	(r'.*s$', 'NNS'), # plural nouns
	 (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
	(r'.*', 'NN') # nouns (default)
	]
 regexp_tagger = nltk.RegexpTagger(patterns)
 regexp_tagger.tag(brown.sents()[9])
[('The', 'NN'), ('City', 'NN'), ('Purchasing', 'VBG'), ('Department', 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('is', 'NNS'), ('lacking', 'VBG'), ('in', 'NN'), ('experienced', 'VBD'), ('clerical', 'NN'), ('personnel', 'NN'), ('as', 'NNS'), ('a', 'NN'), ('result', 'NN'), ('of', 'NN'), ('city', 'NN'), ('personnel', 'NN'), ('policies', 'VBZ'), ("''", 'NN'), ('.', 'NN')]
 brown_test=brown.tagged_sents()[:100]
 print 'Regular expressions Tagger:'
Regular expressions Tagger:
 print 'Accuracy: %4.1f%%' % (
	  100.0 * regexp_tagger.evaluate(brown.tagged_sents()[100:1000]))
Accuracy: 21.5%
 two_tagger=nltk.UnigramTagger(brown_test, backoff=regexp_tagger)
 print 'Regular expressions Tagger + Unigram tagger:'
Regular expressions Tagger + Unigram tagger:
 print 'Accuracy: %4.1f%%' % (

	 100.0 * two_tagger.evaluate(brown.tagged_sents()[100:1000]))
