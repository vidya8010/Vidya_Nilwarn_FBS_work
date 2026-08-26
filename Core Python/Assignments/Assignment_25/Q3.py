import re
def count_words(text):
    words=re.findall(r'\w+', text)
    count={}
    print(words)
    for word in words:
        word=word.lower()

        if word in count:
            count[word]+=1
        else:
            count[word]=1

    return count
text = "Python is easy.Python is powerful."
print(count_words(text))