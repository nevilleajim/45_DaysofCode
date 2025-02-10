# Word Counter Project

def wordCounterOccurence(sentence):
      wordCounts = {}
      words = sentence.split()

      for word in words:
            word = word.lower()
            if word in wordCounts:
                  wordCounts[word] += 1
            else:
                  wordCounts[word] = 1
      return wordCounts

def main():
      sentence = input("Enter a sentence to count word occurrence: ")
      wordCounts = wordCounterOccurence(sentence)

      for word, count in sorted(wordCounts.items()):
            print(word + " : ", count)

if __name__ == "__main__":
      main()