from happytransformer import HappyTextToText, TTSettings

# text similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# grammar checker
# return True if text is grammatically correct
# if false, return False and corrected text


class GrammarChecker:
    def __init__(self):
        self.happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
        self.args = TTSettings(num_beams=5, min_length=1)

        # Preprocess the input strings
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def grammar_check(self, text):
        result = self.happy_tt.generate_text("grammar: " + text, args=self.args)

        # check if original text is equal to corrected text
        orig_text = text.split(" ")
        orig_text = [x.lower() for x in orig_text]  # lower case

        corr_text = result.text.split(" ")
        import string

        table = str.maketrans("", "", string.punctuation)
        corr_text = [w.translate(table) for w in corr_text]  # remove any punc
        corr_text = [x.lower() for x in corr_text]  # lower case items in list

        # if not equal, return corrected text

        correct = corr_text == orig_text
        # print(corr_text)
        return result.text, correct

    def preprocess_string(self, string):
        words = word_tokenize(string.lower())
        words = [
            word for word in words if word.isalpha() and word not in self.stop_words
        ]
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return " ".join(words)

    def similarity_score(self, orig, sug):
        processed_string1 = self.preprocess_string(orig)
        processed_string2 = self.preprocess_string(sug)
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(
            [processed_string1, processed_string2]
        )
        similarity_score = cosine_similarity(tfidf_matrix)[0][1]
        return similarity_score

    def predict_func(self, original_sentence, suggested_sentence):
        # pass in function
        print(original_sentence, suggested_sentence)
        corrected_sentence, correct = self.grammar_check(suggested_sentence)

        sentence = [corrected_sentence, suggested_sentence]

        if correct == True:
            n = 1  # use suggested sentence if grammar is correct
        else:
            n = 0  # use corrected sentence if grammar is incorrect

        d = {
            "original_sentence": original_sentence,
            "suggested_sentence": suggested_sentence,
            "corrected_sentence": corrected_sentence,
            "grammatically correct": correct,
            "sentence_similarity": self.similarity_score(
                sentence[n], original_sentence
            ),  # similiraty score between original and grammatically correct sentence
        }

        # print(d)
        return [d]
