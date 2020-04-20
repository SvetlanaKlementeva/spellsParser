#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
import string


def generate_spell_item(spell_id, lvl, item_name, item_value):
    return {
            "name": "repeating_spell-" + lvl + "_-" + spell_id + "_"+ item_name,
            "current": item_value,
            "max": "",
            "id": "-" + generate_id(19)
        }


def generate_id(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


spell_schools = {'ограждение': "abjuration",
                 'Ограждение': "abjuration",
                 "Преграждение": "abjuration",
                 "призыв": "conjuration",
                 "Призыв": "conjuration",
                 "вызов": "conjuration",
                 "Воплощение": "conjuration",
                 "прорицание": "divination",
                 "Прорицание": "divination",
                 "очарование": "enchantment",
                 "Очарование": "enchantment",
                 "проявление": "evocation",
                 "Проявление": "evocation",
                 "Эвокация": "evocation",
                 "иллюзия": "illusion",
                 "Иллюзия": "illusion",
                 "некромантия": "necromancy",
                 "Некромантия": "necromancy",
                 "преобразование": "transmutation",
                 "Преобразование": "transmutation",
                 "Превращение": "transmutation"
                 }


def generate_spell(input_spell_json):
    spell_id = generate_id(19)

    if input_spell_json['level'] == "0":
        lvl = "cantrip"
    else:
        lvl = input_spell_json['level']

    spellcomp_v = "{{v=1}}"
    spellcomp_s = "{{s=1}}"
    spellcomp_m = "{{m=1}}"

    if input_spell_json.get('components') is not None:
        components = input_spell_json['components']
        if components.find("В") == -1:
            spellcomp_v = "0"
        if components.find("С") == -1:
            spellcomp_s = "0"
        if components.find("M") == -1:
            spellcomp_m = "0"

    if input_spell_json.get('source') is None:
        spellsource = ""
    else:
        spellsource = input_spell_json.get('source')

    name = generate_spell_item(spell_id, lvl, "spellname", input_spell_json['name'].upper())
    school = generate_spell_item(spell_id, lvl, "spellschool", spell_schools[input_spell_json['school']])
    casting_time = generate_spell_item(spell_id, lvl, "spellcastingtime", input_spell_json['castingTime'])
    spell_range = generate_spell_item(spell_id, lvl, "spellrange",  input_spell_json['range'])
    target = generate_spell_item(spell_id, lvl, "spelltarget", "")
    materials = generate_spell_item(spell_id, lvl, "spellcomp_materials", input_spell_json.get('materials'))
    text = generate_spell_item(spell_id, lvl, "spelldescription", input_spell_json['text'])
    duration = generate_spell_item(spell_id, lvl, "spellduration", input_spell_json['duration'])
    comp_v = generate_spell_item(spell_id, lvl, "spellcomp_v", spellcomp_v)
    comp_s = generate_spell_item(spell_id, lvl, "spellcomp_s", spellcomp_s)
    comp_m = generate_spell_item(spell_id, lvl, "spellcomp_m", spellcomp_m)
    source = generate_spell_item(spell_id, lvl, "spellsource", spellsource)

    options_flag = generate_spell_item(spell_id, lvl, "options-flag", "0")

    return [name, school, casting_time, spell_range, target, materials, text, duration, comp_v, comp_s, comp_m, source,
            options_flag]


with open('someSpells.json', encoding='utf-8', newline='') as f:
    spells = json.load(f)

out_db = {}

for spell in spells['allSpells']:
    spell_out = generate_spell(spell['ru'])
    out_db.update({spell['ru']['name'].upper(): spell_out})
    out_db.update({spell['en']['name'].upper(): spell_out})


with open('all_spells_db.json', 'w') as f:
     json.dump(out_db, f, indent=2, ensure_ascii=False)
