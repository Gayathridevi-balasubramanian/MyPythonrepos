class wordSet:
    def __init__(self):
        self.words = set()

    def addText(self , text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(self, text):
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','')
        return text.lower()
    
wordSet = wordSet()
wordSet.addText('Hi, I\'m gayathri! Here is a sentence I want to add!')
print(wordSet.words)

class wordSet:
    def __init__(self):
        self.words = set()

    def addText(self , text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)
            
    @staticmethod
    def cleanText(text):
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','')
        return text.lower()
    
wordSet = wordSet()
wordSet.addText('Hi, I\'m gayathri! Here is a sentence I want to add!')
print(wordSet.words)

# static methods
class wordSet:
    def __init__(self):
        self.words = set()

    def addText(self , text):
        text = wordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    @staticmethod
    # static method doesnot need the self parameter to be passed
    def cleanText(text):
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','')
        return text.lower()
    
wordSet = wordSet()
wordSet.addText('Hi, I\'m gayathri! Here is a sentence I want to add!')
print(wordSet.words)

#static attributes
class wordSet:
    removePunctuation = ['!',',','.','\'']
    def __init__(self):
        self.words = set()

    def addText(self , text):
        text = wordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    @staticmethod
    # static method doesnot need the self parameter to be passed
    def cleanText(text):
        for punc in wordSet.removePunctuation:
            return text.replace(punc,'')
        return text.lower()
    
wordSet = wordSet()
wordSet.addText('Hi, I\'m gayathri! Here is a sentence I want to add!')
print(wordSet.words)

