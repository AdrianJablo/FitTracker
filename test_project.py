from project import show_data, new_data, current_data, BMI
from project import Human, Exercise
from project import show_exercises, new_exercise, exercise_category, delete_exercise
from unittest.mock import patch, mock_open

def test_show_data():
    mock_file = mock_open(read_data='height,bodymass,fatpercentage,watermass,musclemass,date\n180,70,20,50,30,2022-01-01\n170,60,15,45,25,2022-02-01')
    with patch('builtins.open', mock_file):
        result = show_data()
        assert len(result) == 2
        assert isinstance(result[0], Human)
        assert result[0].date == '2022-01-01'

def test_new_data():
    with patch('builtins.input', side_effect=[180, 70, 20, 50, 30]), patch('builtins.open', new_callable=mock_open):
        result = new_data()
        assert result == "Saved new data"

def test_current_data():
    mock_file = mock_open(read_data='height,bodymass,fatpercentage,watermass,musclemass,date\n180,70,20,50,30,2022-01-01\n170,60,15,45,25,2022-02-01')
    with patch('builtins.open', mock_file):
        result = current_data()
        assert isinstance(result, Human)
        assert result.date == '2022-02-01'

def test_BMI(capfd):
    mock_file = mock_open(read_data='height,bodymass,fatpercentage,watermass,musclemass,date\n170,60,15,45,25,2022-02-01')
    with patch('builtins.open', mock_file):
        result = BMI()
        assert result == '20.76'

    captured = capfd.readouterr()
    assert captured.out == 'Youre current BMI: '

def test_show_exercises():
    mock_file = mock_open(read_data='name,seter,rep,category,link\nPush ups,3,10,upper body,link1\nSquats,3,15,lower body,link2')
    with patch('builtins.open', mock_file):
        result = show_exercises()
        assert len(result) == 2
        assert isinstance(result[0], Exercise)
        assert result[0].name == 'Push ups'

def test_new_exercise():
    mock_input = patch('builtins.input', side_effect=['Push-ups', '3', '10', 'upper body', 'link1'])
    mock_file = mock_open()
    with mock_input, patch('builtins.open', mock_file):
        result = new_exercise()
        assert result == 'Saved new data'

def test_exercise_category():
    mock_input = patch('builtins.input', return_value='upper body')
    mock_file = mock_open(read_data='name,seter,rep,category,link\nPush-ups,3,10,upper body,link1\nSquats,3,15,lower body,link2')
    with mock_input, patch('builtins.open', mock_file):
        result = exercise_category()
        assert len(result) == 1
        assert isinstance(result[0], Exercise)
        assert result[0].category == 'upper body'

def test_delete_exercise():
    mock_input = patch('builtins.input', return_value='Push-ups')
    mock_file = mock_open(read_data='name,seter,rep,category,link\nPush-ups,3,10,upper body,link1\nSquats,3,15,lower body,link2')
    with mock_input, patch('builtins.open', mock_file):
        result = delete_exercise()
        assert result == 'Deleted data'
