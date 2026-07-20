#Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set
#data type.
def fun(s):
    word=[]
    for i in s:
        word.extend(i.split())
    unique_words=set(word)
    for w in unique_words:
        print(f'{w}:{word.count(w)}')
s = ["apple orange", "apple banana", "orange apple"]
fun(s)


