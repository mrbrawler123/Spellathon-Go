import nltk
import time
nltk.download("words")
nltk.download("wordnet")
print("\033[2J\033[H")
print("SPELLATHON GO")
time.sleep(3)
from itertools import permutations
print("This is where you can form words. First enter a compulsory letter. Then you can enter other letters which can be in the word. Enter a minimum of four letters in total. I will tell you all the possible words that can be made. The words will only have repeated letters, if you enter them.")
time.sleep(1)
from nltk.corpus import words
from nltk.corpus import wordnet
words_list = words.words() + list(wordnet.words())
mean = input("Enter the compulsory letters (Comma Separated): ")
man = mean.replace(" ", "")
compulsory_letters_list1 = man.split(",")
compulsory_letters_list = []
for ranword in compulsory_letters_list1:
	ranword2 = ranword.lower()
	compulsory_letters_list.append(ranword2)
time.sleep(1)
p = input("Enter the optional letters (Comma Separated): ")
s = p.replace(" ", "")
optional_letters1 = s.split(",")
optional_letters = []
for ranword3 in optional_letters1:
	ranword4 = ranword3.lower()
	optional_letters.append(ranword4)
final_words = []
final_letters = compulsory_letters_list + optional_letters
original_permutations = []
var = 0
for t in range(len(final_letters) - 3):
	original_permutations = list(permutations(final_letters, t + 4)) + original_permutations
word_set = set(words_list)
for i in original_permutations:
	var = 0
	for xp in compulsory_letters_list:
		if xp in i:
			var = var + 1
	if var != len(compulsory_letters_list):
		continue
	j = "".join(i)
	if j in word_set:
		final_words.append(j)
if len(final_words) == 0:
	print("No words can be formed.")
else:
	final_words = list(dict.fromkeys(final_words))
	print(f"Here are the words that can be formed: {final_words}")