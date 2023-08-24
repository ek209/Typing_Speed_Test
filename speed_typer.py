import requests
from random import randint, choice
import time

class Speed_Test():
    def __init__(self):
        self.sentence = self.sentence_creator()

    #grabs word_count words from api
    def sentence_grabber(self, word_count):
        random_word_api = f'https://random-word-api.herokuapp.com/word?number={word_count}'
        random_sentence_response = requests.get(random_word_api)
        random_sentence_response.raise_for_status()
        return random_sentence_response.json()

    #adds words from json into a string
    def json_to_string(self, json):
        sentence = ''
        for word in json:
            sentence += f'{word} '
        sentence = sentence.strip()
        sentence += choice(['.', '!', '?'])
        return sentence

    #creates sentence of random words for speed test
    def sentence_creator(self):
        self.random_word_count = randint(40,60)
        random_sentence_json = self.sentence_grabber(self.random_word_count)
        sentence = self.json_to_string(random_sentence_json)
        return sentence
    
    def print_sentence(self):
        print(self.sentence)