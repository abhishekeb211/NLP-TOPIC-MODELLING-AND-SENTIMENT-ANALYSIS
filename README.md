# NLP-TOPIC-MODELLING-AND-SENTIMENT-ANALYSIS
RNN ,LSTM and Multiple Topic Map reduce Algorithms with Sentiment Analysis


Setup Virtual Environment(nlp_requirements.txt)
env to install all files in the requirements.txt file.
1.	cd to the directory where requirements.txt is located
2.	activate your virtualenv eg.-	source bin/activate
3.	run: pip install -r nlp_requirements.txt in your shell



PRE-PROCESSING :
1.	Batch Processing (Time Series Preprocessing.py)
Dataset in different format including huge continuous text and time series data.
(Sometimes data format conversion requires as core panda series , Big-query data and various databases )*
•	Text data can be split into lesser than 1 Lac words in different files
•	Time Series data divide into year, month, week and days according to data size.

2.	NLP (Word Processing.py)
•	Tokenization: Divide sentence into smaller parts and removing punctuations.
•	Lemmatization: Stemming means cutting ends and beginnings of words into root form
•	Removing Stop-Words: Removing prepositions from Tokens

3.	Map-Reduce Topic Modelling( Topic Modelling.py):
Labelling unsupervised text from topic modelling with extracting Most frequently and highest embedding value Tokens
•	Dictionary: Creating set of all tokens in document as genism dictionary projection format
•	Corpus: word embedding process word to vector form

LSI Model:
Top 10 or N number of topics consider while representing into concept or terms in graphical format

LDA Model:
Process to discover topics from documents as independent distribution. Disadvantage of this model is optimal solution not achieved in minimal iterations.


HDP Model:
All topics are considered and learned from tokens to improvise result. Advanced version of LDA Model to get exact concept and terms where discussed in huge documents.

Coherence Value:
To find value of N ,N is number of topics considered in Topic Modelling.  

