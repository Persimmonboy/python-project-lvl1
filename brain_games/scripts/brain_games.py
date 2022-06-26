#!/usr/bin/env python

#from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import even


def welcome():
    print("Welcome to the Brain Games!")


def main():
    welcome()
    #welcome_user()
    even()


if __name__ == "__main__":
    main()
