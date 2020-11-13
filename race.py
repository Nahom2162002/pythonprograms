import random

def first_car():
    car_speed = random.randint(50, 100)
    return car_speed

def second_car():
    car_speed = random.randint(50, 100)
    return car_speed

def main():
    car1 = first_car()
    car2 = second_car()
    if car1 > car2:
        return "Car 1 wins"
    elif car2 > car1:
        return "Car 2 wins"
    else:
        return "Draw"