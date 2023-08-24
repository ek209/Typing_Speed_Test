import time
from speed_typer import Speed_Test

test = Speed_Test()
start = time.time()
test.print_sentence()
typed = input('Retype sentence: ')
stop = time.time()
elapsed_time = stop - start
correct = 0
for sentence_char, typed_char in zip(test.sentence, typed):
    if sentence_char == typed_char:
        correct += 1
longer_list = max(len(typed), len(test.sentence))
accuracy = round((correct/longer_list) * 100, 2)
minutes = elapsed_time / 60
wpm = round(test.random_word_count / minutes, 2)
cpm = round(longer_list / minutes, 2)
adjusted_wpm = round(cpm / 5, 2)
print(f'Congrats! You typed {adjusted_wpm} words per minute with {accuracy}% accuracy ({cpm} characters, {wpm} actual words)')
