from nltk import  bigrams
import re

def CountFearFeatures_talk(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token == 'говорить':
            counter +=1

    return counter / len(tokens)

def CountFearFeatures_they_talk(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    for token in tokens:
        if token == 'говорят':
            counter +=1

    return counter / len(tokens)

def CountFearFeatures_colon_talk(punctuation_tokens=[]):
    talkTokens = ['говорить:','говорю:','говорит:','говорим:','говорят:','говорите:','говорил:','говорила:','говорило:','говорили:']
    counter = 0

    if len(punctuation_tokens) == 0:
        return 0

    for token in punctuation_tokens:
        if token in talkTokens:
            counter += 1

    return counter / len(punctuation_tokens)

def CountFearFeatures_doctor_talk(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    tokens_pairs = bigrams(tokens)

    for first_token, next_token in tokens_pairs:
        if first_token == 'врач' and next_token in ('говорить','сказать'):
            counter += 1

    return counter / len(tokens)

def CountFearFeatures_what_talk(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    tokens_pairs = bigrams(tokens)

    for first_token, next_token in tokens_pairs:
        if first_token == 'говорить' and next_token == 'что':
            counter += 1

    return counter / len(tokens)

def CountFearFeatures_toldMe(punctuation_tokens=[]):
    counter = 0

    if len(punctuation_tokens) == 0:
        return 0

    tokens_pairs = bigrams(punctuation_tokens)

    for first_token, next_token in tokens_pairs:
        first_token = re.sub(r'[^\w\s]','',first_token)
        next_token = re.sub(r'[^\w\s]','',next_token)
        if first_token.lower() == 'мне' and next_token.lower() == 'говорили':
            counter += 1

    return counter / len(punctuation_tokens)

def CountFearFeatures_talk_myself(tokens=[]):
    counter = 0

    if len(tokens) == 0:
        return 0

    tokens_pairs = bigrams(tokens)

    for first_token, next_token in tokens_pairs:
        if first_token == 'себя' and next_token == 'говорить':
            counter += 1

    return counter / len(tokens)