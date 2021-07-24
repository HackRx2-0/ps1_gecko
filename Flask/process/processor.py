!pip install contractions
!pip install fuzzywuzzy
!pip install TextBlob
!pip install transformers

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import contractions
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('brown')
nltk.download('punkt')
from textblob import TextBlob
from fuzzywuzzy import fuzz
from transformers import pipeline,BertTokenizer, TFBertModel
import joblib
import tensorflow as tf
from scipy.spatial import distance  

"""
# to be run only once
nlp_qa = pipeline('question-answering')
summarizer = pipeline('summarization')
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = TFBertModel.from_pretrained("bert-base-uncased")

joblib.dump(summarizer,"/content/drive/MyDrive/Hackathon/summarizer.joblib")
joblib.dump(nlp_qa,"/content/drive/MyDrive/Hackathon/question_answering.joblib")
model.save_pretrained("/content/drive/MyDrive/Hackathon/Bert_model",save_format="tf")
joblib.dump(tokenizer,"/content/drive/MyDrive/Hackathon/Bert_tokenizer.joblib")
"""


class QueryProcessor:
    def __init__(self):
        try:
            self.summarizer = joblib.load("process/Models/summarizer.joblib")
            self.nlp_qa = joblib.load("process/Models/question_answering.joblib")
            self.model = TFBertModel.from_pretrained("process/Models/Bert_model")
            self.tokenizer = joblib.load("process/Models/Bert_tokenizer.joblib")
        except Exception as e:
            print(e)
        finally:
            self.lem = WordNetLemmatizer()
            
    def generic_preprocessor(self, text):
        text = str(text)
        soup = BeautifulSoup(text)
        text = soup.get_text()
        text = text.encode('ascii', 'ignore')
        text = text.decode()
        text = text.lower()
        text = str(TextBlob(text).correct())
        text = contractions.fix(text)
        # text = ' '.join([word for word in text.split()
        #                  if not word in set(stopwords.words('english'))])
        text = re.sub('[^a-zA-Z]', ' ', text)
        text = ' '.join(text.split())
        # text = self.lem.lemmatize(text)
        return text

    def fuzz_matching(self, quest1, quest2):
        if type(quest1) == list:
            quest1 = " ".join(quest1)
        if type(quest2) == list:
            quest2 = " ".join(quest2)
        quest1 = self.generic_preprocessor(quest1)
        quest2 = self.generic_preprocessor(quest2)
        return fuzz.partial_ratio(quest1, quest2)

    def keyword_extraction(self, text):
        return list(TextBlob(text).noun_phrases)

    def question_answering(self, content, question, rec=False):
        if rec == False and len(content.split(" ")) < 10:
            return " "
        elif rec == True and len(content) < 10:
            return (0, " ")

        elif rec == False and 10 < len(content.split(" ")) < 500:
            return self.nlp_qa(context=content, question=question)["answer"]

        elif rec == True and 10 < len(content) < 500:
            content = " ".join(content)
            answer = self.nlp_qa(context=content, question=question)
            return (round(answer["score"], 3), answer["answer"])

        else:
            content = content.split(" ")
            # split on basis of senetnce
            content = [content[i:i+499] for i in range(0, len(content), 499)]
            content = [self.question_answering(
                i, question, rec=True) for i in content]
            possible_answers = sorted(
                content, key=lambda x: x[0], reverse=True)
            if len(possible_answers) == 1:
                return possible_answers[0][1]
            else:
                if possible_answers[0][0] == possible_answers[1][0]:
                    return possible_answers[0][1]
                elif 0 < ((possible_answers[0][0] - possible_answers[1][0])/possible_answers[1][0]) < 0.05:
                    return possible_answers[0][1] + " | " + possible_answers[1][1]
                else:
                    return possible_answers[0][1]

    def summarization(self, text):
        if type(text) == str:
            if len(text.split(" ")) < 10:
                return text
            if len(text.split(" ")) < 500:
                return self.summarizer(text)[0]["summary_text"]
            else:
                text = text.split(" ")
                # split on basis of sentence
                text = [text[i:499] for i in range(0, len(text), 499)]
                text = [self.summarization(i) for i in text]
                # can be improved with fuzzy match from list of summarized don't chose text with higher similarity to other
                return " ".join(text)
        else:
            if len(text) < 10:
                return " ".join(text)
            text = " ".join(text)
            return self.summarizer(text)[0]["summary_text"]

    def semantic_search(self,text1, text2):
        inputs1 = self.tokenizer(
            [text1], add_special_tokens=True, return_tensors="tf")
        inputs2 = self.tokenizer(
            [text2], add_special_tokens=True, return_tensors="tf")
        output1 = self.model(inputs1)[-1].numpy()
        output2 = self.model(inputs2)[-1].numpy()
        return (1 - distance.cosine(output1, output2))*100

"""
Q = QueryProcessor()
Q.generic_preprocessor("Hello, how are yuo?")
"""
