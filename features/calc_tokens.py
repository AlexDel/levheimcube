
def calc_tokens_feature(targetTokens=[]):
    def calc_tokens_ratio(textTokens=[]):
        counter = 0

        if len(textTokens) == 0:
            return 0

        for token in textTokens:
            if token in targetTokens:
                counter +=1

        return counter / len(textTokens)

    return calc_tokens_ratio
