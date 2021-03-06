import logging, gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# load id->word mapping (the dictionary), one of the results of step 2 above
id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
# load corpus iterator
mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm')
# mm = gensim.corpora.MmCorpus('wiki_en_tfidf.mm.bz2') # use this if you compressed the TFIDF output

print(mm)

lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000,
                                      passes=1)
lda.print_topics(20)
