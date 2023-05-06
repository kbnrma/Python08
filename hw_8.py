# 1) 
import random

def rndm_language(languages):
    rndm_choice = random.choice(languages)
    with open('txtfile.txt', 'a') as output_file:
        output_file.write(rndm_choice + '\n')
    return rndm_choice
language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]
print (rndm_language(language))

# 2) 
text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.'''
with open('text.txt', 'w') as new:
    new.write(text)
with open('text.txt', 'w') as new:
    print(text, file=new)

# ДОП ЗАДАЧА:
# 3) 
with open('text.txt', 'r') as new_file:
    text = new_file.read()

with open('wikipedia.txt', 'w') as new_file1:
    new_file1.write(text)
