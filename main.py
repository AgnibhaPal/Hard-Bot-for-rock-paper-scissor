import time
import os
import random
def clear():
  if os.name == 'nt':
   os.system('cls')
  else:
   os.system('clear')
    
element = ['Rock', 'Paper', 'Scissor']
bot = ''
player = ''
playersc = 0
botsc = 0
x = True
ix = True
save = ''
save1 = 0
while ix:
  if x:
    while True:
     print('****************************************')
     print('WELCOME TO ULTRA HARD ROCK PAPER SCISSOR')
     print('****************************************')
     print('[A] Continue')
     print('[B] Quit')
     print('[C] Info') 
     ans = input('> ')
     time.sleep(0.1)
     clear()
     if ans.lower() == 'c':
      clear()
      print('****************************************')
      print('WELCOME TO ULTRA HARD ROCK PAPER SCISSOR')
      print('****************************************')
      print('[A] Back')
      print('*****************************')
      print('Created by: Agnibha Pal')
      print('Created on: 12-06-2022')
      print('Programming language: Python')
      print('Game Version: 0.1')
      print('Game Idea by: Xie Zhaozhi')
      print('Creator github: https://github.com/AgnibhaPal')
      print('Game Stage: Testing')
      ans = input('> ')
      if ans.lower() == 'a':
       clear()
       continue 
     elif ans.lower() == 'a':
       x = False
       break
     else:
       clear()
       ix = False
       x = None
       break
  else:
   while True:
    clear()
    print('****************************************')
    print('WELCOME TO ULTRA HARD ROCK PAPER SCISSOR')
    print('****************************************')
    print('[A] Back')
    print('*****************************')
    print('Player Score: ' + str(playersc) ,'Bot Score: ' + str(botsc))
    print('*****************************')
    ans = input('Choose (Rock, Paper or Scissor): ')
    if ans == 'a':
      x = True
      clear()
      break
    player = ans
    if save1 == 0:
        bot = random.choice(element)
    elif not save1 == 0:
       if save1 == 'rock':
        bot = 'paper'
       elif save1 == 'paper':
        bot = 'scissor'
       elif save1 == 'scissor':
        bot = 'rock'
    else:
       if save == 'rock':
        bot = 'paper'
       elif save == 'paper':
        bot = 'scissor'
       elif save == 'scissor':
        bot = 'rock'
    print('Bot Choosing...')
    time.sleep(1)
    save = ''
    if player.lower() == bot.lower(): #draw condition = 1
      print('Draw!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      save = player
    elif player.lower() == 'rock' and bot.lower() == 'paper': #lost condition = 2
      print('Player Lost!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc -= 1
      botsc += 1
      save1 = bot
      save = player
    elif player.lower() == 'paper' and bot.lower() == 'rock': #win condition = 3
      print('Player Win!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc += 1  
      botsc -= 1
      save = player
    elif player.lower() == 'paper' and bot.lower() == 'scissor': #lost condition = 4
      print('Player Lost!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc -= 1
      botsc += 1
      save1 = bot
      save = player
    elif player.lower() == 'rock' and bot.lower() == 'scissor': #win condition = 5
      print('Player Win!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc += 1  
      botsc -= 1
      save = player
    elif player.lower() == 'scissor' and bot.lower() == 'paper': #win condition = 6
      print('Player Win!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc += 1  
      botsc -= 1
      save = player
    elif player.lower() == 'scissor' and bot.lower() == 'rock': #lost condition = 7
      print('Player Lost!')
      print('Player choose: ' + player ,'Bot choose: ' + bot)
      playersc -= 1 
      botsc += 1
      save1 = bot
      save = player
    player = ''
    bot = ''
    ans = input('Press Enter to continue: ')
    if not ans == 'rock' or 'paper' or 'scissor':
      continue
      