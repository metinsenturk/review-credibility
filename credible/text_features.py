import re
import json
import statistics
import spacy
from textblob import TextBlob
from langdetect import detect

nlp = spacy.load("en_core_web_lg")


class Nlp(object):
    def __init__(self, text, nlp_object, load_spacy=False):
        """
        NLP Wrapper to extract features from a text.

        text: a sample of text
        nlp_object: spacy nlp object
        load_spacy: a switch to load spacy  
        """

        if load_spacy:
            nlp_object = spacy.load("en_core_web_lg")

        self.text = text
        self.doc = nlp_object(text)
        self.blob = TextBlob(text=text)

        self.noun_phrases = self.blob.noun_phrases
        self.sents = [i for i in self.doc.sents]
        self.words = [token.text for token in self.doc 
            if token.is_stop != True and token.is_punct != True]

    def validate_text(self):
        text = self.text
        regex_email = re.compile(r'[^@]+@[^@]+\.[^@]+', re.IGNORECASE)
        regex_url = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        check_length = len(text) > 50
        check_url = re.match(regex_url, text) is None
        check_email = re.match(regex_email, text) is None

        if check_email and check_url and check_length:
            return True
        else:
            return False
        
    def detect_language(self):
        try:
            return detect(self.text)
        except:
            return 'no'

    def sentiment_polarity(self):
        return self.blob.polarity

    def sentiment_subjectivity(self):
        return self.blob.subjectivity

    def count_sentences(self):
        return len(self.sents)

    def count_words(self):
        return len(self.words)

    def count_chars(self):
        raise Exception('NotImplementedError')

    def count_noun_phrases(self):
        return len(self.noun_phrases)

    def count_pos(self):
        counts_dict = self.doc.count_by(spacy.attrs.IDS['POS'])

        result = []
        for pos, count in counts_dict.items():
            tag = self.doc.vocab[pos].text
            result.append({tag: count})
        return json.dumps(result)

    def avg_len_sentences(self):
        return statistics.mean(len(i) for i in self.doc.sents)

    def avg_len_words(self):
        return statistics.mean(len(i) for i in self.words)

    def ratio_lexical(self):
        """
        lexicality score of a text. the higher the better.
        """
        return len(set(self.words)) / len(self.words)

    def ratio_content(self):
        """
        content amount of a text. the higher the better.
        """
        stop_count = len(list(i for i in self.doc if i.is_stop))
        return (len(self.words) - stop_count) / len(self.words)

    def get_noun_phrases(self):
        return json.dumps(list(self.noun_phrases))

    def __repr__(self):
        return '<Nlp lang={} sc: {} wc: {} rl: {} text: {}>'.format(
            self.detect_language(),
            self.count_sentences(),
            self.count_words(),
            self.ratio_lexical(),
            self.text[:20] + '...'
        )
