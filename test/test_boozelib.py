from nose.tools import assert_almost_equal

from boozelib import get_bac, get_degradation


# TEST DATA

users = (
  (32, 42, 155, True), #f1
  (30, 80, 173, True), #f2
  (30, 68, 172, False), #m1
  (34, 103, 186, False), #m2
)

drinks = (
  (500, 4.9), #d1
  (100, 40.0) #d2
)

test_cases_bac = (
  (users[0], drinks[0], 0.597136937838),
  (users[0], drinks[1], 0.974917449531),
  (users[3], drinks[0], 0.276170740785),
  (users[3], drinks[1], 0.450891005363),
)

test_cases_degradation = (
  (users[0], 60, 0.19193687287649608),
  (users[1], 60, 0.25050519526247184),
  (users[2], 60, 0.1889870440348846),
  (users[3], 60, 0.217695813527036),
)


# HELPER FUNCTIONS

def check_get_bac(user, drink, expected):
  age, weight, height, sex = user
  volume, percent = drink
  bac = get_bac(age, weight, height, sex, volume, percent)
  assert_almost_equal(bac, expected)

def check_get_degradation(user, minutes, expected):
  age, weight, height, sex = user
  deg = get_degradation(age, weight, height, sex, minutes)
  assert_almost_equal(deg, expected)


# TESTS

def test_get_bac():
  for user, drink, expected in test_cases_bac:
    yield check_get_bac, user, drink, expected

def test_get_degradation():
  for user, minutes, expected in test_cases_degradation:
    yield check_get_degradation, user, minutes, expected
