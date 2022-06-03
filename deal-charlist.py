import json

with open('character_table.json') as f:
  character_table = json.load(f)
  a = {}
  for key in character_table:
    if(key[0] == 'c'):
      print(key, ":", key)
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
      del character_table[key]['isNotObtainable']
      del character_table[key]['itemObtainApproach']
      del character_table[key]['groupId']
      del character_table[key]['teamId']
      del character_table[key]['appellation']
      c = []
      for key2 in character_table[key]['skills']:
        c.append(key2['skillId'])
      character_table[key]['skills'] = c
      a[key] = character_table[key]
      
with open('character_table_new.json', 'w') as file:
  json.dump(a, file)