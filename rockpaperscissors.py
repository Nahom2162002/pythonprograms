import random

def rock_paper_scissors():
    x = random.randint(1, 6)
    rounds = 5
    player_rounds = 0
    cpu_rounds = 0
    while rounds > 0:
       if x == 1 | x == 2:
          cpu_input = "Rock"
       elif x == 3 | x == 4:
          cpu_input = "Paper"
       else:
          cpu_input = "Scissors"
       player_input = input("Rock, Paper, Scissors...")
       print("Shoot!")
       if player_input == "Rock" and cpu_input == "Paper":
          print(player_input)
          print(cpu_input)
          print("CPU wins!")
          rounds -= 1
          cpu_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if cpu_rounds == 3:
              break
       elif cpu_input == "Rock" and player_input == "Paper":
          print(player_input)
          print(cpu_input)
          print("Player wins!")
          rounds -= 1
          player_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if player_rounds == 3:
              break
       elif player_input == "Paper" and cpu_input == "Scissors":
          print(player_input)
          print(cpu_input)
          print("CPU wins!")
          rounds -= 1
          cpu_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if cpu_rounds == 3:
              break
       elif cpu_input == "Paper" and player_input == "Scissors":
          print(player_input)
          print(cpu_input)
          print("Player wins!")
          rounds -= 1
          player_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if player_rounds == 3:
              break
       elif player_input == "Scissors" and cpu_input == "Rock":
          print(player_input)
          print(cpu_input)
          print("CPU wins!")
          rounds -= 1
          cpu_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if cpu_rounds == 3:
              break
       elif cpu_input == "Scissors" and player_input == "Rock":
          print(player_input)
          print(cpu_input)
          print("Player wins!") 
          rounds -= 1
          player_rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if player_rounds == 3:
              break
       else:
          print(player_input)
          print(cpu_input)
          print("Draw")
          rounds += 1
          print("Player: ", player_rounds, "CPU: ", cpu_rounds)
          if player_rounds == 3 | cpu_rounds == 3:
              break
    if player_rounds > cpu_rounds:
        print("Player wins!")
    else:
        print("CPU wins!")

def main():
    rock_paper_scissors()

if __name__ == "__main__":
    main()