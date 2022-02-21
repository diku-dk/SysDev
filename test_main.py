import main

# testing with test CPR numbers from medcom


def test_gender_male_full():
    assert main.gender("010490-9995") == 'male'


def test_gender_male_short():
    assert main.gender("0104909995") == 'male'


def test_gender_female_full():
    assert main.gender("010862-9996") == 'female'


def test_gender_female_short():
    assert main.gender("0108629996") == 'female'


def test_age():
    # This test should be refined to use today's date to calculate the expected age.
    # Right now it is hardcoded to be run in February year 2022
    assert main.age("010490-9995") == 31

