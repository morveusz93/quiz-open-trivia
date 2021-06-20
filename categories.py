categories = [
    {
        "name" : "General Knowledge",
        "id" : 9
    },
    {
        "name" : "Science & Nature",
        "id" : 17
    },
    {
        "name" : "Science: Computers",
        "id" : 18
    },
    {
        "name" : "Science: Mathematics",
        "id" : 19
    },
    {
        "name" : "Mythology",
        "id" : 20
    },
    {
        "name" : "Animals",
        "id" : 27
    }
]
class Category:
    def __init__(self, name, id):
        self.name = name
        self.id = id


list_of_categories = [Category(cat["name"], cat["id"]) for cat in categories]