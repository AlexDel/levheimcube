def CountFearFeatures_emphasizers(tokens=[]):
    emphasizersTokens = ['очень', 'очень-очень', 'довольно-таки', 'достаточно', 'вполне', 'неслабо', 'настолько',  'сильно', 'невероятно', 'фантастически', 'удивительно', 'особенно', 'чертовски', 'столь', 'прямо-таки', 'необычайно', 'черезвычайно', 'поистине', 'чрезвычайно', 'супер', 'исключительно', 'шибко', 'весьма', 'слишком', 'чересчур', 'чрезмерно', 'крайне', 'изрядно']

    counter = 0

    if len(tokens) == 0:
        return 0

    for i in range(len(tokens)):
        if tokens[i] in emphasizersTokens:
            counter +=1

    return counter / len(tokens)
