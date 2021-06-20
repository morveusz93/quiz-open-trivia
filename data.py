import json
import requests
from categories import list_of_categories


class QuestionData:

    def __init__(self):
        
        self.choosen_category = self.ask_for_cat()
        self.difficult = self.ask_diff()
        self.link =  f"https://opentdb.com/api.php?amount=12&category={self.choosen_category}&difficulty={self.difficult}&type=boolean"
        self.questions_data = requests.get(self.link).json()["results"]


    def print_categories(self):
        for category in list_of_categories:
            print(f"[{list_of_categories.index(category) + 1}] - {category.name}")


    def ask_for_cat(self):
        print("Please choose category of quiz: ")
        self.print_categories()
        choosen_category = input("Your choice: ")
        print()
        try:
            choosen_category_id = list_of_categories[int(choosen_category) - 1].id 
            return choosen_category_id
        except (ValueError, IndexError):
            print("Wrong choice \n")
            self.ask_for_cat()


    def ask_diff(self):
        diff = input("Difficult (Easy/Medium/Hard): ").lower()
        if diff in ['easy', 'e']:
            return 'easy'
        elif diff in ['medium', 'med', 'm']:
            return 'medium'
        elif diff in ['hard', 'h']:
            return 'hard'
        else:
            print("Wrong choice")
            return self.ask_diff()

