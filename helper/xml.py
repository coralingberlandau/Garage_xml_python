import os
from icecream import ic
import xml.etree.ElementTree as ET

def restart_data():
    global cars
    cars = []
    save_data_to_xml('cars.xml', cars)
    ic ("All data has been cleared.")

def save_data_to_xml(filename, cars):
    cars_root = ET.Element("cars")  
    for car in cars:
        car_element = ET.SubElement(cars_root, "car")  
        for key, value in car.items():
            car_property = ET.SubElement(car_element, key)  
            car_property.text = value  

    tree = ET.ElementTree(cars_root)
    tree.write(filename) 

def load_data_from_xml(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Returning empty list.")
        return []
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    cars = []
    for car_element in root.findall('car'):
        car = {}
        for attr in car_element:
            car[attr.tag] = attr.text
        cars.append(car)
    
    return cars