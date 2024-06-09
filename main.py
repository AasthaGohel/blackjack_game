import art
import random
import os
import sys

print(art.logo)
cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_game():
  return [],[]

def deal_card():
  return random.choice(cards)

def calculate_score(cards):
  score = sum(cards)
  if 11 in cards and score>21:
    cards[cards.index(11)] = 1
    score = sum(cards)
  return score  
  
def show_situation(user_cards,computer_cards):
  print("Yours cards are: ",user_cards,"Current Score: ", calculate_score(user_cards))
  print("Computer's first card is: ",computer_cards[0])

def show_final_situation(user_cards,computer_cards):
  print("Your final hand: ",user_cards,"Final Score: ", calculate_score(user_cards))
  print("Computer's final hand: ",computer_cards,"Final Score: ", calculate_score(computer_cards))


def user_turn(user_cards,computer_cards):
  while calculate_score(user_cards)<21:
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_input == 'y':
          user_cards.append(deal_card())
          show_situation(user_cards,computer_cards)
        else:
          break

def computer_turn(computer_cards):          
  while calculate_score(computer_cards)<17:
        computer_cards.append(deal_card())
  
def check_winner(user_cards,computer_cards):
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  if user_score>21:
    print("You went over. You lose\U0001F61E")
  elif computer_score>21 or user_score>computer_score:
    print("You win\U0001F604")
  elif user_score<computer_score:
    print("You lose\U0001F61E")
  else:
    print("Draw\U0001F19D")
  
def main():
    user_cards,computer_cards = reset_game()
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    show_situation(user_cards,computer_cards)
    user_turn(user_cards,computer_cards)
    computer_turn(computer_cards)
    show_final_situation(user_cards,computer_cards)
    check_winner(user_cards,computer_cards)

def play_game():
  play = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ")
  if play=='y':
    clear_screen()
    print(art.logo)
    main()
    play_game()
    
  else:
    exit() 

play_game()
 
               


  
 

