#!/usr/bin/env python

import random

import os

def welcome():
    print("\nWelcome to Hangman")
    print ("\npress 1 if you would like to play")
    print ("press 2 if you want to quit")
    play = input("\n")
    play = int(play)
    if play == 2 :
        print ("Thanks for playing Bye")
        exit()
    if play == 1 :
        main()
    else:
        print ("that is not an option, please try again")


def main():

    #wordlist()
    word_list = []
    with open ('words.txt', 'rt') as file:
        for x in file:
            word_list.append(x.rstrip('\n'))
            #print(word_list
    while ("" in word_list):
        word_list.remove("")

    random_word = random.choice(word_list)
    #print (word_list)
    #print (random_word)
          #word_list = ["superman","barspin","whip","backflip","cashrole","flair"]
          #random_word = words4
          #word = random.choice(word_list)
    word_length = len(random_word) # get length of chosen word
    hidden = word_length* "*" #convert word into *
    #print("hidden = ", hidden)
    #print (word_length)
    #print (hidden)
    lives = 7
    print("you have to guess a random mtb trick")
    print("the word has", word_length, "characters")
    guess_bank = []

    hidden = list(hidden) # turns stars into list
    guess_list = list(random_word)
    while lives > 0:
        print (' '.join(hidden))
        guess = input("guess a letter"+"\n")
        if not len(guess) == 1:
            print ("please enter only 1 letter at a time")
            continue
        if guess in guess_bank:
           print ("You have already entered that letter, please try again")
           continue
        else:
             guess_bank.append(guess)
        if guess in random_word:
            print("You guessed correctly")
            for letter in guess_list:
               if guess == letter:
                    location = guess_list.index(guess) # makes variable containing index place of guess
                    hidden[location] = guess # Change star to guess
                    guess_list[location]  = '_'
                    continue
        else:
            lives = lives - 1
            if lives < 1:
                print ("You lost")
                continue
            print ("Wrong, try again")
            print ("you have", lives, "lives left")
            continue
        print ("Well done you have", lives, "lives left")
        if not "*" in hidden:
            print ("congratulations, you correctly guessed {}! You are a champion".format(random_word))
            welcome()
            

    welcome()

welcome()