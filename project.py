import sys
import os
import csv
from datetime import date

class Exercise:
    def __init__(self, name, seter, rep, category, link):
        if not name:
            raise ValueError("Missing name")
        if not seter:
            raise ValueError("Missing set")
        if not rep:
            raise ValueError("Missing reps")
        if not category:
            raise ValueError("Missing category")
        self.name = name
        self.seter = seter
        self.rep = rep
        self.category = category
        self.link = link

    def __str__(self):
        return f"Name: {self.name}, Sets: {self.seter}, Reps: {self.rep}, Category: {self.category}, Link: {self.link}"

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def seter(self):
        return self._seter

    @seter.setter
    def seter(self, seter):
        self._seter = seter

    @property
    def rep(self):
        return self._rep

    @rep.setter
    def rep(self, rep):
        self._rep = rep

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link


class Human:
    def __init__(self, height, bodymass, fatpercentage, watermass, musclemass, date):
        if not height:
            raise ValueError("Missing height")
        if not bodymass:
            raise ValueError("Missing bodymass")
        if not fatpercentage:
            raise ValueError("Missing fatpercentage")
        if not watermass:
            raise ValueError("Missing watermass")
        if not musclemass:
            raise ValueError("Missing musclemass")
        self.height = height
        self.bodymass = bodymass
        self.fatpercentage = fatpercentage
        self.watermass = watermass
        self.musclemass = musclemass
        self.date = date

    def __str__(self):
        return f"Body mass = {self.bodymass} kg, Fat = {self.fatpercentage} %, Water = {self.watermass} %, Muscle mass = {self.musclemass} kg, Date: {self.date}"

    def __repr__(self):
        return self.__str__()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def bodymass(self):
        return self._bodymass

    @bodymass.setter
    def bodymass(self, bodymass):
        self._bodymass = bodymass

    @property
    def fatpercentage(self):
        return self._fatpercentage

    @fatpercentage.setter
    def fatpercentage(self, fatpercentage):
        self._fatpercentage = fatpercentage

    @property
    def watermass(self):
        return self._watermass

    @watermass.setter
    def watermass(self, watermass):
        self._watermass = watermass

    @property
    def musclemass(self):
        return self._musclemass

    @musclemass.setter
    def musclemass(self, musclemass):
        self._musclemass = musclemass

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date


def main():
    print("----------------")
    print("1. My body\n2. My exercises\n3. Exit")
    print("----------------")
    choice_monitor()

def choice_monitor():
    try:
        choice = int(input("Enter number: "))
        match choice:
            case 1:
                os.system('clear')
                human_monitor()
            case 2:
                os.system('clear')
                exercises_monitor()
            case 3:
                sys.exit("See you later alligator 😉")
    except ValueError:
        pass



def human_monitor():
    print("----------------")
    print("1. Show all data\n2. Add new data\n3. Current body data\n4. Print BMI\n5. Go back")
    print("----------------")
    try:
        choice = int(input("Enter number: "))
        match choice:
            case 1:
                os.system('clear')
                data = show_data()
                for human in data:
                    print(human)
                human_monitor()
            case 2:
                os.system('clear')
                print(new_data())
                human_monitor()
            case 3:
                os.system('clear')
                print(current_data())
                human_monitor()
            case 4:
                os.system('clear')
                print(BMI())
                human_monitor()
            case 5:
                os.system('clear')
                main()
    except ValueError:
        pass

def show_data():
    data = []
    with open("human.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Human(row["height"], row["bodymass"], row["fatpercentage"], row["watermass"], row["musclemass"], row["date"]))

    return data

def new_data():
    try:
        height = int(input("What is youre current height ?: "))
        bodymass = float(input("What is youre current body mass ?: "))
        fatpercentage = float(input("What is youre current fat percentage ?: "))
        watermass = float(input("What is youre current water mass ?: "))
        musclemass = float(input("What is youre current muscle mass ?: "))
        today  = date.today()

        with open("human.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["height","bodymass", "fatpercentage", "watermass", "musclemass", "date"])
            writer.writerow({"height": height,"bodymass": bodymass, "fatpercentage": fatpercentage, "watermass": watermass, "musclemass": musclemass, "date": today})

        return "Saved new data"
    except:
        pass

def current_data():
    data = []
    with open("human.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Human(row["height"], row["bodymass"], row["fatpercentage"], row["watermass"], row["musclemass"], row["date"]))

    max_date = max(data, key = lambda Human: Human.date)
    return max_date

def BMI():
    print("Youre current BMI: ", end = "")
    data = []
    with open("human.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Human(row["height"], row["bodymass"], row["fatpercentage"], row["watermass"], row["musclemass"], row["date"]))

    max_date = max(data, key = lambda Human: Human.date)
    bmi = (float(max_date.bodymass)/int(max_date.height)**2)*10000
    return format(bmi,".2f")


def exercises_monitor():
    print("----------------")
    print("1. Show all exercises\n2. Add new exercise\n3. Exercises by category\n4. Delete exercise\n5. Go back")
    print("----------------")
    try:
        choice = int(input("Enter number: "))
        match choice:
            case 1:
                os.system('clear')
                data = show_exercises()
                for exercise in data:
                    print(exercise)
                exercises_monitor()
            case 2:
                os.system('clear')
                print(new_exercise())
                exercises_monitor()
            case 3:
                os.system('clear')
                data = exercise_category()
                for exercise in data:
                    print(exercise)
                exercises_monitor()
            case 4:
                os.system('clear')
                print(delete_exercise())
                exercises_monitor()
            case 5:
                os.system('clear')
                main()
    except ValueError:
        pass

def show_exercises():
    data = []
    with open("exercise.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Exercise(row["name"], row["seter"], row["rep"], row["category"], row["link"]))

    return data

def new_exercise():
    try:
        name = input("Enter exercise name: ").lower()
        seter = int(input("Enter exercise sets: "))
        rep = int(input("Enter exercise reps: "))
        category = input("Enter exercise category: ").lower()
        link = input("Enter link for the exercise: ")
        if link == "":
            link = "None"

        with open("exercise.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name","seter", "rep", "category", "link"])
            writer.writerow({"name": name,"seter": seter, "rep": rep, "category": category, "link": link})

        return "Saved new data"
    except:
        pass

def exercise_category():
    data = []
    with open("exercise.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Exercise(row["name"], row["seter"], row["rep"], row["category"], row["link"]))

    by_category = input("Enter exercise category: ").lower()
    filtered_data = []
    for d in data:
        if d.category == by_category:
            filtered_data.append(d)
    return filtered_data

def delete_exercise():
    data = []
    with open("exercise.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(Exercise(row["name"], row["seter"], row["rep"], row["category"], row["link"]))

    by_name = input("Enter exercise name to delete it: ").lower()
    new_data = []
    for d in data:
        if d.name != by_name:
            new_data.append(d)

    with open("exercise.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name","seter", "rep", "category", "link"])
            writer.writeheader()
            for d in new_data:
                writer.writerow({"name": d.name,"seter": d.seter, "rep": d.rep, "category": d.category, "link": d.link})
                
    return "Deleted data"

if __name__ == "__main__":
    main()
