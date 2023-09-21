import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

import calculate_calorie as calc

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('contents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def calculate_bmi(height,weight):
     if(height<=0 or weight <=0):
          print("invalid input")
          return -1
     return weight/(height*height)

def ask_food():
    food_list = []
    print("Tell me what are your daily intakes for food with amount sepereated by space. Press 'q' to go back")
    food = ""
    while(food != 'q'):
         food = input()
         food = food.split()
         food, amount = food[0], food[1]

         print(f"{food}, {amount}")

    
    
def chat():
     bot_name = "Sam"
     print("Let's chat! (type 'quit' to exit)")
     while True:
     # sentence = "do you use credit cards?"
          sentence = input("You: ")
          if sentence == "quit":
               break

          sentence = tokenize(sentence)
          X = bag_of_words(sentence, all_words)
          X = X.reshape(1, X.shape[0])
          X = torch.from_numpy(X).to(device) 

          output = model(X)
          _, predicted = torch.max(output, dim=1)

          tag = tags[predicted.item()]

          probs = torch.softmax(output, dim=1)
          prob = probs[0][predicted.item()]
          if prob.item() > 0.75:
               for intent in intents['intents']:
                    if tag == intent["tag"]:
                         if(tag == "lose weight" or tag == "gain weight"):
                              print(f"{bot_name}: {random.choice(intent['responses'])}, for that we need to calculate bmi")
                              height = float(input("What is your height(in m)"))
                              weight = float(input("What is your weight(in kg)"))
                              age = float(input("What is your age?"))
                              gender = input("What is your gender?")
                              activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ")
                              bmi = calculate_bmi(height, weight)

                              calorie = int(calc.calculate_bmr(height, weight, gender,age,activity_level))
                              print(f"Your bmi is {bmi} \n")
                              print(f"For being healthy you need to drink at least 5 Litres of water per day")
                              print(f"Your calorie is {calorie}")
                              if(bmi < 18.5):
                                   print("You are under weight")
                                   # ask_food()
                              elif(bmi >=18.5 and bmi < 24.9):
                                   print("You are healthy")
                              elif(bmi>24.5 and bmi <=29.9):
                                   print("you are over weight")
                                   #  ask_food()
                              elif(bmi>29.9):
                                   print("you are obese")

                              if(tag == 'lose weight'):
                                   print(f"According to the data given by you, you need to intake {calorie-300} calories per day")
                              if(tag == 'gain weight'):
                                   print(f"According to the data given by you, you need to intake {calorie+300} calories per day")
                         else:
                              print(f"{bot_name}: {random.choice(intent['responses'])}")
          else:
               print(f"{bot_name}: I do not understand...")