
from enum import Enum
import xml.etree.ElementTree as ET
import os
from icecream import ic
from helper.xml import load_data_from_xml, save_data_to_xml, restart_data
from helper.helpers import add_car, print_data, delete_car, find_index_car, update_car, sum_cars

cars = []

class Menu(Enum):
    ADD = 1
    PRINT = 2
    DELETE = 3
    UPDATE = 4
    SUM = 5
    RESTART = 6
    EXIT =7

def display_nemu():
    for men in Menu: print (f'{men.value} - {men.name}')
    return Menu (int(input("please enter what you need:")))


if __name__ == "__main__":
    try: 
        cars = load_data_from_xml('cars.xml')
        while True:
                selece_user = display_nemu()
                if selece_user == Menu.ADD: add_car(cars)
                if selece_user == Menu.PRINT: print_data(cars)
                if selece_user == Menu.DELETE: delete_car(cars)
                if selece_user == Menu.UPDATE: update_car(cars)
                if selece_user == Menu.SUM: sum_cars(cars)
                if selece_user == Menu.RESTART: restart_data()
                if selece_user == Menu.EXIT:
                    save_data_to_xml("cars.xml", cars)
                    exit()
    except Exception as e:
        print("Error:", e)
        print("Recharge")