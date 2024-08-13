import nltk
import string
import re
import inflect

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def normalize_text(text):
    """
    Fix and normalize the input text by addressing common formatting issues.

    Parameters:
    text (str): The input text string to be fixed.

    Returns:
    str: The fixed text string.
    """
    # Remove incorrect spaces within words
    text = re.sub(r'\b(\w)\s+(\w)\b', r'\1\2', text) r
    
    # Remove incorrect spaces inside parentheses
    text = re.sub(r'\(\s*(\w+)\s*\)', r'(\1)', text)
    
    # Normalize spaces 
    text = remove_multiple_spaces(text)
    
    # Correct space before punctuation
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)

    return text



def remove_html_tags(text):
    """
    Removes HTML tags from the text.
    
    Parameters:
    text (str): The input text containing HTML tags.
    
    Returns:
    str: The text with HTML tags removed.
    """
    return re.sub(r'<[^>]+>', '', text)


def convert_emojis_to_words(text):
    """
    Converts emojis to words.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with emojis converted to words.
    """
    return emoji.demojize(text)


def convert_emoticons_to_words(text):
    """
    Converts common emoticons to words.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with emoticons converted to words.
    """
    emoticons_dict = {
        ':)': 'smile',
        ':(': 'sad',
        ':D': 'laugh',
        ';)': 'wink',
        ':-)': 'smile',
        ':-(': 'sad',
        ':-D': 'laugh',
        ';-)': 'wink'
    }
    
    words = text.split()
    converted_words = [emoticons_dict.get(word, word) for word in words]
    return ' '.join(converted_words)


def remove_emojis(text):
    """
    Removes emojis from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with emojis removed.
    """
    return re.sub(r'[^\w\s,]', '', text)


def stem_text(text):
    """
    Applies stemming to the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The stemmed text.
    """
    stemmer = PorterStemmer()
    words = text.split()
    return ' '.join([stemmer.stem(word) for word in words])


def remove_rare_words(text, threshold=0.01):
    """
    Removes words that appear too rarely in the text.
    
    Parameters:
    text (str): The input text.
    threshold (float): The frequency threshold; words with a frequency lower than this will be removed.
    
    Returns:
    str: The text with rare words removed.
    """
    words = text.split()
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    
    rare_words = {word for word, count in word_counts.items() if count / total_words < threshold}
    
    return ' '.join([word for word in words if word not in rare_words])


def remove_frequent_words(text, threshold=0.01):
    """
    Removes words that appear too frequently in the text.
    
    Parameters:
    text (str): The input text.
    threshold (float): The frequency threshold; words with a frequency higher than this will be removed.
    
    Returns:
    str: The text with frequent words removed.
    """
    words = text.split()
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    
    frequent_words = {word for word, count in word_counts.items() if count / total_words > threshold}
    
    return ' '.join([word for word in words if word not in frequent_words])


def eliminate_handles(text):
    """
    Removes handles (e.g., Twitter handles starting with '@') from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with handles removed.
    """
    return re.sub(r'@\w+', '', text)

#####???
def named_entity_recognition(text):
    """
    Performs Named Entity Recognition (NER) on the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    nltk.Tree: A tree structure representing the named entities.
    """
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    return ne_chunk(pos_tags)


def correct_spelling(tokens):
    """
    Corrects spelling using a spell checker.
    
    Parameters:
    tokens (list): A list of tokens (words) that may contain repeated characters.
    
    Returns:
    list: A list of corrected tokens.
    """
    spell = SpellChecker()
    corrected_tokens = [spell.correction(token) if re.search(r'(.)\1', token) else token for token in tokens]
    return corrected_tokens


def reduce_excessive_repetition(text):
    """
    Reduces excessive character repetition to a maximum of two occurrences.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with excessive character repetition reduced.
    """
    return re.sub(r'(.)\1{2,}', r'\1\1', text)


