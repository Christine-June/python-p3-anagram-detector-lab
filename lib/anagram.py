# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        result = []
        for candidate in word_list:
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word:
                result.append(candidate)
        return result
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))

