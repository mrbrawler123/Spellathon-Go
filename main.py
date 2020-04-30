import nltk
import time
nltk.download("words")
print("\033[2J\033[H")
print("The Diamonds Presents...")
time.sleep(3)
print("SPELLATHON GO")
time.sleep(3)
from itertools import permutations
print("This is where you can form words. First enter a compulsory letter. Then you can enter other letters which can be in the word. Atleast enter three of them. I will tell you all the possible words that can be made. The words will only have repeated letters, if you enter them. ")
time.sleep(1)
from nltk.corpus import words
words_list = words.words()
compulsory_letter = list(input("Enter the compulsory letter: "))
time.sleep(1)
s = input("Enter the optional letters (Comma Separated): ")
s.strip()
optional_letters = s.split(",")
final_words = []
final_letters = compulsory_letter + optional_letters
c = "".join(compulsory_letter)
print("This may take a while...")
for t in range(len(final_letters)):
  p = permutations(final_letters, t + 4)
  for i in p:
    for x in words_list:
      if len(x) < 4:
        continue
      if len(x) > len(final_letters):
        continue
      if c not in x:  
        continue
      if i == x:
        final_words.append(x)
        break 
if len(final_words) == 0:
  print("No words can be formed.")
else:
  print(f"Here are the words that can be formed: {final_words}")