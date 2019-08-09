# CREATING DICTIONARY AS WORD AND VECTOR
# CORPUS TEXT WITHOUT PUNCTUATIONS,ALPHABETS AND WORD ROOT FORM
# LSI ,HDP AND LDA MODELS

def dict_corp(file) :
    file1=file+'_Token.txt'
    corpus=file+'_Corpus.pkl'
    lsid=file+'_Lsi.gensim'
    HDP=file+'_HDP.gensim
    LDA=file+'_LDA.gensim'
    Dict=file+'_dictionary.gensim'
    text_data=''
    abs1=[]
    with open(file1) as f3:
        text_data = simplejson.load(f3)

        # DICTIONARY SAVE
        Dictionary = corpora.Dictionary(text_data)
        Dictionary.save(Dict)

        # CORPUS SAVE         
        Corpus = [Dictionary.doc2bow(text) for text in text_data]
        pickle.dump(Corpus, open(corpus, 'wb'))
        
        # LSI MODEL CODE
        Lsi_Model=LsiModel(corpus=Corpus,num_topics=10,id2word=Dictionary)
        Lsi_Model.save(lsid)

        # HDP MODEL
        HDP_Model=HdpModel(corpus=Corpus,id2word=Dictionary)
        HDP_Model.save(HDP)

        Ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 10, id2word=dictionary, passes=10)
        Ldamodel.save(LDA)
        lda_display = pyLDAvis.gensim.prepare(Ldamodel, corpus, dictionary, sort_topics=False)
        pyLDAvis.display(lda_display)
        
#FILE NAMES
EFiles=['3_1_WEEK','3_2_WEEK','3_3_WEEK','3_4_WEEK','3_5_WEEK',
       '4_1_WEEK','4_2_WEEK','4_3_WEEK','4_4_WEEK','4_5_WEEK',
       '5_1_WEEK','5_2_WEEK','5_3_WEEK','5_4_WEEK','5_5_WEEK',
       '6_1_WEEK','6_2_WEEK','6_3_WEEK','6_4_WEEK','6_5_WEEK',
       '7_1_WEEK','7_2_WEEK','7_3_WEEK','7_4_WEEK','7_5_WEEK']


# PASSING FILE NAME TO DICTIONARY AND CORPUS AND LSI MODEL 
for E in EFiles:
    print(E)
    dict_corp(E)
    