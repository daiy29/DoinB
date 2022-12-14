from helpers import jsonLoader
my_file = './assets/summoner.json'

def getTotalSummonerHaste(has_ionians,has_cosmic):
    total_haste = 0
    if has_ionians:
        total_haste += 12
    if has_cosmic:
        total_haste += 18
    return total_haste

def hasteMultiplier(haste):
    return 100/(100+haste)

def getCDFromSpell(spell_name): 
    data = jsonLoader(my_file)
    for spells in data:
        if spells["name"] == spell_name:
            return spells["cooldown"]
    
def calculateNewHaste(summoner_spell, item_id, rune_id):
    base_cd = getCDFromSpell(summoner_spell)
    haste = getTotalSummonerHaste(item_id,rune_id)
    new_cd = hasteMultiplier(haste) * base_cd
    return new_cd

