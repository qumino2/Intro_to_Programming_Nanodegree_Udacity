#!/usr/bin/env python
# -*- coding: utf-8 -*-

paragraph_easy = "The __1__ is a bunch of computers that communicate\n\
with each other. When writing HTML, we tell __2__s the type\n\
of each __3__ by using HTML __4__s."
answers_easy =["web", "browser", "element", "tag"]
blanks_easy = ["__1__", "__2__", "__3__", "__4__"]

paragraph_medium = "__1__ stands for __2__ Style Sheets and they give __3__s a way\n\
to control the __4__ of related HTML elements. This is done by giving\n\
similar __5__ elements the same __6__ name and then specifying\n\
the style that should apply to that class."
answers_medium = ["CSS", "Cascading", "programmer", "style", "HTML", "class"]
blanks_medium = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__"]

paragraph_hard = "HTML elements are either __1__ or __2__.\n\
When writing __3__, programmers use special text __4__s.\n\
For example, some text editors will automatically generate\n\
a __5__ HTML tag when you write an __6__ tag.\n\
When programmers don't avoid __7__,\n\
they will often have to do the __8__ thing over and over." 
answers_hard = ["inline", "block", "code", "editor", "closing", "opening", "repetition", "same"]
blanks_hard = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__"]


# def user_choose_level():
# 	"""
# 	function user_choose_level returns function user_guess_word with
# 	parameters respectively when the input is valid, otherwise
# 	return itself
# 	inputs: None
# 	outputs: call function user_choose_level() or user_choose_level()   

# 	"""
# 	level_choice = raw_input("Please select a game difficulty by typing it in!\n\
# Possible choices include easy, medium, and hard.\n").lower()
# 	if level_choice == "easy":
# 		print "You've chosen easy!\n\nYou will get 5 guesses per problem\n"
# 		return user_guess_word(paragraph_easy, answers_easy, blanks_easy)
		
# 	elif level_choice == "medium":
# 		print "You've chosen medium!\n\nYou will get 5 guesses per problem\n"
# 		return user_guess_word(paragraph_medium, answers_medium, blanks_medium)
		
# 	elif level_choice == "hard":
# 		print "You've chosen hard!\n\nYou will get 5 guesses per problem\n"
# 		return user_guess_word(paragraph_hard, answers_hard, blanks_hard)

# 	else:
# 		print "That's not an option!"
# 		user_choose_level()

def user_choose_level():
    """
    function user_choose_level returns function user_guess_word with
    parameters respectively when the input is valid, otherwise
    return itself
    inputs: None
    outputs: call function user_choose_level() or user_choose_level()   

    """
    level_choice = raw_input("Please select a game difficulty by typing it in!\n\
Possible choices include easy, medium, and hard.\n").lower()
    while level_choice not in ["easy", "medium", "hard"]:
        level_choice = raw_input("That's not an option!\nPlease select a game difficulty by typing it in!\n\
Possible choices include easy, medium, and hard.\n").lower()
    announce = "You've chosen {0}!\n\nYou will get 5 guesses per problem\n".format(level_choice)
    print(announce)
    if level_choice == "easy":
        return user_guess_word(paragraph_easy, answers_easy, blanks_easy)
    elif level_choice == "medium":
        return user_guess_word(paragraph_medium, answers_medium, blanks_medium)
    elif level_choice == "hard":
        return user_guess_word(paragraph_hard, answers_hard, blanks_hard)
	

def user_guess_word(paragraph, answers, blanks):
	"""
	function user_guess_word takes in three parameters: paragraph, answers, blanks，
	return strings which give users information about how to play this game and 
	what to do next.
	inputs: paragraph, which is a string, answers and blanks which are lists
	outputs: a string, which tells the users what to do next.

	"""
	
	index_blanks = 0 
	num_tries = 5 
	while index_blanks < len(blanks):

		guess = raw_input(paragraph + "\n\n\n" + "What should be substituted in for " + blanks[index_blanks] + "?")
		if guess.lower() == answers[index_blanks].lower():
			paragraph = paragraph.replace(blanks[index_blanks], answers[index_blanks])
			index_blanks += 1
			print "\nCorrect!\n"
			
		else:
			num_tries -= 1
			if num_tries > 0:
				print "That isn't the correct answer! Let's try again; you have " + str(num_tries) + " trys left!\n" 
			else:
				print  "You've failed too many straight guesses!  Game over!"
				break

	if index_blanks == len(blanks):
				print paragraph + "\n\nYou won!\n"

user_choose_level()