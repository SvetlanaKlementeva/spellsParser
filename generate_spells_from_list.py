#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime
import os

def generate_spells_out_json(input_spells_json):
    out_json = []
    for input_spell in input_spells_json:
        if all_spells.get(input_spell.upper()) is not None:
            for item in all_spells[input_spell.upper()]:
                out_json.append(item)
            print("[INFO] Spell with name '" + input_spell + "' added")
        else:
            print("[ERROR] Spell with name '" + input_spell + "' not found in DB!!")
    return out_json


with open('all_spells_db.json') as f:
    all_spells = json.load(f)

print(
    'Enter spell names separated by a comma (, )\n'
    'For example "Волшебная рука, prestidigitation, НЕЧИТАЕМАЯ ФИГНЯ, ray of frost":\n'
    'Your spells:\n')
input_spells_sting = input()
print("\n")
input_spells = input_spells_sting.split(", ")

out = generate_spells_out_json(input_spells)

timestamp = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
out_file_name = 'spells_for_npc(' + timestamp + ').json'

with open(out_file_name, 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("\nFinished!!")
print("Get your spells from [" + out_file_name + "] file")
print("P.S. Please remove '[' and ']' symbols in the begin and end of file before copy spells to import file")

os.system('pause')