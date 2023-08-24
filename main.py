import requests
from random import randint, choice
import time

random_word_count =  10 #randint(40,60)
random_word_api = f'https://random-word-api.herokuapp.com/word?number={random_word_count}'
random_sentence_response = requests.get(random_word_api)
random_sentence_response.raise_for_status()
random_sentence_json = random_sentence_response.json()
sentence = ''
for word in random_sentence_json:
    sentence += f'{word} '
sentence = sentence.strip()
sentence += choice(['.', '!', '?'])
start = time.time()
print(sentence)
typed = input('Retype sentence: ')
stop = time.time()
elapsed_time = stop - start
correct = 0
for sentence_char, typed_char in zip(sentence, typed):
    if sentence_char == typed_char:
        correct += 1
longer_list = max(len(typed), len(sentence))
accuracy = (correct/longer_list) * 100
minutes = elapsed_time / 60
wpm = random_word_count / minutes
cpm = longer_list / minutes
print(f'Congrats! You typed {wpm} words per minute ({cpm} characters per minute) with {accuracy}% accuracy')