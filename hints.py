import numpy
import json
import random

#cateogry
def main():
    with open('spell_sets.json', 'r') as json_File:
        spell_sets = json.load(json_File)
    hint = True
    if hint == True:
        num = random.randint(1,4)
        set_name = 'Set ' + str(num)
        set_info = spell_sets[set_name]
        print(set_info['attribute'])
            

main()