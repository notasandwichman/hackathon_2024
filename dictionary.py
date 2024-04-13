import csv

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

# Example usage:
csv_file = 'spells.csv'  # Path to your CSV file
spell_dictionary = csv_to_spell_dict(csv_file)

# Test the result by printing the dictionary for a specific spell
print(spell_dictionary['Acid Splash'])
