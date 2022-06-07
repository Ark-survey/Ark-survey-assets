import json

new_table = {}
with open('source/character_table.json',encoding='utf-8') as f:
  character_table = json.load(f)
  for key in character_table:
    if(key[0] == 'c'):
      del character_table[key]['phases']
      del character_table[key]['talents']
      del character_table[key]['potentialItemId']
      del character_table[key]['canUseGeneralPotentialItem']
      del character_table[key]['trait']
      del character_table[key]['potentialRanks']
      del character_table[key]['favorKeyFrames']
      del character_table[key]['allSkillLvlup']
      del character_table[key]['description']
      del character_table[key]['displayNumber']
      del character_table[key]['tokenKey']
      del character_table[key]['itemUsage']
      del character_table[key]['itemDesc']
      del character_table[key]['itemObtainApproach']
      del character_table[key]['groupId']
      del character_table[key]['teamId']
      del character_table[key]['appellation']
      c = {}
      for key2 in character_table[key]['skills']:
        c[key2['skillId']] = {}
      character_table[key]['skills'] = c
      character_table[key]['equips'] = {}
      character_table[key]['skins'] = {}
      new_table[key] = character_table[key]
      
      
with open('source/skill_table.json',encoding='utf-8') as f:
  skill_table = json.load(f)
  for key in new_table:
    i = 0
    for key2 in new_table[key]['skills']:
      new_table[key]['skills'][key2] ={ 'index': i,'name': skill_table[key2]['levels'][0]['name'] }
      i += 1

with open('source/uniequip_table.json',encoding='utf-8') as f:
  uniequip_table = json.load(f)
  for key in uniequip_table['equipDict']:
    charId = uniequip_table['equipDict'][key]['charId']
    new_table[charId]['equips'][key] = {
      'name': uniequip_table['equipDict'][key]['uniEquipName'],
      'typeIcon': uniequip_table['equipDict'][key]['typeIcon'],
    }
    
with open('source/skin_table.json',encoding='utf-8') as f:
  skin_table = json.load(f)
  for key in skin_table['charSkins']:
    if(key[0] == 'c'):
      charId = skin_table['charSkins'][key]['charId']
      new_table[charId]['skins'][skin_table['charSkins'][key]['avatarId']] = {
        'name': skin_table['charSkins'][key]['displaySkin']['skinName'],
      }
      
with open('game-data/character_table.json', 'w') as file:
  json.dump(new_table, file)