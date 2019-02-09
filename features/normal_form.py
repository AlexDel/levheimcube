import pymorphy2

morph = pymorphy2.MorphAnalyzer()
p = morph.parse('они')[0]
lemma = p.normal_form
print(lemma)
print(p.tag)

if 'что-то'.find('-то') != -1:
    print('ДА')