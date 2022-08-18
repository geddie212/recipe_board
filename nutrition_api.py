import requests
import os

URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

HEADERS = {
    "X-RapidAPI-Key": os.environ.get("X-RapidAPI-Key"),
    "X-RapidAPI-Host": os.environ.get("X-RapidAPI-Host")
}

class NutritionAPI:

    def __init__(self, query_dict):
        self.query_dict = query_dict
        self.query_string = {'instructionsRequired': False, 'addRecipeInformation': True, 'number': 50,
                             'fillIngredients': True}

    def query_stringer(self):
        for x, y in self.query_dict.items():
            try:
                if y == 'diet' or y == 'intolerances':
                    self.query_string[y] += f", {x}"
                else:
                    self.query_string[x] += f", {x}"
            except KeyError:
                if y == 'diet' or y == 'intolerances':
                    self.query_string[y] = f"{x}"
                else:
                    self.query_string[x] = f"{y}"
        return self.query_string

    def send_request(self):
        response = requests.request("GET", URL, headers=HEADERS, params=self.query_string)
        return response.json()


class RecipeAPI:

    def __init__(self, id):
        self.url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
        self.response = requests.get(self.url, headers=HEADERS)

    def return_data(self):
        return self.response.json()
