# https://www.codecademy.com/courses/learn-intermediate-python-3/projects/int-python-aishas-greetings
# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, receiver):
  #Q2
  card_file = open(card_type, 'r')
  order = open(f"{sender_name}_generic.txt", 'w')
  try: #Q3
    order.write(f"Dear {receiver}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {sender_name} \n")
    yield order
  finally: #Q4
    order.close()
    card_file.close()

# Q5
with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as order1:
  print('Card Generated! \n')

# Q6
with open('Mwenda_generic.txt', 'r') as mwenda:
  print(mwenda.read())

# Q7 Q8
class Personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file = open(f"{sender}_personalized.txt", 'w')
# Q9
  def __enter__(self):
    self.file.write(f"Dear {self.receiver}, \n \n")
    return self.file
  # Q10
  def __exit__(self, exc_type, exc_val, traceback):
    self.file.write(f"\n \nSincerely, \n{self.sender}, \n")
    self.file.close()
    return False

# Q11
with Personalized('John', 'Michael') as order2:
  order2.write("""I am so proud of you!
Being your friend for all these years has been nothing but a blessing.
I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best.
Always.""")

# Q12 continue...
with generic('happy_bday.txt', 'Josiah', 'Remy') as order3, Personalized('Josiah', 'Esther') as order4:
  order4.write("""Happy Birthday!!
I love you to the moon and back.
Even though you’re a pain sometimes, you’re a pain I can't live without.
I am incredibly proud of you and grateful to have you as a sister.
Cheers to 25!! You’re getting old!""")