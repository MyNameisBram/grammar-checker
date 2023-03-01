from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)


# grammar checker 
# return True if text is grammatically correct
# if false, return False and corrected text

def grammar_check(text):
    result = happy_tt.generate_text("grammar: " + text, args=args)

    # check if original text is equal to corrected text
    orig_text = text.split(" ")
    orig_text = [x.lower() for x in orig_text] # lower case

    corr_text = result.text.split(" ")
    import string
    table = str.maketrans('', '', string.punctuation)
    corr_text = [w.translate(table) for w in corr_text] # remove any punc   
    corr_text = [x.lower() for x in corr_text]  # lower case items in list

    # if not equal, return corrected text

    correct = corr_text == orig_text
    #print(corr_text)
    return result.text, correct


# text similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocess the input strings
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_string(string):
    words = word_tokenize(string.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)


def similarity_score(orig, sug):
    processed_string1 = preprocess_string(orig)
    processed_string2 = preprocess_string(sug)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([processed_string1, processed_string2])
    similarity_score = cosine_similarity(tfidf_matrix)[0][1]
    return similarity_score
