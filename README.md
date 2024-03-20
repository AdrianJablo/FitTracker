# FitTracker
#### Video Demo:  <https://youtu.be/Rs9QrrScKe0>
#### Description:
Console application for tracking your body and exercise data. The program contains two classes “Exercise” and “Human”. Class Exercise gets and sets data about every exercise in the exercise.csv file. This program has four functions to operate on the Exercise class, to show all exercises in the exercise.csv file, add a new exercise, show exercises from a given category, and to delete a exercise by giving its name. Class Human however gets and sets data about our body data in the human.csv file. For the Human class we have four functions, to show all data from every date to check our progress, add new body data, check current data based on the earliest date in the human.csv file, and printing our BMI (Body Mass Index). In the project we have tests (test.py) which check the correct operation of individual functions in the program by mocking its data. The requirements.txt file has all the libraries needed for the proper functioning of the program.
#### Classes
1. Exercise having attributes
    - name
    - seter
    - rep
    - category
    - link
2. Human having attributes
    - height
    - bodymass
    - fatpercentage
    - watermass
    - musclemass
    - date
#### Functions
+  Human monitor
    - show_data() - shows all previous body data
    - new_data() - adds new body data
    - current_data() - shows current data based on earliest date
    - BMI() - prints current Body Mass Index based on earliest date
+ Exercise monitor
    - show_exercises() - shows all added exercises
    - new_exercise() - adds new exercise
    - exercise_category() - find and prints all exercises from the given category
    - delete_exercise() - deletes an exercise by giving its name

#### Clone the project
```bash
    git clone https://github.com/me50/AdrianJablo.git
```

#### Runing Program
```python
usage: python project.py
Choose:
----------------
1. My body
2. My exercises
3. Exit
----------------
Option:
1. My body
----------------
1. Show all data
2. Add new data
3. Current body data
4. Print BMI
5. Go back
----------------
Option:
2. My exercises
----------------
1. Show all exercises
2. Add new exercise
3. Exercises by category
4. Delete exercise
5. Go back
----------------
```

#### Running Tests
To run tests, run the following command
```bash
    pytest
```
#### Author Info
-[GitHub Page](https://github.com/AdrianJablo)
-[LinkedIn Page](https://www.linkedin.com/in/adrian-jabłoński-587b26278)
