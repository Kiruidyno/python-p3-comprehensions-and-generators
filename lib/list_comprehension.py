#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num%2==0]
    return evens
result=return_evens([0, 2, 3, 5, 7, 8, 9])
print(result)

def make_exclamation(sentence_list):
    exclamation_list=[sentence+'!' for sentence in sentence_list]
    return exclamation_list

result=make_exclamation(["Hello", "I'm doing great", "Python is fune"])
print(result)