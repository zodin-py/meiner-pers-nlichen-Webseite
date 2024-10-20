import random, string

# invild a funchin bassword with choice complex 
def password(length=8, complex=False):
  if complex:
    chare = string.ascii_letters + string.digits + string.punctuation
    random_chare = "".join(random.choice(chare) for _ in range(length // 2))
    spicel_chare = input("waht is your spicel chares: ")
    return random_chare + spicel_chare

  else:
    chare = string.ascii_letters + string.digits + string.punctuation    
    return "".join(random.choice(chare) for _ in range(length))


choic = input("Do you want to specify your password length:(y/n)")
if choic == "y":
  length = int(input("Specify the length of the password: ")) 
else:
  length = 8

  
print(password(length, True))



