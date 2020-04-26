import json
import random
import string


def generate_id(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


def generate_spells_out_json(input_spells_json):
    out_json = []
    with open('all_spells_db.json') as f:
        all_spells = json.load(f)
    for input_spell in input_spells_json:
        if all_spells.get(input_spell.upper()) is not None:
            for item in all_spells[input_spell.upper()]:
                out_json.append(item)
            print("[INFO] Spell with name '" + input_spell + "' added")
        else:
            print("[ERROR] Spell with name '" + input_spell + "' not found in DB!!")
    return out_json
