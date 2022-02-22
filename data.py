# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim_models

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore")

import getDatafromDatabase
import data_preprocess

def bigram_q_or_a():
    # q
    data1 = getDatafromDatabase.getdata('select Title,Body from q', [])
    #print(len(data1))

    #a
    data2 = getDatafromDatabase.getdata('select Body from a', [])
    #print(len(data2))


    #1）预处理数据
    #   去除code内容、html标签、邮箱、标点、停用词
    #   提取词干
    train = []
    for post in data1:
        #title+body
        temp = data_preprocess.preprocess(post[0])+data_preprocess.preprocess(post[1])
        train.append(temp)

    for post in data2:
        #body
        temp = data_preprocess.preprocess(post[0])
        train.append(temp)

    #print(len(train))

    #2）构建二元模型
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(train, min_count=5, threshold=1000)  # higher threshold fewer phrases.

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)


    def make_bigram(train):
        return [bigram_mod[doc] for doc in train]

    bigram_data = make_bigram(train)
    #print(bigram_data)

    return bigram_data

def bigram_q():
    #q
    data = getDatafromDatabase.getdata('select Title,Body from `q`', [])

    # 1）预处理数据
    #   去除code内容、html标签、邮箱、标点、停用词
    #   提取词干
    train = []
    for i in range(len(data)):
        temp = data_preprocess.preprocess(data[i][0])+data_preprocess.preprocess(data[i][1])
        train.append(temp)


    #2）构建二元模型
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(train, min_count=5, threshold=1000)  # higher threshold fewer phrases.

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)

    bigram_data = [bigram_mod[doc] for doc in train]

    return bigram_data



def bigram_q_and_a():
    #q&a
    data = getDatafromDatabase.getdata('select QId,Title,QBody,ABody from `q&a`', [])

    # 1）预处理数据
    #   去除code内容、html标签、邮箱、标点、停用词
    #   提取词干
    train = []
    for i in range(len(data)):
        temp = data_preprocess.preprocess(data[i][1])+data_preprocess.preprocess(data[i][2])+data_preprocess.preprocess(data[i][3])
        train.append(temp)

    #print(len(train))

    #2）构建二元模型
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(train, min_count=5, threshold=1000)  # higher threshold fewer phrases.

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)

    bigram_data = [bigram_mod[doc] for doc in train]

    return bigram_data


def bigram_q_with_a(): #有接受的答案则带答案，否则不带答案 3520个
    #q&a
    data = getDatafromDatabase.getdata('select Id,Title,Body,acceptAnswerBody from `q`', [])

    # 1）预处理数据
    #   去除code内容、html标签、邮箱、标点、停用词
    #   提取词干
    train = []

    for i in range(len(data)):
        if data[i][3] is None:
            temp = data_preprocess.preprocess(data[i][1])+data_preprocess.preprocess(data[i][2])
        else:
            temp = data_preprocess.preprocess(data[i][1])+data_preprocess.preprocess(data[i][2])+data_preprocess.preprocess(data[i][3])
        train.append(temp)

    #print(len(train))

    #2）构建二元模型
    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(train, min_count=5, threshold=1000)  # higher threshold fewer phrases.

    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)

    bigram_data = [bigram_mod[doc] for doc in train]
    print(len(bigram_data))

    return bigram_data



# Create Corpus
#texts = bigram_data
#print("corpus:",texts)
#[['im', 'look', 'way', 'auto'...],[...]...]

# Create Dictionary
#id2word = corpora.Dictionary(bigram_data)
#print("Dictionary:",id2word[0],id2word[4])
#Dictionary: auto fine

# Term Document Frequency
#corpus = [id2word.doc2bow(text) for text in texts]
#print("Term Document Frequency",corpus)
#[[(0, 1), (1, 1), (2, 1), (3, 1)...],[...]...]