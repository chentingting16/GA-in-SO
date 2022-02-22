import gensim
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import warnings
warnings.filterwarnings("ignore")


def preprocess(corpus):
    #去除code部分
    #html = '\nhhh@qq.com <p>Give haha@qq.com n a <code>DateTime</code> \nrepresenting a person\'s birthday, how do I calculate their age in years?</p>'
    str = re.sub(r'\<code\>([\d\D]*?)\</code\>', repl='',string=corpus)

    #去除html标签
    soup = BeautifulSoup(str, 'html.parser')

    #转换为小写
    str = soup.get_text().lower()

    #去除邮箱
    str = re.sub(r'[0-9a-zA-Z.]+@[0-9a-zA-Z.]+[com|cn]', repl='',string=str)

    # 去除标点  参数说明：r'[^a-zA-Z0-9\s]' 配对的模式，^表示起始位置，\s表示终止位置，[]表示取中间部分，这个的意思是找出除字符串大小写或者数字组成以外的东西，repl表示使用什么进行替换，这里使用''，即直接替换，string表示输入的字符串
    str = re.sub(r'[^a-zA-Z\s]', repl='', string=str)

    #去除文本前后的空格
    str = str.strip()

    tokens = gensim.utils.simple_preprocess(str, deacc=True)  # deacc=True removes punctuations

    #去除停用词
    #tokens = word_tokenize(str)
    stopword = stopwords.words('english')
    stopword.extend(['github', 'action','use','run','actions','runs','uses','used','ran','im','use'])
    result = [i for i in tokens if not i in stopword]

    #词干提取 Porter词干算法（或“ Porter stemmer”）是用于从英语单词中删除较常见的词法和不固定词尾的过程。
    #将词语简化为词干、词根或词形的过程（如 books-book，looked-look）
    # Porter stemmer 并不是要把单词变为规范的那种原来的样子，它只是把很多基于这个单词的变种变为某一种形式！换句话说，它不能保证还原到单词的原本，也就是"created"不一定能还原到"create"，但却可以使"create" 和 "created" ，都得到"creat"。
    stemmer= PorterStemmer()
    r = []
    for word in result:
        r.append(stemmer.stem(word))
    return r


#词形还原
#基于字典的映射。nltk中要求手动注明词性，否则可能会有问题。因此一般先要分词、词性标注，再词性还原。
"""
lemmatizer=WordNetLemmatizer()
r2 = []
for word in result:
    r2.append(lemmatizer.lemmatize(word))
print(r2)
"""

