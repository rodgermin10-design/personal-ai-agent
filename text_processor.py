import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Загрузка необходимых данных NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('russian'))
    
    def clean_text(self, text):
        """Очистить текст"""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Удалить спецсимволы
        return text.strip()
    
    def tokenize(self, text):
        """Разбить текст на токены"""
        return word_tokenize(text)
    
    def remove_stopwords(self, tokens):
        """Удалить стоп-слова"""
        return [word for word in tokens if word not in self.stop_words]
    
    def extract_keywords(self, text):
        """Извлечь ключевые слова"""
        tokens = self.tokenize(self.clean_text(text))
        keywords = self.remove_stopwords(tokens)
        return keywords
    
    def split_sentences(self, text):
        """Разбить текст на предложения"""
        return sent_tokenize(text)
    
    def analyze_sentiment(self, text):
        """Простой анализ тональности"""
        positive_words = ['хороший', 'отлично', 'спасибо', 'любимый', 'прекрасно']
        negative_words = ['плохо', 'ужасно', 'ненавижу', 'скучно', 'грусть']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
