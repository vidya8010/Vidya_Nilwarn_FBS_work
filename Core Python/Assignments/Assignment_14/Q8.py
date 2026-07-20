#Write a Python program to find all the anagrams and group them
#together from a given list of strings.
def group_anagrams(words):
    visited = set()
    for i in range(len(words)):
        if words[i] in visited:
            continue
        group=[words[i]]
        visited.add(words[i])
        for j in range(i+1,len(words)):
            if sorted(words[i]) == sorted(words[j]):
                group.append(words[j])
                visited.add(words[j])
        if len(group)>1:
            print(set(group))  

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

group_anagrams(words)