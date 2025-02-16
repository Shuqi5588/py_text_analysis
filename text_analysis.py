class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # You will store the provided 'text' as an instance variable.
    def __init__(self, text):
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
        
    def freqAll(self):
        wordList = self.fmtText.split(' ')

        freqMap = {}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap
        
    def freqOf(self,word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0

analyzed = TextAnalyzer(givenstring)
freqMap = analyzed.freqAll()
word = "lorem"
frequency = analyzed.freqOf(word)
print("Formatted Text:", analyzed.fmtText)
print("freqAll Text:", freqMap)
print("The word", word,"appears",frequency,"times.")
