import nltk

try:
    from nltk.corpus import stopwords
    stop_words = stopwords.words('russian')

except (LookupError, NameError) as e:
    nltk.download('stopwords')

other_stopwords = ['это', 'который', 'тот', 'весь', 'свой', 'наш', 'ещё', 'нея', 'мочь']
stop_words.extend(other_stopwords)


def strip_stopwords(tokens=[]):
    return [t for t in tokens if t not in stop_words]
