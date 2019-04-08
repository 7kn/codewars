#!/usr/bin/env python3
# My anwser:
def find_short(s):
    word_list = list(s.split())
    word_len_dict = {}
    
    for word in word_list:
      word_len_dict[word] = len(word)
    
    smallest_key = min(word_len_dict, key= lambda x: word_len_dict.get(x))
    l = word_len_dict[smallest_key]
    
    return l # l: shortest word length

# Best anwser:
#def find_short(s):
#    return min(len(x) for x in s.split())