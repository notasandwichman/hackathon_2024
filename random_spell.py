import csv
import random
import json

def csv_to_spell_dict(csv_file):
    spell_dict = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        for row in reader:
            name = row[0]
            classes = row[1]
            level = int(row[2])
            school = row[3]
            cast_time = row[4]
            spell_range = row[5]
            duration = row[6]
            verbal = bool(int(row[7]))
            somatic = bool(int(row[8]))
            material = bool(int(row[9]))
            material_cost = row[10]
            description = row[11]
            spell_dict[name] = {
                'classes': classes,
                'level': level,
                'school': school,
                'cast_time': cast_time,
                'range': spell_range,
                'duration': duration,
                'verbal': verbal,
                'somatic': somatic,
                'material': material,
                'material_cost': material_cost,
                'description': description
            }
    return spell_dict

def select_random_spells_with_common_attribute(spell_dict):
    while True:
        # Select a random attribute from the spell dictionary, excluding 'description'
        attribute = random.choice([key for key in spell_dict[next(iter(spell_dict))].keys() if key != 'description'])
        # Extract all unique values for the chosen attribute
        unique_attribute_values = list(set(spell[attribute] for spell in spell_dict.values()))
        # Randomly select one unique value for the chosen attribute
        chosen_value = random.choice(unique_attribute_values)
        # Select spells that have the chosen attribute value
        selected_spells = [spell_name for spell_name, spell_info in spell_dict.items() if spell_info[attribute] == chosen_value]
        # If there are less than 4 spells, try again with a new random attribute and value
        if len(selected_spells) == 4:
            return attribute, chosen_value, selected_spells



spell_sets = {}
used_spells = set()  # Keep track of used spells to avoid duplicates
i = 0
while i < 4:
    csv_file = 'dnd-spells.csv'  
    spell_dictionary = csv_to_spell_dict(csv_file)
    attribute, value, spells = select_random_spells_with_common_attribute(spell_dictionary)
    # Ensure selected spells are unique across all sets
    unique_spells = [spell for spell in spells if spell not in used_spells]
    if len(unique_spells) < 4:
        # If there are not enough unique spells, try again with a new set
        continue
    spell_sets[f"Set {i+1}"] = {"attribute": attribute, "value": value, "spells": unique_spells}
    # Add used spells to the set to avoid duplicates
    used_spells.update(unique_spells)
    i += 1

# Write the spell sets into a JSON file
output_file = 'spell_sets.json'
with open(output_file, 'w') as json_file:
    json.dump(spell_sets, json_file, indent=4)

print("Spell sets have been saved to", output_file)