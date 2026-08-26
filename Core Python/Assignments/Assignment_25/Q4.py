# 4. Write a function that extracts all the URLs from a given text using regular expressions.
# Return a list of URLs found in the input text.
import re
def extract_urls(text):
    pattern=r'https?://\S+'
    return re.findall(pattern,text)


text="Visit https://google.com and https://openai.com for more information."

print(extract_urls(text))