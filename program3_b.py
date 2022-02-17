class SentenceReverser:
    vowels=["a", "e", "i", "o", "u"]

    def __init__(self, sentence):
        self.sentence = sentence
        self.reverse_sentence()

    def reverse_sentence(self):
        self.reversedSentence = " ".join(reversed(self.sentence.split()))

    def get_reverse_sentence(self):
        return self.reversedSentence

    def get_vowel_count(self):
        self.vowel_count = sum(s in self.vowels for s in self.sentence.lower())
        return self.vowel_count

def main():
    items=[]
    for i in range(3):
        st = input("Enter phrase: ")
        if st!="":
            sentence = SentenceReverser(st.strip())
            items.append(sentence)

    sortedItems = sorted(items, key=lambda item:item.get_vowel_count(), reverse=True)

    for i in range (len(sortedItems)):
        print("Reversed Sentence: ", sortedItems[i].reversedSentence, " Frequency: ", sortedItems[i].vowel_count)


main()
