# 1. Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.
import re
def replace_words(text, forbidden):
    for word in forbidden:
        text=re.sub(word, '*' * len(word),text)
    return text

text="I hate bad words and bad language"
forbidden=["bad"]

print(replace_words(text, forbidden))