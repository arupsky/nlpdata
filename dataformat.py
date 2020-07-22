from xml.etree import ElementTree
import csv
import pandas as pd
import json

file = 'data/articles-training-byarticle-20181122/articles-training-byarticle-20181122.xml'
tree = ElementTree.parse(file)
root = tree.getroot()
print(root)


def element_to_string(element):
    s = element.text or ""
    for sub_element in element:
        s += ElementTree.tostring(sub_element, encoding='unicode')
    s += element.tail
    return s

for article in root.iter('article'):
    if 'id' in article.attrib:
        articleID = article.attrib['id']
    else:
        articleID = ''
    if 'published-at' in article.attrib:
        pub = article.attrib['published-at']
    else:
        pub = ''
    if 'title' in article.attrib:
        articleTitle = article.attrib['title']
    else:
        articleTitle = ''

    contt = element_to_string(article)

    result = [articleID, pub, articleTitle, contt]
    #print(result)
    #df = pd.DataFrame(result)
    #df.to_csv('file2.csv', index=False, header=False)

    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, sort_keys = True, indent=4)

