#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from common import generate_id
from math import floor
# import generate_spells_from_list
from common import generate_spells_out_json

with open('someMonsters.json', encoding='utf-8', newline='') as f:
    monsters = json.load(f)

print(len(monsters['dataList']))
# print(monsters['dataList'][1])

for monster_json in monsters['dataList']:

    def generate_monster_item(item_name, item_value, item_max=""):
        return {
            "name": item_name,
            "current": item_value,
            "max": item_max,
            "id": "-" + generate_id(19)
        }


    def generate_monster_action_item(action_id, item_name, item_value):
        return {
            "name": "repeating_npcaction_-" + action_id + "_" + item_name,
            "current": item_value,
            "max": "",
            "id": "-" + generate_id(19)
        }


    def generate_monster_trait_item(trait_id, item_name, item_value):
        return {
            "name": "repeating_npctrait_-" + trait_id + "_" + item_name,
            "current": item_value,
            "max": "",
            "id": "-" + generate_id(19)
        }


    characteristics = {"strength": "str",
                       "dexterity": "dex",
                       "constitution": "con",
                       "intelligence": "int",
                       "wisdom": "wis",
                       "charisma": "cha"
                       }

    skills_map = {"Акробатика": "acrobatics",
                  "Исследование": "investigation",
                  "Атлетика": "athletics",
                  "Восприятие": "perception",
                  "Внимательность": "perception",
                  "Выживание": "survival",
                  "Выступление": "performance",
                  "Запугивание": "intimidation",
                  "История": "history",
                  "Ловкость рук": "sleight_of_hand",
                  "Ловкость Рук": "sleight_of_hand",
                  "Магия": "arcana",
                  "Медицина": "medicine",
                  "Обман": "deception",
                  "Природа": "nature",
                  "Проницательность": "insight",
                  "Религия": "religion",
                  "Скрытность": "stealth",
                  "Убеждение": "persuasion",
                  "Уход за животными": "animal_handling",

                  "Acrobatics": "acrobatics",
                  "Investigation": "investigation",
                  "Athletics": "athletics",
                  "Perception": "perception",
                  "Survival": "survival",
                  "Performance": "performance",
                  "Intimidation": "intimidation",
                  "History": "history",
                  "Sleight of hand": "sleight_of_hand",
                  "Sleight of Hand": "sleight_of_hand",
                  "Arcana": "arcana",
                  "Medicine": "medicine",
                  "Deception": "deception",
                  "Nature": "nature",
                  "Insight": "insight",
                  "Religion": "religion",
                  "Stealth": "stealth",
                  "Persuasion": "persuasion",
                  "Animal handling": "animal_handling"
                  }

    saves = {"Сил": "str",
             "Лов": "dex",
             "Тел": "con",
             "Инт": "int",
             "Мдр": "wis",
             "Муд": "wis",
             "Хар": "cha",

             "Сила": "str",
             "Ловкость": "dex",
             "Телосложение": "con",
             "Интеллект": "int",
             "Мудрость": "wis",
             "Харизма": "cha",

             "Str": "str",
             "Dex": "dex",
             "Con": "con",
             "Int": "int",
             "Wis": "wis",
             "Cha": "cha"
             }


    def generate_characteristic(characteristic_name, value):
        base = generate_monster_item(characteristic_name + "_base", value)
        flag = generate_monster_item(characteristic_name + "_flag", "0")
        characteristic_value = generate_monster_item(characteristic_name, int(value))
        mod_value = floor((int(value) - 10) / 2)
        mod = generate_monster_item(characteristic_name + "_mod", mod_value)
        is_negative = 1 if mod_value < 0 else 0
        negative = generate_monster_item("npc_" + characteristics[characteristic_name] + "_negative", is_negative)
        return [base, flag, characteristic_value, mod, negative]

    def generate_skill(skill_name, value):
        base = generate_monster_item("npc_" + skill_name + "_base", value)
        # is_negative = 1 if int(value) > 0 else 3
        flag = generate_monster_item("npc_" + skill_name + "_flag", "1")
        characteristic_value = generate_monster_item("npc_" + skill_name, int(value))
        return [base, flag, characteristic_value]

    def generate_save(save_name, value):
        base = generate_monster_item("npc_" + save_name + "_save_base", value)
        # is_negative = 1 if int(value) > 0 else 3
        flag = generate_monster_item("npc_" + save_name + "_save_flag", 1)
        characteristic_value = generate_monster_item("npc_" + save_name + "_save", int(value))
        return [base, flag, characteristic_value]

    print(monster_json)
    # monster_json = monsters['dataList'][1]

    is_npc = generate_monster_item("npc", "1")

    name = generate_monster_item("npc_name", monster_json['name'])

    type = generate_monster_item("npc_type", monster_json['type'] + " "
                                 + monster_json['alignment'])
    speed = generate_monster_item("npc_speed", monster_json['speed'])

    hp_value = monster_json['hp'].split(" (")[0]
    hp = generate_monster_item("hp", "", hp_value)

    ac = generate_monster_item("npc_ac", monster_json['ac'])

    ac2 = generate_monster_item("ac", monster_json['ac'])

    language = "" if monster_json.get('languages') is None else monster_json['languages']
    languages = generate_monster_item("npc_languages", language)

    challenge = generate_monster_item("npc_challenge", monster_json['cr'])

    passive_wisdom = generate_monster_item("passive_wisdom", monster_json['cr'])

    strength = generate_characteristic("strength", monster_json['str'])
    dexterity = generate_characteristic("dexterity", monster_json['dex'])
    constitution = generate_characteristic("constitution", monster_json['con'])
    intelligence = generate_characteristic("intelligence", monster_json['int'])
    wisdom = generate_characteristic("wisdom", monster_json['wis'])
    charisma = generate_characteristic("charisma", monster_json['cha'])

    characteristics = [strength, dexterity, constitution, intelligence, wisdom, charisma]

    initiative_bonus = generate_monster_item("initiative_bonus", floor((int(monster_json['dex'])-10) / 2))

    if monster_json.get('image') is not None:
        if isinstance(monster_json.get('image'), str):
            image = monster_json['image'].split(".")[0].upper() + ".jpg"
        else:
            image = monster_json['image']['src'].split(".")[0].upper() + ".jpg"
    else:
        if monster_json['name'].find("(") != -1:
            image = monster_json['name'].split("(")[1].split(")")[0].upper().replace(" ", "_").replace("/", "_") + ".jpg"
        else:
            if monster_json['name'].find("[") != -1:
                image = monster_json['name'].split("[")[1].split("]")[0].upper().replace(" ", "_").replace("/", "_") + ".jpg"
            else:
                image = ""
    hitdieroll = generate_monster_item("hitdieroll", "4")
    version = generate_monster_item("version", 4.21)
    appliedUpdates = generate_monster_item("appliedUpdates", "upgrade_to_4_2_1")
    mancer_confirm_flag = generate_monster_item("mancer_confirm_flag", "")
    mancer_npc = generate_monster_item("mancer_npc", "on")
    l1mancer_status = generate_monster_item("l1mancer_status", "completed")
    dtype = generate_monster_item("dtype", "full")
    rtype = generate_monster_item("rtype", "@{advantagetoggle}")

    npc_options_flag = generate_monster_item("npc_options-flag", "0")
    ui_flags = generate_monster_item("ui_flags", "")
    showleveler = generate_monster_item("showleveler", 0)
    invalidXP = generate_monster_item("invalidXP", 0)

    attributes = [hitdieroll, showleveler, invalidXP, version, mancer_confirm_flag, mancer_npc, l1mancer_status,
                  rtype, dtype, appliedUpdates, is_npc, npc_options_flag, ui_flags, name, type, speed, hp,
                  ac, ac2, languages, challenge, passive_wisdom, initiative_bonus]

    if monster_json['hp'].find("(") != -1:
        hp_dice = monster_json['hp'].split("(")[1].split(")")[0].replace("к", "d")
        hp_formula = generate_monster_item("npc_hpformula", hp_dice)
        attributes.append(hp_formula)

    for characteristic in characteristics:
        for item in characteristic:
            attributes.append(item)

    if monster_json.get('skill') is not None:
        npc_skills_flag = generate_monster_item("npc_skills_flag", 3)
        attributes.append(npc_skills_flag)
        skills_list = monster_json['skill'].split(", ")
        for skill in skills_list:
            skills_items = generate_skill(skills_map[skill.split(" +")[0]], skill.split(" +")[1])
            for skill_item in skills_items:
                attributes.append(skill_item)

    if monster_json.get('save') is not None:
        npc_saving_flag = generate_monster_item("npc_saving_flag", 7)
        attributes.append(npc_saving_flag)
        saves_list = monster_json['save'].split(", ")
        for save in saves_list:
            save_items = generate_save(saves[save.split(" +")[0]], save.split(" +")[1])
            for save_item in save_items:
                attributes.append(save_item)

    if monster_json.get('resist') is not None:
        resistances = generate_monster_item("npc_resistances", monster_json.get('resist'))
        attributes.append(resistances)

    if monster_json.get('immune') is not None:
        immunities = generate_monster_item("npc_immunities", monster_json.get('immune'))
        attributes.append(immunities)

    if monster_json.get('conditionImmune') is not None:
        conditionImmune = generate_monster_item("npc_condition_immunities", monster_json.get('conditionImmune'))
        attributes.append(conditionImmune)

    if monster_json.get('vulnerable') is not None:
        vulnerabilities = generate_monster_item("npc_vulnerabilities", monster_json.get('vulnerable'))
        attributes.append(vulnerabilities)

    if monster_json.get('senses') is not None:
        senses = generate_monster_item("npc_senses", monster_json.get('senses'))
        attributes.append(senses)


    def add_action(action_json):
        if action_json.get('attack') is not None:
            if isinstance(action_json['attack'], list):
                for attack in action_json['attack']:
                    action_id = generate_id(19)
                    action_name = generate_monster_action_item(action_id, "name", action_json['name']
                                                               + " (" + attack.split("|")[0] + ")")
                    attributes.append(action_name)
                    if isinstance(action_json['text'], list):
                        action_text = ""
                        for action_text_item in action_json['text']:
                            action_text += action_text_item.replace("<i>", "\n").replace("</i>", "\n") + "\n\n"

                    else:
                        action_text = action_json['text'].replace("<i>", "\n").replace("</i>", "\n")

                    action_description = generate_monster_action_item(action_id, "description", action_text)
                    attributes.append(action_description)

                    action_attack_flag = generate_monster_action_item(action_id, "attack_flag", "on")
                    attributes.append(action_attack_flag)
                    attack_tohitrange = generate_monster_action_item(action_id, "attack_tohitrange",
                                                                     "+" + attack.split("|")[1])
                    attributes.append(attack_tohitrange)
                    damage = attack.split("|")[2]
                    attack_onhit = generate_monster_action_item(action_id, "attack_onhit", "")
                    attributes.append(attack_onhit)
                    attack_tohit = generate_monster_action_item(action_id, "attack_tohit", attack.split("|")[1])
                    attributes.append(attack_tohit)
                    action_damage = generate_monster_action_item(action_id, "attack_damage", damage)
                    attributes.append(action_damage)
                    action_damage_flag = generate_monster_action_item(action_id, "damage_flag",
                                                                      "{{damage=1}} {{dmg1flag=1}}")
                    attributes.append(action_damage_flag)
                    attack_rollbase = "@{wtype}&{template:npcaction} {{attack=1}} @{damage_flag} " \
                                      "@{npc_name_flag} {{rname=@{name}}} {{r1=[[@{d20}+(@{attack_tohit})]]}} " \
                                      "@{rtype}+(@{attack_tohit})]]}} {{dmg1=[[@{attack_damage}]]}} " \
                                      "{{dmg1type=@{attack_damagetype}}} {{dmg2=[[@{attack_damage2}+0]]}} " \
                                      "{{dmg2type=@{attack_damagetype2}}} {{crit1=[[@{attack_crit}+0]]}} " \
                                      "{{crit2=[[@{attack_crit2}+0]]}} {{description=@{show_desc}}} @{charname_output}"
                    rollbase = generate_monster_action_item(action_id, "rollbase", attack_rollbase)
                    attributes.append(rollbase)
                    crit1 = generate_monster_action_item(action_id, "attack_crit", attack.split("|")[2])
                    attributes.append(crit1)
                    crit2 = generate_monster_action_item(action_id, "attack_crit2", "")
                    attributes.append(crit2)

            else:
                action_id = generate_id(19)
                action_name = generate_monster_action_item(action_id, "name", action_json['name'])
                attributes.append(action_name)
                if isinstance(action_json['text'], list):
                    action_text = ""
                    for action_text_item in action_json['text']:
                        action_text += action_text_item.replace("<i>", "\n").replace("</i>", "\n") + "\n\n"

                else:
                    action_text = action_json['text'].replace("<i>", "\n").replace("</i>", "\n")
                action_description = generate_monster_action_item(action_id, "description", action_text)
                attributes.append(action_description)

                action_attack_flag = generate_monster_action_item(action_id, "attack_flag", "on")
                attributes.append(action_attack_flag)
                attack_tohitrange = generate_monster_action_item(action_id, "attack_tohitrange",
                                                                 "+" + action_json['attack'].split("|")[1])
                attributes.append(attack_tohitrange)
                damage = action_json['attack'].split("|")[2]
                attack_onhit = generate_monster_action_item(action_id, "attack_onhit", "")
                attributes.append(attack_onhit)
                attack_tohit = generate_monster_action_item(action_id, "attack_tohit", action_json['attack'].split("|")[1])
                attributes.append(attack_tohit)
                action_damage = generate_monster_action_item(action_id, "attack_damage", damage)
                attributes.append(action_damage)
                action_damage_flag = generate_monster_action_item(action_id, "damage_flag",
                                                                  "{{damage=1}} {{dmg1flag=1}}")
                attributes.append(action_damage_flag)
                attack_rollbase = "@{wtype}&{template:npcaction} {{attack=1}} @{damage_flag} " \
                                  "@{npc_name_flag} {{rname=@{name}}} {{r1=[[@{d20}+(@{attack_tohit})]]}} " \
                                  "@{rtype}+(@{attack_tohit})]]}} {{dmg1=[[@{attack_damage}]]}} " \
                                  "{{dmg1type=@{attack_damagetype}}} {{dmg2=[[@{attack_damage2}+0]]}} " \
                                  "{{dmg2type=@{attack_damagetype2}}} {{crit1=[[@{attack_crit}+0]]}} " \
                                  "{{crit2=[[@{attack_crit2}+0]]}} {{description=@{show_desc}}} @{charname_output}"
                rollbase = generate_monster_action_item(action_id, "rollbase", attack_rollbase)
                attributes.append(rollbase)
                crit1 = generate_monster_action_item(action_id, "attack_crit", action_json['attack'].split("|")[2])
                attributes.append(crit1)
                crit2 = generate_monster_action_item(action_id, "attack_crit2", "")
                attributes.append(crit2)
        else:
            action_id = generate_id(19)
            action_name = generate_monster_action_item(action_id, "name", action_json['name'])
            attributes.append(action_name)
            action_description = generate_monster_action_item(action_id, "description", action_json['text'])
            attributes.append(action_description)
            attack_tohitrange = generate_monster_action_item(action_id, "attack_tohitrange", "+0")
            attributes.append(attack_tohitrange)
            attack_onhit = generate_monster_action_item(action_id, "attack_onhit", "")
            attributes.append(attack_onhit)
            action_damage_flag = generate_monster_action_item(action_id, "damage_flag", "")
            attributes.append(action_damage_flag)

            crit1 = generate_monster_action_item(action_id, "attack_crit", "")
            attributes.append(crit1)
            crit2 = generate_monster_action_item(action_id, "attack_crit2", "")
            attributes.append(crit2)

            attack_rollbase = "@{wtype}&{template:npcaction} @{npc_name_flag} {{rname=@{name}}} " \
                              "{{description=@{show_desc}}} @{charname_output}"

            rollbase = generate_monster_action_item(action_id, "rollbase", attack_rollbase)
            attributes.append(rollbase)


    if monster_json.get('action') is not None:
        actions = monster_json.get('action')
        if actions is not None and isinstance(actions, dict):
            add_action(actions)
        else:
            if actions is not None:
                for action in actions:
                    add_action(action)

    def add_trait(trait_json):
        is_spell = 0
        # if trait_json.get('attack') is not None:
        #     add_action(trait_json)
        # else:
        trait_id = generate_id(19)
        trait_name = generate_monster_trait_item(trait_id, "name", trait_json['name'])
        attributes.append(trait_name)
        trait_text = trait_json['text']

        text = ""
        if isinstance(trait_text, list):
            for trait_text_item in trait_text:
                text += trait_text_item.replace("<br>", "\n\n").replace("<i>", "\n").replace("</i>", "\n") + "\n\n"
                if trait_text_item.find("<a href='https://tentaculus.ru/spells/#q=") != -1:
                    text = text.replace("<a href='https://tentaculus.ru/spells/#q=", "")
                    text = text.replace("'>", "")
                    text = text.replace("&view=text", "")
                    text = text.replace("</a>", ": ")
                    is_spell += 1
                    spells_links = trait_text_item.split("<a href='https://tentaculus.ru/spells/#q=")
                    spells = []
                    spells_links.pop(0)
                    for spell in spells_links:
                        spells.append(spell.split("'>")[0].replace('&view=text', "").replace("_", " "))
                        text = text.replace(spell.split("'>")[0] + "'", "")
                    spells_json = generate_spells_out_json(spells)
                    for spell_item in spells_json:
                        attributes.append(spell_item)

        else:
            text += trait_text.replace("<br>", "\n\n").replace("<i>", "\n").replace("</i>", "")
            if trait_text.find("<a href='https://tentaculus.ru/spells/#q=") != -1:
                text = text.replace("<a href='https://tentaculus.ru/spells/#q=", "")
                text = text.replace("</a>", "")
                is_spell += 1
                spells_links = trait_text.split("<a href='https://tentaculus.ru/spells/#q=")
                spells = []
                spells_links.pop(0)
                for spell in spells_links:
                    spells.append(spell.split("'>")[0].replace('&view=text', "").replace("_", " "))
                    text = text.replace(spell.split("'>")[0] + "'", "")
                spells_json = generate_spells_out_json(spells)
                for spell_item in spells_json:
                    attributes.append(spell_item)

        trait_desc = generate_monster_trait_item(trait_id, "description", text)
        attributes.append(trait_desc)
        return is_spell


    if monster_json.get('trait') is not None:
        spellcasting = 0
        traits = monster_json.get('trait')
        if traits is not None and isinstance(traits, dict):
            spellcasting += add_trait(traits)
        else:
            if traits is not None:
                for trait in traits:
                    spellcasting += add_trait(trait)
        is_spell_value = "1" if spellcasting > 0 else "0"
        npcspellcastingflag = generate_monster_item("npcspellcastingflag", is_spell_value)
        attributes.append(npcspellcastingflag)

    fiction = "" if monster_json.get('fiction') is None else monster_json['fiction']

    out = {"schema_version": 2, "oldId": "-" + generate_id(19), "name": monster_json['name'],
           "avatar": "https://tentaculus.ru/monsters/img/cute_monsters/" + image, "bio": fiction,
           "gmnotes": "", "defaulttoken": "", "tags": "[]", "controlledby": "", "inplayerjournals": "",
           "attribs": attributes, "abilities": []}

    with open('./monsters/' + monster_json['name'].replace("/", ",") + '.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=4, ensure_ascii=False)



