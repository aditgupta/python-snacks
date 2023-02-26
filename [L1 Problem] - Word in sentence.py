"""
Given a sentence and a word, write a function that returns the number of times the word appears in the sentence
without using the count() method
"""


def word_in_sentence(sentence, target_word) -> int:
    count = 0
    words = sentence.split()
    for word in words:
        if word == target_word:
            count += 1
    return count


new_sentence = "A blue car with blue wheels under the blue sky"
selected_word = "blue"
print(word_in_sentence(new_sentence, selected_word))
