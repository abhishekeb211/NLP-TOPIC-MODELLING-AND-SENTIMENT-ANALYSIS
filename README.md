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

1]LSI Model:
Top 10 or N number of topics consider while representing into concept or terms in graphical format
eg. 
Bitcoin Tweets Dataset:

[(0, '0.802*"bitcoin" + 0.257*"\\u2026" + 0.257*"blockchain" + 0.248*"crypto" + 0.233*"cryptocurrency" + 0.203*"ethereum" + 0.164*"SCREEN_NAME" + 0.070*"airdrop" + 0.056*"token" + 0.055*"price"'), (1, '0.377*"bitcoin" + -0.307*"token" + -0.270*"\\u2026" + -0.269*"freetoken" + -0.263*"30;000" + -0.263*"15;000" + -0.261*"worth" + -0.251*"blockchain" + -0.229*"crypto" + -0.202*"airdrop"'), (2, '0.344*"bitcoin" + -0.288*"SCREEN_NAME" + 0.264*"30;000" + 0.264*"15;000" + -0.262*"blockchain" + 0.262*"worth" + 0.251*"freetoken" + -0.241*"ethereum" + -0.225*"\\u2026" + 0.215*"token"'), (3, '-0.855*"SCREEN_NAME" + -0.211*"airdrop" + -0.167*"cybersecurity" + 0.157*"blockchain" + -0.155*"bounty" + 0.149*"crypto" + -0.098*"token" + 0.095*"price" + -0.085*"freetoken" + -0.079*"altcoin"'), (4, '0.476*"ratio" + -0.391*"cybersecurity" + 0.257*"hitbtc" + 0.236*"SCREEN_NAME" + -0.196*"cryptocurrency" + -0.193*"ethereum" + -0.186*"airdrop" + 0.183*"price" + 0.159*"trading" + 0.150*"arbitraj"'), (5, '0.563*"ratio" + 0.279*"hitbtc" + 0.246*"ethereum" + 0.227*"cybersecurity" + -0.194*"trading" + -0.181*"crypto" + 0.175*"arbingtool" + 0.175*"arbitraj" + 0.174*"arbitrage" + 0.173*"cryptocurrency"'), (6, '0.407*"\\u2026" + -0.385*"escort" + -0.254*"costarica" + -0.229*"mexico" + -0.207*"guatemala" + -0.207*"\\u2605\\u2605\\u2605" + -0.195*"cryptocurrency" + -0.177*"nowplaying" + -0.171*"\\u279c" + -0.171*"blockchain"'), (7, '-0.271*"stock" + -0.262*"investment" + -0.250*"makemoneyonline" + -0.246*"trading" + -0.236*"workfromhome" + -0.235*"block" + -0.231*"internetmarketing" + -0.231*"strategy" + -0.230*"affiliate" + -0.229*"paypal"'), (8, '0.676*"airdrop" + -0.251*"cybersecurity" + -0.228*"blockchain" + 0.225*"javatoken" + -0.159*"SCREEN_NAME" + 0.144*"crypto" + 0.141*"bounty" + 0.115*"joining" + 0.114*"limited" + 0.114*"jtokens"'), (9, '0.491*"crypto" + -0.370*"\\u2026" + 0.220*"cybersecurity" + 0.213*"fintech" + 0.190*"cryptocurrency" + -0.184*"escort" + 0.176*"market" + 0.175*"wallet" + -0.166*"\\u2605\\u2605\\u2605" + 0.158*"money2020"')]

2]LDA Model:
Process to discover topics from documents as independent distribution. Disadvantage of this model is optimal solution not achieved in minimal iterations.


3]HDP Model:
All topics are considered and learned from tokens to improvise result. Advanced version of LDA Model to get exact concept and terms where discussed in huge documents.

*Coherence Value:
To find value of N ,N is number of topics considered in Topic Modelling.  

