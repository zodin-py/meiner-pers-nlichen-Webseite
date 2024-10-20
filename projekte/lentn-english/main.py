import random, time, os

WORDS = {
    "Absence": "The lack or unavailability of something or someone.",
    "Approval": "Having a positive opinion of something or someone.",
    "Answer": "The response or receipt to a phone call, question, or letter.",
    "Attention": "Noticing or recognizing something of interest.",
    "Amount": "A mass or a collection of something",
    "Borrow":
    "To take something with the intention of returning it after a period of time.",
    "Baffle": "An event or thing that is a mystery and confuses.",
    "Ban": "An act prohibited by social pressure or law.",
    "Banish": "Expel from the situation, often done officially.",
    "Banter": "Conversation that is teasing and playful.",
    "Characteristic":
    "referring to features that are typical to the person, place, or thing.",
    "Cars": "Four-wheeled vehicles used for traveling.",
    "Care": "extra responsibility and attention.",
    "Chip": "a small and thin piece of a larger item.",
    "Cease": "to eventually stop existing.",
    "Dialogue": "A conversation between two or more people.",
    "Decisive": "a person who can make decisions promptly.",
}


def mein():
  # dictionary with the words and definitions
  while True:
    massege = '''1. Review random word
2. Test yourself
3. Exit
'''
    print(massege)
    choice = input("Enter your choice: ")

    if choice == "1":
      review_random_word(WORDS)
      print("-" * 30)

    elif choice == "2":
      test_yourself(WORDS)

    elif choice == "3":
      print("-" * 30)
      break

    else:
      print("Invald choice please Enter a number berwen 1 and 3.")


def review_random_word(words):
  random_word = random.choice(list(words.keys()))
  print(f"Word:{random_word} ")
  print(f"Definition: {words[random_word]}")


def test_yourself(words):

  attempt = 3
  random_word = random.choice(list(words.keys()))
  print(f"Definition: {words[random_word]}")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for _ in range(3):

    gauss = input("Enter the word: ")
    if gauss.title() == random_word:
      print("correct")
      break
    else:
      attempt -= 1
      if attempt == 0:
        print("Incorrect answer, you have no more attempts left.")
        print("-" * 30)
        print(f"The word was: {random_word}")
        print("Better luck next time!")
      else:
        print(
            f"Incorrect answer, you have {attempt} attempt{'s' if attempt != 1 else ''} left."
        )


mein()
