#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime
import os
from common import generate_spells_out_json

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
