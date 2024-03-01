# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
# Word may contain dots '.' where dots can be matched with any letter.
 
# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class WordDictionary:

    def __init__(self):
        self.dictionary = {str:list}

    def addWord(self, word: str) -> None:
        # keys will be the length of the words
        # values will be an array of the words of that length
        # this will simplify search fxn
        if word in self.dictionary[len(word)]:
            print(word + " is already in the dictionary")
        else:
            self.dictionary[len(word)].append(word)

    def search(self, word: str) -> bool:
        # will need to use regEx for this
        # will go with less optimized soln. for now
        # determine the length of the word first
        lengthOfSearch = len(word)
        # turned into list to compare each character
        arrOfWord = list(word)
        # we could also split into two situations
        # 1. the search contains '.'
        # 2. the search is a single word
        # need to finish logic at a later time
        for wordInDict in self.dictionary[lengthOfSearch]:
            arrWordInDict = list(wordInDict)
            while i in range(lengthOfSearch - 1):
                if arrOfWord[i] == '.':
                    continue
                # elif arrOfWord[i] != arrWordInDict:

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)