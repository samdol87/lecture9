'''
SI 507 W18 homework 3: Classes and Inheritance

Your discussion section: Section 8
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  def __init__(self, name="Coco", boredom = 6, hunger = 10):
    self.name = name
    self.hunger = hunger
    self.boredom = boredom

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state

coco = Explore_pet("Coco", 7, 9)
brian = Explore_pet("Brian", 5, 11)
print(coco)
print(brian)

#your code begins here . . .

'''
Task B
'''
#add your codes inside of the Pet class
class Pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  species = ["dog", "cat", "others"]
  words_list = ["hello", "bye", "sit", "bark", "run!", "stand up!"]

  def __init__(self, name="Coco", boredom = 6, hunger = 10, species = "dog"):
    self.name = name
    self.hunger = hunger
    self.boredom = boredom
    self.species = species

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state

  def clock_tick(self):
    self.hunger += 2
    self.boredom += 2

  def say(self):
    speak = "I know how to say"
    for i in self.words_list:
      print(speak, i)

  def teach(self, word):
    self.new_word = word
    self.words_list.append(self.new_word)
    if self.boredom < self.boredom_decrement:
      self.boredom = 0
    else:
      self.boredom = self.boredom + self.boredom_decrement

  def feed(self):
    if self.hunger < self.hunger_decrement:
      self.hunger = 0
    else:
      self.hunger = self.hunger + self.hunger_decrement

'''
Task C
'''

class Pet:
  boredom_decrement = -4
  hunger_decrement = -4
  boredom_threshold = 6
  hunger_threshold = 10
  words_list = ["hello", "bye", "sit", "bark", "run!", "stand up!"]

  def __init__(self, name="Coco", boredom = 6, hunger = 10):
    self.name = name
    self.hunger = hunger
    self.boredom = boredom

  def mood(self):
    if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
        return "happy"
    elif self.hunger > self.hunger_threshold:
        return "hungry"
    else:
        return "bored"

  def __str__(self):
    state = "I'm " + self.name + '. '
    state += 'I feel ' + self.mood() + '. '
    if self.mood() == 'hungry':
      state += 'Feed me.'
    if self.mood() == 'bored':
      state += 'You can teach me new words.'
    return state

  def clock_tick(self):
    self.hunger += 2
    self.boredom += 2

  def say(self):
    speak = "I know how to say"
    for i in self.words_list:
      print(speak, i)

  def teach(self, word):
    self.new_word = word
    self.words_list.append(self.new_word)
    if self.boredom < self.boredom_decrement:
      self.boredom = 0
    else:
      self.boredom = self.boredom + self.boredom_decrement

  def feed(self):
    if self.hunger < self.hunger_decrement:
      self.hunger = 0
    else:
      self.hunger = self.hunger + self.hunger_decrement

  def hi(self):
    rand_num = randrange(0, len(self.words_list))
    print(self.words_list[rand_num])


def teaching_session(my_pet, new_words = []):
  for i in new_words:
    if i not in my_pet.words_list:
      my_pet.teach(i)
  my_pet.hi()
  print(my_pet)
  if my_pet.hunger > my_pet.hunger_threshold:
    my_pet.feed()
  my_pet.clock_tick()

teddy = Pet("teddy", 10, 16)
teaching_session(teddy, ["I am sleepy", "You are the best", "I love you, too"])


  #your code begins here . . .



#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
#your code begins here . . .

class Dog(Pet):

  def __str__(self):
    state = "I'm " + self.name + 'arrrf!'
    state += 'I feel ' + self.mood() + 'arrrf!'
    if self.mood() == 'hungry':
	  state += 'Feed me. arrrf!'
    if self.mood() == 'bored':
      state += 'You can teach me new words. arrrf!'
    return state

class Cat(Pet):

  def __init__(self, name="Coco", meow_count = 0):
    self.name = name
    self.meow_count = meow_count

  def hi(self):
    rand_num2 = randrange(0, len(self.words_list))
    print(self.words_list[rand_num2]*self.meow_count)


'''
Task B: Poodle
'''
#your code begins here . . .

class Poodle(Dog):

  def dance(self):
    print("Dancing in circles like poodles do!")

  def say(self):
    print("Dancing in circles like poodles do!")
    speak = "I know how to say"
    for i in self.words_list:
      print(speak, i)

petty = Poodle("Petty")
petty.say()

pororo = Cat("Pororo", 10)
pororo.hi()
