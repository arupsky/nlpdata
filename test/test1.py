"""
import pandas as pd
from lxml import etree
import archive

xmlfile = archive.open("test.xml")
xmldoc = etree.parse(xmlfile)
root = xmldoc.getroot()

foods  = root.find("breakfast_menu").findall("food")

(name, price, description, calories) = (list() for i in range(4))

for food in foods:
    name.append(food.find("name").text)
    price.append(food.find("price").text)
    description.append(food.find("description").text)
    calories.append(food.find("calories").text)

df= pd.DataFrame({"name": name,
                  "price": price,
                  "description": description,
                  "calories": calories})
df.to_csv(test1, sep='\t', encoding='utf-8')

"""
from xml import etree
from xml.etree import ElementTree
def element_to_string(element):
    s = element.text or ""
    for sub_element in element:
        s += etree.tostring(sub_element)
    s += element.tail
    return s

element_to_string('element_to_string('')')