def remove_special_characters(text):
    """
    Removes special characters from the text, keeping only words, spaces, and basic punctuation (.,?!).
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with special characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9\s,.?!]', '', text)


def remove_urls(text):
    """
    Removes URLs from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with URLs removed.
    """
    return re.sub(r'https?://\S+|www\.\S+', '', text)




def lemmatize_text(text):
    """
    Lemmatizes words in the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with words lemmatized.
    """
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_text)


def text_lowercase(text):
    """
    Converts all characters in the text to lowercase.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text converted to lowercase.
    """
    return text.lower()




def remove_numbers(text):
    """
    Removes all numbers from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with numbers removed.
    """
    return re.sub(r'\d+', '', text)


    import string

def remove_punctuation(text):
    """
    Removes all punctuation from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with punctuation removed.
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_whitespace(text):
    """
    Removes leading, trailing, and extra internal whitespace from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with unnecessary whitespace removed.
    """
    return " ".join(text.split())



def convert_number_to_text(text):
    """
    Converts numerical digits in the text to words.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with numbers converted to words.
    """
    p = inflect.engine()
    words = text.split()
    converted_words = [p.number_to_words(word) if word.isdigit() else word for word in words]
    return ' '.join(converted_words)



def remove_stopwords(text, language="english"):
    """
    Removes stopwords from the text.
    
    Parameters:
    text (str): The input text.
    language (str): The language of stopwords to remove.
    
    Returns:
    str: The text with stopwords removed.
    """
    stop_words = set(stopwords.words(language))
    words = word_tokenize(text)
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_text)



def remove_non_ascii(text):
    """
    Removes non-ASCII characters from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with non-ASCII characters removed.
    """
    return re.sub(r'[^\x00-\x7F]+', '', text)




def expand_contractions(text):
    """
    Expands contractions in the text (e.g., don't -> do not).
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with contractions expanded.
    """
    return contractions.fix(text)


def remove_extra_line_breaks(text):
    """
    Removes extra line breaks from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with extra line breaks removed.
    """
    return text.replace('\n', ' ').replace('\r', '').strip()



def remove_multiple_spaces(text):
    """
    Reduces multiple spaces in the text to a single space.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with multiple spaces reduced to a single space.
    """
    return re.sub(r'\s+', ' ', text).strip()


def remove_digits(text):
    """
    Removes all numeric digits from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with digits removed.
    """
    return re.sub(r'\d+', '', text)


import html

def remove_html_entities(text):
    """
    Removes HTML entities (e.g., &amp;, &lt;) from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with HTML entities removed.
    """
    return html.unescape(text)

import unicodedata

def remove_accented_characters(text):
    """
    Removes accented characters from the text, replacing them with non-accented equivalents.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with accented characters replaced.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')



######??????
def remove_non_printable(text):
    """
    Removes non-printable characters from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with non-printable characters removed.
    """
    return ''.join(c for c in text if c.isprintable())


def remove_currency_symbols(text):
    """
    Removes currency symbols from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with currency symbols removed.
    """
    return re.sub(r'[\$\€\£\¥\₹\¢\₱\₦]', '', text)


def remove_brackets(text):
    """
    Removes brackets and their contents from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with brackets and their contents removed.
    """
    return re.sub(r'\[.*?\]|\(.*?\)|\{.*?\}|\<.*?\>', '', text)



### ???????
def remove_dates(text):
    """
    Removes dates from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with dates removed.
    """
    date_pattern = r'\b(?:\d{1,2}[-/th|st|nd|rd\s]+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[-/\s]?\d{0,4}|\d{4})\b'
    return re.sub(date_pattern, '', text)


def remove_emails(text):
    """
    Removes email addresses from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with email addresses removed.
    """
    return re.sub(r'\S+@\S+', '', text)


def tokenize_words(text):
    """
    Tokenizes the text into words.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    list: A list of word tokens.
    """
    return word_tokenize(text)

def tokenize_sentences(text):
    """
    Tokenizes the text into sentences.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    list: A list of sentence tokens.
    """
    return sent_tokenize(text)


def remove_single_characters(text):
    """
    Removes isolated single characters from the text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    str: The text with isolated single characters removed.
    """
    return re.sub(r'\b\w\b', '', text).strip()
