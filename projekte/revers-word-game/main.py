# importing the random and time modules
import random
import time

# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into',
'could',
 'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like',
'then',
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find',
'also',
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through',
'long',
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because',
'good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world',
'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show',
'house', 'both',
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
'move', 'thing',
'general', 'school', 'never', 'same', 'another', 'begin', 'while',
'number', 'part',
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child',
'small', 'since',
'against', 'late', 'home', 'interest', 'large', 'person', 'open',
'public', 'follow',
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern',
'around',
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead',
'system',
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]
print("You welcam to the revers word game!")
print("-" * 20)
# choose a random index
random_word = random.randint(0,len(words) -1)

# choose a word from the list
word = words[random_word]

# make a list from a string
word_list = list(word)

# reverse the list
word_list.reverse()

# make a string from the list
word_str = "".join(word_list)

# print the reserved word
print(f"The revers word is: {word_str}")
print("-" * 20)

# record the start time
start_time = time.time()

# make the guess
guess = input("The word is: ")
print("-" * 20)
# record the end time
end_tim = time.time()
# calculate the answer time
time = (end_tim - start_time)
# check the guess
if word == guess and time < 5:
 result = "You won!"
else:
  if time < 5:
    print("You took too long!")
  if word != guess:
    print("Wrong word!")
    
  print("you lost")


