 import nltk
 from nltk.corpus import brown
 d={'iphone':'apple''nexus4''Google-LG'}
 #ввела нові значення
 d['htc desire x']='HTC'
 # намагалося створити неіснуючий вхід
 print d['xyz']

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print d['xyz']
KeyError: 'xyz'
 #нам вибиває помилку
