import spacy
nlp = spacy.load("en_core_web_md")

class IdentifyCategory:
    def __init__(self, input_text):
        categories={
            'technical':0,
            'behavioural':0,
            'basic questions':0
        }
        doc = nlp(input_text)
        for key in categories.keys():
            categories[key]=doc.similarity(nlp(key))
        self.category=max_key = max(categories, key=categories.get)
        print(categories)
        print(self.category)

# IdentifyCategory('i have a deep knowledge in technical rounds')

class IdentifyLevel:
    def __init__(self, input_text):
        levels={
            'basic level':0,
            'medium level':0,
            'hard level':0
        }
        doc = nlp(input_text)
        for key in levels.keys():
            levels[key]=doc.similarity(nlp(key))
        self.category=max_key = max(levels, key=levels.get)
        print(levels)
        print(self.category)
# IdentifyLevel('i am at medium level')