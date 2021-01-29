import discord
from discord.ext import commands
import random
from discord.ext.commands import cooldown, BucketType
import copy

def calculate(secs):
    seconds = 0
    minutes = 0
    hours = 0
    integer = int(secs /60)
    modulo = int(secs % 60)
    seconds = modulo
    integer = int(integer/60)
    modulo = int(integer % 60)
    minutes = modulo
    hours = integer
    total = f'{hours}h {minutes}m {seconds}s'
    return total

def fightcal(x, y, area):
    global area2
    area2 = area.split()
    return area2[x+((y-1)*9)]

class User:
    def __init__(self, name):
        self.tutorial = 0
        self.name = name
        self.coins = 0
        self.items = {}
        self.inventory_print = ''
        self.current_monster_hp = 0
        self.is_alive = True
        self.hp = 100
        self.total_hp = 100
        self.xp = 0
        self.level = 1
        self.required_xp = 10
        self.attack = 1
        self.ranged_attack = 1
        self.defense = 5
        self.randomator = 0
        self.is_leveling = False
        self.current_location = ''
        self.current_scavenge = ''
        self.stage = 1
        self.max_stage = 1
        self.area = areas[self.stage-1]
        self.amount1 = 0
        self.amount2 = 0
        self.randomator2 = 0
        self.swords = {'Melee': {'Name': 'None', 'Value': 0, 'Accuracy': 100}, 'Ranged': {'Name': 'None', 'Value': 0, 'Accuracy': 100}, 'Axe': {'Name': 'Old axe', 'Value': 1}, 'Pickaxe': {'Name': 'None', 'Value': 0}, 'Rods': {'Name': 'None', 'Value': 1}}
        self.armour = {'Armour1': {'Name': 'None', 'Value': 0}}
        self.axe = 1
        self.pickaxe = 0
        self.rod = 1
        self.current_recipes = None
        self.required_items = None
        self.all_calculate = float('inf')
        self.equip_checklist = None
        self.printthing = ''
        self.damage = 0
        self.total_damage = 0
        self.monster_stage = 0
        self.monster_alive = True
        self.running = False
        self.attack2 = 0
        self.command_list = []
        self.inventory_print2 = ''
        self.command_print = ''''''
        self.count = 0
        self.current_item = None
        self.current_items = {}
        self.current_item_amount = 0
        self.items_prevalues = []
        self.items_values = {}
        self.count2 = 0
        self.is_staging = False
        self.monster = None
        self.current_trades = None
        self.trading_stage = 0
        self.current_trade = None
        self.letter_check = ''
        self.trade_index = 0
        self.trade_amount = 0
        self.the_trade = None
        self.the_trade_amount = None
        self.finished_trade = False
        self.backup_recipes = None
        self.monster_drop = None
        self.monster_dropping = False
        self.material_no = 0
        self.craft_no = 0
        self.hunt_no = 0
        self.current_achievement = None
        self.material_achievements = {'A Material Start': [3, False, [10, 5]], 'A Gathering Newbie': [20, False, [50, 10]]}
        self.donation_achievements = {'Kindness': [1000, False, [300, 100]], 'Giveaway Novice': [5000, False, [1500, 500]]}
        self.crafting_achievements = {'A Crafty Start': [1, False, [10, 5]], 'Crafting Novice': [10, False, [400, 50]]}
        self.hunting_achievements = {'Normie Hunter': [1, False, [10, 5]], 'A Monster\'s Nightmare': [20, False, [1900, 550]]}
        self.level_achievements = {'Leveling Noob': [10, False, [1000, 20]], 'Leveling Player': [20, False, [3500, 600]], 'Leveling Try Hard': [40, False, [750000, 7000]], 'Leveling Pro': [], 'Leveling Sweat': []}
        self.remaining_xp = 0
        self.weapon_values = {'old sword': [2, 70, 0, 100],
                             'wooden sword': [5, 90, 0, 100],
                         'fishbone rapier': [12, 90, 0, 100],
                         'stone bone sword': [20, 90, 0, 100],
                         'iron sword': [35, 95, 0, 100]}
        self.axe_values = {'old axe': 1,
                      'wooden axe': 2,
                      'stone axe': 4,
                      'iron axe': 8}
        self.pickaxe_values = {
                         'wooden pickaxe': 1,
                         'stone pickaxe': 2,
                         'iron pickaxe': 4
                         }
        self.armour_values = {'wooden armour': 5,
                         'fish scale armour': 12,
                         'stone bone armour': 20,
                         'iron armour': 35}
        self.rod_values = {
                    'wooden fishing rod': 2,
                    'fishbone fishing rod': 4,
                    'iron fishing rod': 8
                    }
        self.ranged_values = {
                        'crab launcher': [15, 50, 0, 100]
                        }
        self.xp_tr_cost = 100
        self.melee_tr_cost = 100
        self.ranged_tr_cost = 100
        self.training_type = None
        self.training_stage = 0
        self.fight_map = 0
        self.fight_map_pic = ''
        self.fight_stage = 0
        self.opponent = None
        self.fight_stat = None
        self.can_attack = False
        self.fight_hp = self.hp
        self.fight_hp2 = self.hp
        self.fight_turn = None
        self.position = [0, 0]
        self.fight_fin = False
        self.op_mem = None
        self.fight_dead = False
        self.shot_path = []
        self.ended = False
        self.fight_map_pic_edits = None
        self.id = 0
        self.is_healing = False
        self.is_chancing = False
        self.fight_def = self.defense
        self.fight_atk = self.attack
        self.heal_count = 0
        self.shield_count = 0
    def add_coins(self, amount):
        self.coins += amount
    def add_item(self, item_name, item_amount):
        if item_name in self.items:
            self.items[item_name] += item_amount
        else:
            self.items[item_name] = item_amount
    def remove_item(self, item_name, item_amount):
        if item_name in self.items:
            if self.items[item_name] >= item_amount:
                self.items[item_name] -= item_amount
                if self.items[item_name] == 0:
                    del self.items[item_name]
    def try_level(self):
        if self.xp >= self.required_xp:
            self.remaining_xp = self.xp - self.required_xp
            self.is_leveling = True
            self.total_hp += 10
            self.hp += 10
            self.defense += 1
            self.attack += 1
            self.required_xp = self.stage*self.level*150
            self.xp = 0
            self.level += 1
            self.xp += self.remaining_xp
            if self.level == 3:
                self.max_stage += 1
                self.stage = self.max_stage
                self.is_staging = True
            if self.level%10 == 0 and self.level != 10:
                self.stage += 1
                self.is_staging = True
            self.try_level()
    def try_material(self):
        self.inventory_print = ''''''
        self.inventory_print2 = ''''''
        for ach, value in self.material_achievements.items():
            if value[1] == False:
                self.current_achievement = [value, ach]
                break
        if self.material_no >= self.current_achievement[0][0]:
            self.xp += self.current_achievement[0][2][0]
            self.coins += self.current_achievement[0][2][1]
            self.inventory_print += f'You have finshed the achievement `{self.current_achievement[1]}`! You gained {self.current_achievement[0][2][0]} EXP and {self.current_achievement[0][2][1]} COINS.'
            self.material_achievements[self.current_achievement[1]][1] = True
        else:
            self.inventory_print = ''''''
            return
    def try_hunt(self):
        self.inventory_print = ''''''
        self.inventory_print2 = ''''''
        for ach, value in self.hunting_achievements.items():
            if value[1] == False:
                self.current_achievement = [value, ach]
                break
        if self.hunt_no >= self.current_achievement[0][0]:
            self.xp += self.current_achievement[0][2][0]
            self.coins += self.current_achievement[0][2][1]
            self.inventory_print += f'You have finshed the achievement `{self.current_achievement[1]}`! You gained {self.current_achievement[0][2][0]} EXP and {self.current_achievement[0][2][1]} COINS.'
            self.hunting_achievements[self.current_achievement[1]][1] = True
        else:
            self.inventory_print = ''''''
            return
    def try_craft(self):
        self.inventory_print = ''''''
        self.inventory_print2 = ''''''
        for ach, value in self.crafting_achievements.items():
            if value[1] == False:
                self.current_achievement = [value, ach]
                break
        if self.craft_no >= self.current_achievement[0][0]:
            self.xp += self.current_achievement[0][2][0]
            self.coins += self.current_achievement[0][2][1]
            self.inventory_print += f'You have finshed the achievement `{self.current_achievement[1]}`! You gained {self.current_achievement[0][2][0]} EXP and {self.current_achievement[0][2][1]} COINS.'
            self.crafting_achievements[self.current_achievement[1]][1] = True
        else:
            self.inventory_print = ''''''
            return


client = commands.Bot(command_prefix='adv ', case_insensitive = True)
client.remove_command('help')
randomator = 0
profile_list = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
emoji_values = {'logs': '<:log:756832919968022600>', 'epic logs': '<:EPIClog:756835059817775155>'}
commands_with_cooldowns = ['chop', 'fish', 'mine', 'scavenge', 'daily', 'pillage', 'trade', 'hunt', 'donate']
tree_emojis = [':christmas_tree:', ':evergreen_tree:', ':deciduous_tree:', ':palm_tree:']
equipment_emojis = [':hiking_boot:', ':helmet_with_cross:', ':goggles:', ':shirt:']
possible_commands = [['chop', 'fish', 'sell', 'dismantle', 'trade', 'buy', 'open'], ['chop', 'fish', 'sell', 'dismantle', 'trade', 'buy', 'open'], ['chop', 'fish', 'mine', 'sell', 'dismantle', 'trade', 'buy', 'open'], ['chop', 'fish', 'sell', 'dismantle', 'trade', 'buy', 'open']]
possible_monsters = [{'sand golem': [], 'big crab': ['crab claw', 1, 5], 'mutant rock': []},
                     {'sand golem': [], 'big crab': ['crab claw', 1, 5], 'mutant rock': []}]
possible_locations = [':blue_book: library :green_book:', 'fish market :fishing_pole_and_fish:']
possible_items = ['logs', 'logs', 'logs', 'fish', 'fish', 'fish', 'stone', 'stone', 'old sword', 'nothing', 'nothing', 'nothing', 'nothing', 'glowing fish', 'glowing fish', 'epic logs', 'epic logs', 'grass', 'grass', 'grass', 'grass']
possible_recipes = [{}, {'wooden sword': {'epic logs': 1, 'logs': 20, 'sticks': 10},
                     'wooden armour': {'epic logs': 5, 'logs': 40, 'sticks': 2},
                     'sticks': {'logs': 2},
                     'golden scales': {'scales': 15},
                     'golden fishbones': {'fishbones': 15},
                     'fishbone rapier': {'fishbones': 100,'golden fishbones': 10,'sticks': 20, 'wooden sword': 1},
                     'fishscale armour': {'wooden armour': 1,'scales': 300, 'golden scales': 40, 'sticks': 2},
                     'wooden pickaxe': {'sticks': 10, 'stone': 10, 'epic logs': 2},
                     'wooden fishing rod': {'epic logs': 10, 'sticks': 50, 'grass': 100},
                     'fishbone fishing rod': {'fishbones': 90, 'epic logs': 15, 'grass': 150},
                     'wooden axe': {'sticks': 20, 'logs': 35, 'epic logs': 15},
                     'crab launcher': {'epic logs': 10, 'special logs': 2, 'crab claw': 1, 'fishbones': 100}
                     },
                    {
                     'stone bone sword': {'stone': 100, 'fishbones': 1000, 'fishbone rapier': 1, 'epic logs': 15},
                     'stone bone armour': {'stone': 200, 'golden fishbones': 50, 'fishscale armour': 1, 'scales': 100, 'golden scales': 40, 'sticks': 20},
                     'iron sword': {'iron': 30, 'stone': 300, 'stone bone sword': 1, 'fishbones': 100, 'epic logs': 10, 'sticks': 20},
                     'iron armour': {'iron': 80, 'stone': 500, 'stone bone armour': 1, 'golden scales': 100},
                     'furnace': {'stone': 150 , 'logs': 100},
                     'blast furnace': {'stone': 500, 'coal': 200, 'logs': 200},
                     'stone axe': {'stone': 200, 'epic logs': 10, 'wooden axe': 1},
                     'stone pickaxe': {'stone': 100, 'epic logs': 10, 'wooden pickaxe': 1},
                     'iron axe': {'iron': 100, 'stone': 500, 'stone axe': 1},
                     'iron pickaxe': {'iron': 100, 'stone': 200, 'stone pickaxe': 1},
                     'iron fishing rod': {'iron': 100, 'sticks': 50, 'fishbone fishing rod': 1, 'grass': 200}
                    }
                    ]
category_dict = {
                'start': 'Utility',
                'help': 'Utility',
                'profile': 'Utility',
                'inv': 'Utility',
                'clear_message': 'Utility',
                'equip': 'Utility',
                'unequip': 'Utility',
                'map': 'Utility',
                'equipment': 'Utility',
                'chop': 'Item',
                'mine': 'Item',
                'fish': 'Item',
                'craft': 'Item',
                'dismantle': 'Item',
                'recipes': 'Item',
                'daily': 'Item',
                'buy': 'Item',
                'shop': 'Item',
                'scavenge': 'Item',
                'pillage': 'Item',
                'trade': 'Item',
                'lootbox': 'Lootbox',
                'open': 'Lootbox',
                'upgrade': 'Lootbox',
                'more': 'Money',
                'sell': 'Money',
                'hunt': 'Fighting',
                'heal': 'Fighting',
                'ready': 'Utility',
                'donate': 'Item'
                }
possible_categories = ['Utility', 'Item', 'Lootbox', 'Money', 'Fighting']
areas = ['The Tutorial', 'The Inland Beach', 'The Mountains', 'The Forest', 'Expert Etherlands']
lop = {'common lootbox': 100, 'rare lootbox': 500, 'epic lootbox': 2500, 'mega lootbox': 10000}
lop2 = [{'logs': 100, 'stone': 200, 'fish': 60, 'regeneration tokens': 50, 'common lootbox': 1000, 'rare lootbox': 10000, 'epic lootbox': 50000, 'mega lootbox': 700000}, {'logs': 50, 'stone': 70, 'fish': 40, 'regeneration tokens': 50, 'common lootbox': 1500, 'rare lootbox': 7500, 'epic lootbox': 60000, 'mega lootbox': 800000, 'grand lootbox': 3000000}]
lootboxes = [{
            'common lootbox': [{'logs': [1, 3], 'epic logs': [1, 1], 'fish': [1, 3], 'glowing fish': [1, 1]}, 2],
            'rare lootbox': [{'logs': [2, 4], 'epic logs': [1, 2], 'fish': [2, 4], 'glowing fish': [1, 2], 'stone': [1, 1], 'fishbones': [8, 3]}, 4], #The format is : {lootbox_name: [{itemname: [highest_possible_amount, chances]}, total_items]}
            'epic lootbox': [{'logs': [3, 4], 'epic logs': [2, 2], 'fish': [3, 4], 'glowing fish': [2, 2], 'stone': [2, 1], 'fishbones': [14, 3], 'golden fishbones': [5, 2]}, 7]
            },
             {
            'common lootbox': [{'logs': [1, 5], 'epic logs': [1, 2], 'fish': [1, 5], 'glowing fish': [1, 2], 'stone': {1, 1}, 'paper': [1, 1]}, 3],
            'rare lootbox': [{'logs': [2, 6], 'epic logs': [1, 2], 'fish': [2, 6], 'glowing fish': [1, 2], 'stone': [1, 2], 'fishbones': [8, 4], 'iron': [1, 1], 'glass': [1, 1], 'common lootbox': [1, 1]}, 5], #The format is : {lootbox_name: [{itemname: [highest_possible_amount, chances]}, total_items]}
            'epic lootbox': [{'logs': [3, 4], 'epic logs': [2, 2], 'fish': [3, 4], 'glowing fish': [2, 2], 'stone': [2, 1], 'fishbones': [14, 3], 'golden fishbones': [5, 2]}, 10],
            'mega lootbox': [{'logs': [8, 8], 'epic logs': [3, 4], 'fish': [7, 8], 'glowing fish': [4, 4], 'stone': [5, 4], 'fishbones': [20, 6], 'golden fishbones': [8, 4], 'grass': [28, 9], 'epic lootbox': [1, 1], 'crab claw': [1, 2]}, 25],
            'trader\'s lootbox': [{'paper': [3, 3], 'gunpowder': [2, 2], 'logs': [4, 4], 'sugar': [1, 2]}, 5]
            }]
trades = [{}, {'beach trader': [[[['logs', 1], ['fish', 1]], [['fish', 1], ['logs', 1]], [['epic logs', 1], ['glowing fish', 1]], [['glowing fish', 1], ['epic logs', 1]], [['logs', 1], ['grass', 2]], [['grass', 2], ['logs', 1]]], 4, 5], #The format is : {trader_name: [{[receiving_name, receiving_amount]: [giving_name, giving_amount]}, chances, max_items]}
               'wandering trader': [[[['logs', 1], ['fish', 2]], [['fish', 4], ['stone', 1]], [['stone', 1], ['fish', 4]]], 1, 3],
               'nothing': [[], 3, 1]}]
sell_values = [{'logs': 20, 'epic logs': 100, 'fish': 20, 'glowing fish': 100, 'stone': 300, 'special logs': 550},
               {'logs': 40, 'epic logs': 160, 'fish': 40, 'glowing fish': 160, 'exotic fish': 600, 'special logs': 600, 'stone': 250, 'paper': 130}]
dismantle_values = {'epic logs': {'logs':[3, 7]}, 'special logs': {'epic logs':[3, 7]}, 'glowing fish': {'golden fishbones':[7, 13], 'golden scales': [8, 14]}, 'fish': {'fishbones': [7, 13], 'scales': [9, 15]}}
area_buffs = [{}, {}, {'mine': 2}, {'chop': 2}, {'scavenge': 2}, {'sell': 2}, {'chop': 4}, {'fish': 2}, {'mine': 4, 'coins': 2}, {'coins': 4, 'chop': 4, 'fish': 4, 'mine': 4, 'scavenge': 4}]
fight1 = [['| 1️⃣ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ |', '| 1️⃣ ⚪ 🟠 ⚪ ⚪ ⚪ ⚪ |']]
fight2 = [['| 🟠 ⚪ ⚪ 🟠 🟠 🟠 💖 |', '| 🟠 ⚪ ⚪ 🟠 🟠 🟠 💖 |']]
fight3 = [['| 🟠 🟠 ⚪ ⚪ 🟠 ⚪ ⚪ |', '| 🟠 🟠 ⚪ ⚪ ⚪ ⚪ ⚪ |']]
fight4 = [['| 🟢 ⚪ 💖 🟠 🟠 🟠 🟠 |', '| 🟢 ⚪ 💖 🟠 ⚪ 🟢 🟠 |']]
fight5 = [['| ⚪ 🟠 ⚪ ⚪ ⚪ ⚪ 🟠 |', '| ⚪ 🟠 ⚪ ⚪ ⚪ ⚪ 🟠 |']]
fight6 = [['| ⚪ 🟠 🟠 ⚪ 🟠 ⚪ 2️⃣ |', '| ⚪ 🟠 🟠 ⚪ 🟠 ⚪ 2️⃣ |']]




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.command(name = 'start', brief = 'Start the game!', description = 'You can only use this command once at the start of the game. it starts your game for you.', aliases = [], usage = 'adv start')
async def start(ctx):
    username, d = str(ctx.author).split('#')
    listy = []
    for x in profile_list:
        listy.append(x)
    for x in profile_list:
        if x.name == username:
            await ctx.channel.send('You are already playing the game!')
            return
    if username not in listy:
        profile_list.append(User(username))
        await ctx.channel.send('You were travelling in a private boat on uncharted waters. Rough winds blew you off course onto an unknown island. Crashing into the shallow reef. Your only sailor drowns and leaves you stranded. Looking for survivors, you found an old axe instead. Type `adv chop` to begin the tutorial.')
    else:
        await ctx.channel.send('You are already in the game!')

@client.command(name = 'achievements', aliases = ['ach'])
async def achievements(ctx, cater='all'):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if cater == 'all':
                embed = discord.Embed(colour=random.randint(0, 0xffffff))
                for ach, value in x.material_achievements.items():
                    if value[1] == True:
                        x.inventory_print += f'{ach} --- :white_check_mark:\n'
                    else:
                        x.inventory_print2 += f'`{ach}`: Obtain materials {value[0]} times. (With `chop`, `fish` and `mine`)\n**Progress:** {x.material_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                        break
                embed.set_author(name=f'{x.name}\'s achievements', icon_url=ctx.author.avatar_url)
                if x.inventory_print != '''''':
                    embed.add_field(name='Previous **material** achievements:', value=x.inventory_print, inline = False)
                embed.add_field(name='The achievement you are working towards:', value=x.inventory_print2, inline = False)
                embed.add_field(name='\u200b', value = '------------------------------------------------------------------------------')
                x.inventory_print = ''''''
                x.inventory_print2 = ''''''
                for ach, value in x.crafting_achievements.items():
                    if value[1] == True:
                        x.inventory_print += f'{ach} --- :white_check_mark:\n'
                    else:
                        x.inventory_print2 += f'`{ach}`: Craft items {value[0]} times. (With `craft`)\n**Progress:** {x.craft_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                        break
                if x.inventory_print != '''''':
                    embed.add_field(name='Previous **crafting** achievements:', value=x.inventory_print, inline = False)
                embed.add_field(name='The achievement you are working towards:', value=x.inventory_print2, inline = False)
                embed.add_field(name='\u200b', value = '------------------------------------------------------------------------------')
                x.inventory_print = ''''''
                x.inventory_print2 = ''''''
                for ach, value in x.hunting_achievements.items():
                    if value[1] == True:
                        x.inventory_print += f'{ach} --- :white_check_mark:\n'
                    else:
                        x.inventory_print2 += f'`{ach}`: Kill {value[0]} monsters. (With `hunt`)\n**Progress:** {x.hunt_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                        break
                if x.inventory_print != '''''':
                    embed.add_field(name='Previous **hunting** achievements:', value=x.inventory_print, inline = False)
                embed.add_field(name='The achievement you are working towards:', value=x.inventory_print2, inline = False)
                embed.add_field(name='\u200b', value = '------------------------------------------------------------------------------')
                x.inventory_print = ''''''
                x.inventory_print2 = ''''''
                for ach, value in x.donation_achievements.items():
                    if value[1] == True:
                        x.inventory_print += f'{ach} --- :white_check_mark:\n'
                    else:
                        x.inventory_print2 += f'`{ach}`: Donate over {value[0]} coins to a player. (With `donate`)\n\n **REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                        break
                if x.inventory_print != '''''':
                    embed.add_field(name='Previous **donation** achievements:', value=x.inventory_print, inline = False)
                embed.add_field(name='The achievement you are working towards:', value=x.inventory_print2, inline = False)
                embed.add_field(name='\u200b', value = '------------------------------------------------------------------------------')
                x.inventory_print = ''''''
                x.inventory_print2 = ''''''
                await ctx.channel.send(embed=embed)
            else:
                if cater == 'material':
                    for ach, value in x.material_achievements.items():
                        if value[1] == True:
                            x.inventory_print += f'{ach} --- :white_check_mark:\n'
                        else:
                            x.inventory_print2 += f'`{ach}`: Obtain materials {value[0]} times. (With `chop`, `fish` and `mine`)\nProgress:** {x.material_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                            break
                elif cater == 'crafting':
                    for ach, value in x.crafting_achievements.items():
                        if value[1] == True:
                            x.inventory_print += f'{ach} --- :white_check_mark:\n'
                        else:
                            x.inventory_print2 += f'`{ach}`: Craft items {value[0]} times. (With `craft`)\nProgress:** {x.hunt_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                            break
                elif cater == 'hunting':
                    for ach, value in x.hunting_achievements.items():
                        if value[1] == True:
                            x.inventory_print += f'{ach} --- :white_check_mark:\n'
                        else:
                            x.inventory_print2 += f'`{ach}`: Hunt and kill {value[0]} monsters. (With `hunt`)\n**Progress:** {x.craft_no}/{value[0]}\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                            break
                elif cater == 'donation':
                    for ach, value in x.donation_achievements.items():
                        if value[1] == True:
                            x.inventory_print += f'{ach} --- :white_check_mark:\n'
                        else:
                            x.inventory_print2 += f'`{ach}`: Donate over {value[0]} coins to a player. (With `donate`)\n\n**REWARD** :gift::\n+ {value[2][0]} coins\n+ {value[2][1]} xp'
                            break
                else:
                    await ctx.channel.send('That isn\'t a valid category! The categories are: `hunting`, `material`, `crafting` and `donation`.')
                    return
                embed = discord.Embed(colour=random.randint(0, 0xffffff))
                embed.set_author(name=f'{x.name}\'s achievements', icon_url=ctx.author.avatar_url)
                if x.inventory_print != '''''':
                    embed.add_field(name='Previous achievements:', value=x.inventory_print, inline = False)
                embed.add_field(name='The achievement you are working towards:', value=x.inventory_print2, inline = False)
                x.inventory_print = ''''''
                x.inventory_print2 = ''''''
                await ctx.channel.send(embed=embed)
        
@client.command(name = 'help', brief = 'Shows this message. A list of all the commands', description = 'This is part of the help command. You can ask for a specific command or help in general.', aliases = [], usage = 'adv help [optional:command_name]')
async def help(ctx, command='all'):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            theembed = discord.Embed(
                title='__Command Help__',
                description='Help on the commands...',
                colour=random.randint(0, 0xffffff)
            )
            theembed.set_thumbnail(url=ctx.author.avatar_url)
            theembed.set_footer(text=f'As requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            x.count = 0
            if command == 'all':
                for y in possible_categories:
                    for com in client.commands:
                        category = category_dict.get(str(com))
                        if category == y:
                            des = com.brief
                            x.command_print += str(f'`{com}`')
                            x.command_print +=' --- '
                            x.command_print += str(des)
                            x.command_print += '\n'
                    theembed.add_field(name=f'{y} Commands:', value=x.command_print, inline=False)
                    x.command_print = ''''''
            else:
                for com in client.commands:
                    if str(com) == command:
                        x.command_print += f'**Description**: {str(com.description)}\n**Usage**: {str(com.usage)}\n**Aliases**: {str(com.aliases)}'
                        theembed.add_field(name = f'`{str(com).upper()}`', value=x.command_print, inline = False)
                        x.command_print = ''''''
            await ctx.channel.send(embed=theembed)
            

                    
            
            
@client.command(name = 'chop', brief = 'Gets you logs and sometimes epic logs', description = 'You can get up to your stage of epic logs from this command. You can get more logs from it by crafting better axes.', aliases = [], usage = 'adv chop')
@commands.cooldown(1, 120, BucketType.user)
async def chop(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if x.name == username:
            if 'chop' in possible_commands[x.stage-1]:
                if x.tutorial == 0:
                    x.add_item('logs', 1)
                    await ctx.channel.send('This command chops down trees, depending on your axe. You have obtained **1 log**. Check your inventory with `adv inv`')
                    x.tutorial = 1
                    return
                x.material_no += 1
                x.randomator = (random.randint(1, x.stage))*x.swords['Axe']['Value']*area_buffs[x.stage-1].get('chop', 1)
                if x.swords['Axe']['Value'] <= 2:
                    x.randomator2 = random.randint(1, x.stage*22)
                    if x.randomator2 <= x.stage*17:
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('logs', x.randomator)
                    elif x.randomator2 <= x.stage*21:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} epic logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('epic logs', x.randomator)
                    elif x.randomator2 <= x.stage*22:
                        x.randomator = 1
                        await ctx.channel.send(f'NANI!? {x.name} has obtained **a :sparkles: Special Log :sparkles:*!!!')
                        x.add_item('special logs', 1)
                elif x.swords['Axe']['Value'] <= 8:
                    x.randomator2 = random.randint(1, x.stage*44)
                    if x.randomator2 <= x.stage*30:
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('logs', x.randomator)
                    elif x.randomator2 <= x.stage*40:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} epic logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('epic logs', x.randomator)
                    elif x.randomator2 <= x.stage*43:
                        x.randomator = random.randint(1, 3)
                        await ctx.channel.send(f'Wow! {x.name} has obtained **{x.randomator} SPECIAL LOGS**!!!')
                        x.add_item('special logs', x.randomator)
                    elif x.randomator2 <= x.stage*44:
                        x.randomator = 1
                        await ctx.channel.send('WILL WONDERS NEVER CEASE? {x.name.upper()} HAS GOTTEN A SHINING LOG!!!')
                        x.add_item('shining logs', 1)
                else:
                    x.randomator2 = random.randint(1, x.stage*1000)
                    if x.randomator2 <= x.stage*770:
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('logs', x.randomator)
                    elif x.randomator2 <= x.stage*970:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has chopped down {x.randomator} epic logs! {tree_emojis[random.randint(0, 3)]}')
                        x.add_item('epic logs', x.randomator)
                    elif x.randomator2 <= x.stage*990:
                        x.randomator = random.randint(1, 4)
                        await ctx.channel.send(f'Wow! {x.name} has obtained **{x.randomator} special logs**!!!')
                        x.add_item('special logs', x.randomator)
                    elif x.randomator2 <= x.stage*999:
                        x.randomator = random.randint(1, 2)
                        await ctx.channel.send('AMAZING! {x.name)} has chopped down {x.randomator} shining logs!!!')
                        x.add_item('shining logs', x.randomator)
                    elif x.randomator2 <= x.stage*1000:
                        x.randomator = 1
                        await ctx.channel.send(f'Lucky duck. You got a legendary log. The chances are 1 in 1000 you know.')
                        x.add_item('legendary logs', 1)
                x.xp += random.randint(x.stage, x.level*5)
                x.try_material()
                if x.inventory_print != '''''':
                    await ctx.channel.send(x.inventory_print)
                    x.inventory_print = ''''''
                x.try_level()
                if x.is_leveling == True:
                    await ctx.channel.send(f'{ctx.author.mention} has leveled up! DEF +1, ATK +1, HP +5')
                    x.is_leveling = False
                if x.is_staging == True:
                    await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                    x.is_staging = False
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(name = 'inv', brief = 'Shows your inventory and its contents.', description = 'This gives you your inventory as a whole.', aliases = ['i', 'inventory'], usage = 'adv inv')
async def inv(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if x.name == username:
            x.inventory_print += f':point_right:**`{x.name}\'s`** inventory: :point_left:'
            x.inventory_print += '\n'
            for y,z in x.items.items():
                x.inventory_print += f'\n:star: {y} : {z}'
            embed = discord.Embed(title=None,
                                  description=None,
                                  colour=discord.Colour.dark_orange())
            embed.set_author(name=f"{x.name}'s inventory", icon_url='{}'.format(ctx.author.avatar_url))
            embed.add_field(name='Items', value=x.inventory_print, inline=False)
            await ctx.channel.send(embed=embed)
            x.inventory_print = ''
            if x.tutorial == 1:
                await ctx.channel.send('See? You have 1 log in your inventory. You can also fish with the command `adv fish`')
                x.tutorial = 2

@client.command(name = 'fish', brief = 'Gets you fish and sometimes glowing fish.', description = 'Similar to the chop command but with glowing fish instead of epic logs. These fish are important to make items in adv recipes. ', aliases = [], usage = 'adv fish')
@commands.cooldown(1, 120, BucketType.user)
async def fish(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if x.name == username:
            if x.tutorial == 2:
                x.add_item('fish', 1)
                await ctx.channel.send('This command, like `adv chop`, gives you fish depending on your fishing rod. You grabbed **1 fish**. Now for scavenging! Type `adv scavenge` to scavenge')
                x.tutorial = 3
                return
            if 'fish' in possible_commands[x.stage-1]:
                x.material_no += 1
                x.randomator = (random.randint(1, x.stage))*x.swords['Rods']['Value']*area_buffs[x.stage-1].get('fish', 1)
                if x.swords['Rods']['Value'] <= 2:
                    x.randomator2 = random.randint(1, x.stage*22)
                    if x.randomator2 <= x.stage*17:
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} fish! :fish:')
                        x.add_item('fish', x.randomator)
                    elif x.randomator2 <= x.stage*21:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} glowing fish! :tropical_fish:')
                        x.add_item('glowing fish', x.randomator)
                    elif x.randomator2 <= x.stage*22:
                        x.randomator = 1
                        await ctx.channel.send(f'NANI!? {x.name} has obtained **AN EXOTIC FISH**!!!')
                        x.add_item('exotic fish', 1)
                elif x.swords['Rods']['Value'] <= 8:
                    x.randomator2 = random.randint(1, x.stage*44)
                    if x.randomator2 <= x.stage*30:
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} fish! :fish:')
                        x.add_item('fish', x.randomator)
                    elif x.randomator2 <= x.stage*40:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} glowing fish! :tropical_fish:')
                        x.add_item('glowing fish', x.randomator)
                    elif x.randomator2 <= x.stage*43:
                        x.randomator = random.randint(1, 3)
                        await ctx.channel.send(f'Wow! {x.name} has obtained **{x.randomator} EXOTIC FISH**!!!')
                        x.add_item('exotic fish', x.randomator)
                    elif x.randomator2 <= x.stage*44:
                        x.randomator = 1
                        await ctx.channel.send('WILL WONDERS NEVER CEASE? {x.name.upper()} HAS FISHED UP A MYTHICAL FISH!!!')
                        x.add_item('mythical fish', 1)
                else:
                    x.randomator2 = random.randint(1, x.stage*1000)
                    if x.randomator2 <= x.stage*770:
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} fish! :fish:')
                        x.add_item('fish', x.randomator)
                    elif x.randomator2 <= x.stage*970:
                        x.randomator = random.randint(1, x.stage)
                        await ctx.channel.send(f'**{ctx.author.mention}** has fished up {x.randomator} glowing fish! :tropical_fish:')
                        x.add_item('glowing fish', x.randomator)
                    elif x.randomator2 <= x.stage*990:
                        x.randomator = random.randint(1, 4)
                        await ctx.channel.send(f'Wow! {x.name} has obtained **{x.randomator} EXOTIC FISH**!!!')
                        x.add_item('exotic fish', x.randomator)
                    elif x.randomator2 <= x.stage*999:
                        x.randomator = random.randint(1, 2)
                        await ctx.channel.send('AMAZING! {x.name)} has fished up {x.randomator} MYTHICAL FISH!!!')
                        x.add_item('mythical fish', x.randomator)
                    elif x.randomator2 <= x.stage*1000:
                        x.randomator = 1
                        await ctx.channel.send(f'Lucky duck. You got a legendary fish. The chances are 1 in 1000 you know.')
                        x.add_item('legendary fish', 1)
                x.xp += random.randint(x.stage, x.level*5)
                x.try_material()
                if x.inventory_print != '''''':
                    await ctx.channel.send(x.inventory_print)
                    x.inventory_print = ''''''
                x.try_level()
                if x.is_leveling == True:
                    await ctx.channel.send(f'{ctx.author.mention} has leveled up! DEF +1, ATK +1, HP +5')
                    x.is_leveling = False
                if x.is_staging == True:
                    await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                    x.is_staging = False
                
                
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(name = 'mine', brief = 'Gives you stone and sometimes iron.', description = 'Gives you stone and sometimes iron. Unlocks in area 2 and you must also have a pickaxe.', aliases = [], usage = 'adv mine')
@commands.cooldown(1, 120, BucketType.user)
async def mine(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if x.name == username:
            if 'mine' in possible_commands[x.stage-1]:
                x.material_no += 1
                x.randomator = (random.randint(1, x.stage*2))*x.swords['Pickaxe']['Value']*area_buffs[x.stage-1].get('mine', 1)
                x.randomator2 = random.randint(1, x.stage*4)
                if x.randomator2 <= x.stage*3:
                    await ctx.channel.send(f'**{ctx.author.mention}** has mined {x.randomator} stone! :pick:')
                    x.add_item('stone', x.randomator)
                else:
                    x.randomator = x.stage
                    await ctx.channel.send(f'**{ctx.author.mention}** has mined {x.randomator} iron! :hammer_and_pick:')
                    x.add_item('iron', x.randomator)
                x.xp += random.randint(x.stage*2, x.level*10)
                x.try_level()
                if x.is_leveling == True:
                    await ctx.channel.send(f'{ctx.author.mention} has leveled up! DEF +1, ATK +1, HP +5')
                    x.is_leveling = False
                if x.is_staging == True:
                    await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                    x.is_staging = False
                x.xp += random.randint(x.stage, x.level*5)
                x.try_material()
                if x.inventory_print != '''''':
                    await ctx.channel.send(x.inventory_print)
                    x.inventory_print = ''''''
                x.try_level()
                if x.is_leveling == True:
                    await ctx.channel.send(f'{ctx.author.mention} has leveled up! DEF +1, ATK +1, HP +5')
                    x.is_leveling = False
                if x.is_staging == True:
                    await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                    x.is_staging = False
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(name = 'clear_message', brief = 'In development', description = 'Will be able to delete messages in the channel.', aliases=[], usage = 'adv clear_message {amount}')
async def clear_message(ctx, amount):
    await ctx.purge(limit=int(amount))
    return



@client.command(name = 'profile', brief = 'Gives you your general stats.', description = 'Your general information including your health, name, coins, xp, level, defense and attack. Your stage is shown in adv map.', aliases = ['p'], usage = 'adv profile')
async def profile(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            embed = discord.Embed(title = '\u2028', description = '\u2028', colour = random.randint(0, 0xffffff))
            x.inventory_print += '**Name: **'
            x.inventory_print += str(x.name)
            x.inventory_print += '\n**Coins: **'
            x.inventory_print += str(x.coins)
            x.inventory_print += '\n**XP: **'
            x.inventory_print += str(x.xp)
            x.inventory_print += '/'
            x.inventory_print += str(x.required_xp)
            x.inventory_print += '\n**HP: **'
            x.inventory_print += str(int(x.hp))
            x.inventory_print += f'/{str(x.total_hp)}'
            x.inventory_print += f'\n**Level: **'
            x.inventory_print += str(x.level)
            x.inventory_print += '\n**DEF: **'
            x.inventory_print += f'{str(x.defense)} :shield:'
            x.inventory_print += '\n**ATK: **'
            x.inventory_print += f'{str(x.attack)} :crossed_swords:'
            embed.set_author(name = f'{x.name}\'s profile', icon_url = ctx.author.avatar_url)
            embed.add_field(name = 'PROFILE:', value = x.inventory_print, inline = True)
            await ctx.channel.send(embed=embed)
            x.inventory_print = ''
            

@client.command(name = 'daily', brief = 'Your daily reward.', description = 'Your daily reward. Can give a variety of items and coins. Resets every 12 hours.', aliases = [], usage = 'adv daily')
@commands.cooldown(1, 43200, BucketType.user)
async def daily(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            item = random.randint(1,5)
            coinS = random.randint(100, 1000)
            if item == 1:
                await ctx.channel.send('You got a common lootbox!')
                x.add_item('common lootbox', 1)
            elif item == 2:
                await ctx.channel.send('You got 2 epic logs!')
                x.add_item('epic logs', 2)
            elif item == 3:
                await ctx.channel.send('You got 1 iron!')
                x.add_item('iron', 1)
            elif item == 4:
                await ctx.channel.send('You got a rare lootbox!!')
                x.add_item('rare lootbox', 1)
            else:
                await ctx.channel.send('You got 5 logs!')
                x.add_item('logs', 5)
            await ctx.channel.send(f'You got {coinS} coins!')
            x.coins += coinS*area_buffs[x.stage-1].get('coins', 1)

@client.command(name = 'lootbox', brief = 'Gives a list of lootboxes.', description = 'The possible lootboxes and (soon) their drops.', aliases = [], usage = 'adv lootbox')
async def lootbox(ctx):
    if 'lootbox' in possible_commands[x.stage-1]:
        await ctx.channel.send(r'''
common lootbox: 100 coins
rare lootbox: 500 coins
epic lootbox: 2500 coins
mega lootbox: 10000 coins
Use !buy {lootbox name} to buy one.
''')
    else:
        await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(name = 'buy', brief = 'Buys things that are in the shop.', description = 'Use your coins to buy items and regeneration tokens.', aliases = [], usage = 'adv buy [amount:int (or all)] [itemname]')
async def buy(ctx, amount,*, itemname):
    itemname = str(itemname)
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if 'buy' in possible_commands[x.stage-1]:
                if amount == 'all':
                    amount = int(coins/lop2[x.stage-1].get(itemname, 1))
                    if amount == coins:
                        amount = 0
                else:
                    amount = int(amount)
                if itemname in lop2[x.stage-1]:
                    cost = lop2[x.stage-1][itemname]*amount
                    if x.coins >= cost:
                        x.add_item(itemname, amount)
                        x.coins -= cost
                        await ctx.channel.send(f'You successfully bought {amount} {itemname}!')
                    else:
                        await ctx.channel.send(f'You do not have enough coins for {amount} {itemname}. That costs {cost} coins...')
                else:
                    await ctx.channel.send('That isn\'t a valid item...')
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(pass_context = True, name = 'ready', brief = 'What commands are not on cooldown.', desciption = 'Gives you a list of the cooldowned commands that are not on cooldown. It doesn\'t give you a time yet though...', aliases = ['rd', 'done'], usage = 'adv ready')
async def ready(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            x.inventory_print = ''''''
            embed = discord.Embed(colour=random.randint(0, 0xffffff))
            for uno in possible_categories:
                for com in client.commands:
                    if com.is_on_cooldown(ctx) == False and str(com) in commands_with_cooldowns and category_dict.get(str(com), None) == uno:
                        x.inventory_print += f':white_check_mark: --- `{str(com).capitalize()}`\n'
                if len(x.inventory_print) > 0:
                    embed.add_field(name=f'**{uno} Commands:**\n', value = x.inventory_print, inline = False)
                x.inventory_print = ''''''
            embed.set_author(name=f'{x.name}\'s ready', icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
            x.inventory_print = ''''''

@client.command(name = 'open', brief = 'Open your lootboxes!', description = 'Use this command to open your lootboxes and get those items you always wanted!', aliases = [], usage = 'adv open [lootbox name]')
async def open(ctx, *, name):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if 'open' in possible_commands[x.stage-1]:
                x.count = 0
                x.count2 = 0
                if name in lootboxes[x.stage-1]:
                    for number in lootboxes[x.stage-1][name][0]:
                        for t in range(x.count+1, lootboxes[x.stage-1][name][0][number][1]+1+x.count):
                            x.items_prevalues.append(t)
                        x.items_values[number] = x.items_prevalues
                        x.items_prevalues = []
                        x.count += lootboxes[x.stage-1][name][0][number][1]
                    if name in x.items:
                        for y in range(lootboxes[x.stage-1][name][1]):
                            x.current_item_amount = random.randint(1, x.count)
                            for itemname, values in x.items_values.items():
                                if x.current_item_amount in values:
                                    x.current_item = itemname
                                    break
                            x.current_item_amount = random.randint(1, lootboxes[x.stage-1][name][0][x.current_item][0])
                            if x.current_item not in x.current_items:
                                x.current_items[x.current_item] = x.current_item_amount
                            else:
                                x.current_items[x.current_item] += x.current_item_amount
                        embed = discord.Embed(title = 'Lootbox',
                                              description = f'Here are your items...',
                                              colour = random.randint(0, 0xffffff))
                        embed.set_author(name=f'{x.name}\'s lootbox', icon_url = ctx.author.avatar_url)
                        for item, value in x.current_items.items():
                            x.inventory_print += f'+ {value} **{item}**\n'
                            x.add_item(item, value)
                        x.remove_item(name, 1)
                        embed.add_field(name=f'`{x.name}` opened a **{name}** and obtained:', value = x.inventory_print, inline = False)
                        await ctx.channel.send(embed=embed)
                        x.inventory_print = ''''''
                        x.current_items = {}
                        x.items_values = {}
                        
                else:
                    await ctx.channel.send('That lootbox does not exist.')
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')

@client.command(name = 'shop', brief = 'What to buy? Hmm...', description = 'Gives you all the things you can buy. (for now that is...)', aliases = [], usage = 'adv shop')
async def shop(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            embed = discord.Embed(title = '__**The Shop**__',
                                  description = 'Buy your items here!',
                                  colour = random.randint(0, 0xffffff))
            print('3')
            for i in lop2[x.stage-1]:
                x.inventory_print += f'`{i}`'
                x.inventory_print += ': '
                x.inventory_print += str(lop2[x.stage-1][i])
                x.inventory_print += ' coins \n'
            print('2')
            embed.add_field(name=f'**Area {x.stage-1} Shop**', value = x.inventory_print, inline = False)
            print('1')
            await ctx.channel.send(embed=embed)
            x.inventory_print = ''''''
            
@client.command(name = 'heal', brief = 'Allows you to heal. If you have a regeneration token that is...', description = 'Use this command to regain that HP of yours after a fight or a hunt. Buy regeneration tokens from the shop first.', aliases = ['regenerate'], usage = 'adv heal')
async def heal(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if 'regeneration tokens' in x.items:
                if x.hp < x.total_hp:
                    if x.hp < x.total_hp - 39:
                        x.hp += 40
                        x.remove_item('regeneration tokens', 1)
                        await ctx.channel.send('You have healed...')
                    else:
                        x.hp = x.total_hp
                        x.remove_item('regeneration tokens', 1)
                        await ctx.channel.send('You have healed...')
                else:
                    await ctx.channel.send('You are already full hp!')
            else:
                await ctx.channel.send('You do not have any regeneration tokens in your inventory! Please buy one...')
    
@client.command(name = 'recipes', brief = 'Shows the recipes for the current area', description = 'All the recipes for your current area.', aliases = [], usage = 'adv recipes')
async def recipes(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if x.stage-1 != 0:
                x.stage = x.stage
            else:
                await ctx.channel.send('You are on the tutorial. There are no recipes here! Get to level **3** to get recipes.')
                return
            embed = discord.Embed(colour=random.randint(0, 0xffffff))
            for number in range(1, x.stage):
                x.inventory_print = ''''''
                for y,z in possible_recipes[number].items():
                    x.inventory_print += f'\n**{y.capitalize()}: **'
                    for a,b in z.items():
                        x.printthing += f'`{b} {a}` + '
                    x.inventory_print += x.printthing
                    x.printthing = ''
                    if x.inventory_print[-1] == ' ' and x.inventory_print[-2] == '+':
                        x.inventory_print = x.inventory_print[:-2]
                embed.add_field(name=f'Area {number+1} Recipes', value=x.inventory_print)
            embed.set_author(name=f'{x.name}\'s recipes', icon_url=ctx.author.avatar_url)
            embed.set_footer(text='New recipes unlock every area!')
            await ctx.channel.send(embed=embed)
            x.inventory_print = ''
            x.printthing = ''



                
@client.command(name = 'pillage', brief = 'Pillaging time!', description = 'This command is not yet unlocked for use. It is used to pillage small settlements in certain places.', aliases = ['pil'], usage = 'adv pillage')
@commands.cooldown(1, 60, BucketType.user)
async def pillage(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if 'pillage' in possible_commands[x.stage-1]:
                x.current_location = possible_locations[random.randint(0,1)]
                x.randomator = random.randint(1,2)
                await ctx.channel.send(f'You are trying to pillage the {x.current_location}!')
                if x.randomator == 1:
                    await ctx.channel.send(f'Sadly the {x.current_location} was too much for you. You lost {x.total_hp/2} HP and 200 coins')
                    x.coins -= 200
                    if x.coins < 0:
                        x.coins = 0
                    x.hp -= 50
                    if x.hp < 0:
                        x.hp = 0
                else:
                    x.randomator = random.randint(1, 100)
                    if x.randomator < 100:
                        await ctx.channel.send(f'Successful pillage! You gained {x.level*100} coins and {x.level*28} xp!')
                        x.coins += x.level*100
                        x.xp += x.level*28
                        x.try_level()
                        if x.is_leveling == True:
                            await ctx.channel.send(f'{x.name} has leveled up! DEF +5, ATK +5, HP +10')
                            x.is_leveling = False
                        if x.is_staging == True:
                            await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                            x.is_staging = False
                    else:
                        if x.current_location == 'library':
                            x.randomator = random.randint(1,10)
                            await ctx.channel.send(f'You have destroyed the library and gained {x.randomator} paper!')
                            x.add_item('paper', x.randomator)
                            x.coins += x.level*100
                            x.xp += x.level*28
                            x.try_level()
                            if x.is_leveling == True:
                                await ctx.channel.send(f'{x.name} has leveled up! DEF +5, ATK +5, HP +10')
                                x.is_leveling = False
                            if x.is_staging == True:
                                await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                                x.is_staging = False
                        else:
                            x.randomator = random.randint(10,100)
                            await ctx.channel.send(f'You have destroyed the fish market and gained {x.randomator} fish!')
                            x.add_item('fish', x.randomator)
                            x.coins += x.level*100
                            x.xp += x.level*28
                            x.try_level()
                            if x.is_leveling == True:
                                await ctx.channel.send(f'{x.name} has leveled up! DEF +5, ATK +5, HP +10')
                                x.is_leveling = False
                            if x.is_staging == True:
                                await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                                x.is_staging = False
            else:
                await ctx.channel.send('This area does not support that command. You cannot use it yet...')
            
@client.command(name = 'scavenge', brief = 'I wonder what you can find?', description = 'You can find many interesting things in the places you are. Rare things pop up now and again too...', aliases = ['scav'], usage = 'adv scavenge')
@commands.cooldown(1, 60, BucketType.user)
async def scavenge(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if x.tutorial == 3:
                x.add_item('logs', 2)
                await ctx.channel.send('Scavenging can give you useful and nice items. Sometimes it gives you nothing though... :no_mouth: In this case, you have obtained **2** more logs. This is all! Type adv help for the full list of commands. Good luck!')
                x.tutorial = 4
                return
            x.current_scavenge = possible_items[random.randint(0, len(possible_items)-1)]
            if x.current_scavenge == 'nothing':
                await ctx.channel.send(f'{ctx.author.mention} Sadly, you found nothing')
            elif x.current_scavenge == 'coins':
                x.randomator = random.randint(100,1000)
                await ctx.channel.send(f'{ctx.author.mention} You got {x.randomator} coins!')
                x.coins += x.randomator
            else:
                x.randomator = random.randint(1, x.stage)
                x.add_item(x.current_scavenge, x.randomator)
                await ctx.channel.send(f'{ctx.author.mention} You have found **{x.randomator} {x.current_scavenge}**!')

@client.command(name = 'equip', brief = 'Equip your armour and weapons.', description = 'Doing this increases your defense and attack if you have a better sword or armour in your inventory. It also returns the current item.', aliases = [], usage = 'adv equip [itemname]')
async def equip(ctx, *, itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if itemname in x.weapon_values:
                x.equip_checklist = x.weapon_values
                if x.items.get(itemname, 0) > 0:
                    x.attack += x.weapon_values[itemname][0]
                    x.attack -= x.swords['Melee']['Value']
                    if x.swords['Melee']['Name'] != 'None':
                        x.add_item(x.swords['Melee']['Name'], 1)
                    x.swords['Melee']['Name'] = itemname
                    x.swords['Melee']['Value'] = x.weapon_values[itemname][0]
                    x.swords['Melee']['Accuracy'] = x.weapon_values[itemname][1]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped your weapon!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            elif itemname in x.axe_values:
                x.equip_checklist = x.axe_values
                if x.items.get(itemname, 0) > 0:
                    x.axe = x.axe_values[itemname]
                    if x.swords['Axe']['Name'] != 'None':
                        x.add_item(x.swords['Axe']['Name'], 1)
                    x.swords['Axe']['Name'] = itemname
                    x.swords['Axe']['Value'] = x.axe_values[itemname]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped your axe!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            elif itemname in x.pickaxe_values:
                x.equip_checklist = x.pickaxe_values
                if x.items.get(itemname, 0) > 0:
                    x.pickaxe = x.pickaxe_values[itemname]
                    if x.swords['Pickaxe']['Name'] != 'None':
                        x.add_item(x.swords['Pickaxe']['Name'], 1)
                    x.swords['Pickaxe']['Name'] = itemname
                    x.swords['Pickaxe']['Value'] = x.pickaxe_values[itemname]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped your pickaxe!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            elif itemname in x.armour_values:
                x.equip_checklist = x.armour_values
                if x.items.get(itemname, 0) > 0:
                    x.defense += x.armour_values[itemname]
                    x.defense -= x.armour['Armour1']['Value']
                    if x.armour['Armour1']['Name'] != 'None':
                        x.add_item(x.armour['Armour1']['Name'], 1)
                    x.armour['Armour1']['Name'] = itemname
                    x.armour['Armour1']['Value'] = x.armour_values[itemname]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped some armour!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            elif itemname in x.rod_values:
                x.equip_checklist = x.rod_values
                if x.items.get(itemname, 0) > 0:
                    x.rod = x.rod_values[itemname][0]
                    if x.swords['Rods']['Name'] != 'None':
                        x.add_item(x.swords['Rods']['Name'], 1)
                    x.swords['Rods']['Name'] = itemname
                    x.swords['Rods']['Value'] = x.rod_values[itemname]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped your rod!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            elif itemname in x.ranged_values:
                x.equip_checklist = x.ranged_values
                if x.items.get(itemname, 0) > 0:
                    x.ranged_attack += x.ranged_values[itemname][0]
                    x.ranged_attack -= x.swords['Ranged']['Value']
                    if x.swords['Ranged']['Name'] != 'None':
                        x.add_item(x.swords['Ranged']['Name'], 1)
                    x.swords['Ranged']['Name'] = itemname
                    x.swords['Ranged']['Value'] = x.ranged_values[itemname][0]
                    x.swords['Ranged']['Accuracy'] = x.ranged_values[itemname][1]
                    x.remove_item(itemname, 1)
                    await ctx.channel.send(f'{ctx.author.mention} You have successfully equipped your ranged weapon!')
                else:
                    await ctx.channel.send('You do not have that item inside your inventory')
            else:
                await ctx.channel.send('That\'s not a item...')
                

@client.command(name = 'sell', brief = 'Sell your items.', description = 'You can sell your items over here.', aliases = [], usage = 'adv sell [amount] [itemname]')
async def sell(ctx,amount, *,itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if amount == 'all':
                amount = x.items.get(itemname, 0)
            else:
                amount = int(amount)
            if x.items.get(itemname, 0) >= amount:
                value = sell_values[x.stage-1].get(itemname, 0)*amount
                x.coins += value
                x.remove_item(itemname, amount)
                await ctx.channel.send(f'You successfully sold **{amount} {itemname}** for **{value} coins!**')
                return
            

@client.command(name = 'craft', brief = 'Craft some stuff.', description = 'Use your materials to craft unique and powerful items to aid you on your journey. These may include weapons, armour, axes, rods or pickaxes.', aliases = [], usage = 'adv craft [amount] [itemname]')
async def craft(ctx, amount, *, itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            x.backup_recipes = copy.deepcopy(possible_recipes)
            x.count = 0
            for sett in range(1, x.stage):
                for item, value in x.backup_recipes[sett].items():
                    x.backup_recipes[x.stage-1][item] = value
            x.current_recipes = x.backup_recipes[x.stage-1]
            if itemname not in x.current_recipes:
                await ctx.channel.send('That isn\'t an item in the recipes list! Type `adv recipes` for the full list of items.')
                return
            for y,z in x.current_recipes.items():
                if y == itemname:
                    x.required_items = z
                    break
            if x.required_items == None:
                return
            if amount == 'all':
                for y,z in x.required_items.items:
                    if int(x.items.get(y, 0)/z) < x.all_calculate:
                        x.all_calculate = int(x.items.get(y, 0)/z)
                amount = x.all_calculate
            else:
                amount = int(amount)
            for y,z in x.required_items.items():
                if x.items.get(y, 0) < z*amount:
                    await ctx.channel.send('You do not have enough materials for that!')
                    return
            await ctx.channel.send(f'You successfully crafted {amount} {itemname}!')
            x.craft_no += 1
            x.add_item(itemname, amount)
            for y,z in x.required_items.items():
                x.remove_item(y, z*amount)
            x.all_calculate = float('inf')
            x.try_craft()
            if x.inventory_print != '''''':
                await ctx.channel.send(x.inventory_print)
                x.inventory_print = ''''''


@client.command(name = 'unequip', brief = 'Unequip your armour and weapons', description = 'You can also take off your armour and weapons.', aliases = [], usage = 'adv unequip [itemname]')
async def unequip(ctx,*, itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if itemname == x.swords['Melee']['Name']:
                if x.swords['Melee']['Name'] != 'None':
                    x.add_item(x.swords['Melee']['Name'], 1)
                    x.attack -= x.swords['Melee']['Value']
                    x.swords['Melee']['Value'] = 0
                    x.swords['Melee']['Accuracy'] = 100
                    x.swords['Melee']['Name'] = 'None'
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped your weapon!")
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            elif itemname == x.swords['Axe']['Name']:
                if x.swords['Axe']['Name'] != 'None':
                    x.add_item(x.swords['Axe']['Name'], 1)
                    x.axe = 0
                    x.swords['Axe']['Name'] = 'None'
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped your weapon!")
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            elif itemname == x.swords['Pickaxe']['Name']:
                if x.swords['Pickaxe']['Name'] != 'None':
                    x.add_item(x.swords['Pickaxe']['Name'], 1)
                    x.swords['Pickaxe']['Name'] = 'None'
                    x.pickaxe = 0
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped your weapon!")
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            elif itemname == x.swords['Rods']['Name']:
                if x.swords['Rods']['Name'] != 'None':
                    x.add_item(x.swords['Rods']['Name'], 1)
                    x.swords['Rods']['Name'] = 'None'
                    x.rod = 0
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped your weapon!")
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            elif itemname == x.armour['Armour1']['Name']:
                if x.armour['Armour1']['Name'] != 'None':
                    x.add_item(x.armour['Armour1']['Name'], 1)
                    x.armour['Armour1']['Name'] = 'None'
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped some armour!")
                    x.defense -= x.swords['Armour1']['Value']
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            elif itemname == x.swords['Ranged']['Name']:
                if x.swords['Ranged']['Name'] != 'None':
                    x.add_item(x.swords['Ranged']['Name'], 1)
                    x.ranged_attack -= x.swords['Ranged']['Value']
                    x.swords['Ranged']['Value'] = x.ranged_attack
                    x.swords['Ranged']['Accuracy'] = 100
                    x.swords['Ranged']['Name'] = 'None'
                    await ctx.channel.send(f"{ctx.author.mention} Successfully unequipped your weapon!")
                    return
                else:
                    await ctx.channel.send('Yeetus la...')
            else:
                await ctx.channel.send(f'{ctx.author.mention} You have not equipped that item yet...')


@client.command(name = 'deconstruct', brief = 'Takes apart your items', description = 'Seperate and break up your items to create new ones. You cannot deconstruct everything.', aliases = ['dismantle'], usage = 'adv dismantle [amount] [itemname]')
async def deconstruct(ctx, amount, *, itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            embed = discord.Embed(colour=random.randint(0, 0xffffff))
            if amount == 'all':
                amount = x.items.get(itemname, 0)
            else:
                amount = int(amount)
            if itemname in dismantle_values:
                if x.items.get(itemname, 0) >= amount:
                    x.inventory_print = ''''''
                    x.inventory_print += f'{amount} {itemname} --> '
                    for item, value in dismantle_values[itemname].items():
                        x.randomator = random.randint(value[0], value[1])*amount
                        x.add_item(item, x.randomator)
                        x.inventory_print += f'{x.randomator} {item} + '
                    x.inventory_print = x.inventory_print[:-2]
                    embed.add_field(name='Your final deconstruction is:', value = x.inventory_print)
                    embed.set_author(name = f'{x.name}\'s deconstruction', icon_url=ctx.author.avatar_url)
                    x.inventory_print = ''''''
                    x.remove_item(itemname, amount)
                    await ctx.channel.send(embed=embed)
                else:
                    await ctx.channel.send(f'You do not have that many {itemname}. That isn\'t possible!')
            else:
                await ctx.channel.send(f'{ctx.author.mention} What are you trying to dismantle? Please check the name of your item.')

@client.command(name = 'more', brief = 'Money... Money... Money...', description = 'Get some money with this command. Don\'t be greedy.', aliases = [], usage = 'adv more [amount]')
@commands.cooldown(1, 3600, BucketType.user)
async def more(ctx, amount:int):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            x.randomator = random.randint(1,3)
            if x.randomator < 3:
                if amount < 2000:
                    await ctx.channel.send(f'Hooray! You got {amount} coins!')
                    x.coins += amount
                else:
                    await ctx.channel.send(f'Naughty {x.name}. Don\'t be greedy. You lost {amount} coins.')
                    x.coins -= amount
                    if x.coins < 0:
                        x.coins = 0
            else:
                await ctx.channel.send('Oof... You didn\'t get any coins. :skull:')

@client.command(name = 'equipment', brief = 'How good is your equipment?', description = 'Shows you your current tools and weapons and armour and their multipliers', aliases = ['eq'], usage = 'adv equipment')
async def equipment(ctx, name='all'):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            embed = discord.Embed(colour = random.randint(0, 0xffffff))
            if name == 'all':
                embed.add_field(name=f"**__Melee__**:", value=f"Name: **{x.swords['Melee']['Name'].capitalize()}**\nDamage: {x.swords['Melee']['Value']+x.weapon_values.get(x.swords['Melee']['Name'], [0, 100, 0])[2]}\nAccuracy: {x.swords['Melee']['Accuracy']}", inline=False)
                embed.add_field(name=f"**__Ranged__**:", value=f"Name: **{x.swords['Ranged']['Name'].capitalize()}**\nDamage added: {x.swords['Ranged']['Value']+x.ranged_values.get(x.swords['Ranged']['Name'], [0, 100, 0])[2]}\nAccuracy: {x.swords['Ranged']['Accuracy']}", inline=False)
                embed.add_field(name=f"**__Armour__**:", value=f"Name: **{x.armour['Armour1']['Name'].capitalize()}**\nProtection: {x.armour['Armour1']['Value']}", inline=False)
                embed.add_field(name=f"**__Axe__**:", value=f"Name: **{x.swords['Axe']['Name'].capitalize()}**\nMultiplier: {x.swords['Axe']['Value']}", inline=False)
                embed.add_field(name=f"**__Pickaxe__**:", value=f"Name: **{x.swords['Pickaxe']['Name'].capitalize()}**\nMultiplier: {x.swords['Pickaxe']['Value']}", inline=False)
                embed.add_field(name=f"**__Fishing rod__**:", value=f"Name: **{x.swords['Rods']['Name'].capitalize()}**\nMultiplier: {x.swords['Rods']['Value']}", inline=False)
                embed.set_author(name=f'{x.name}\'s equipment', icon_url = ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)
            else:
                if name == 'melee':
                    embed.set_author(name=f'{x.name}\'s melee weapon', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.swords['Melee']['Name'].capitalize()}:**", value=f"Damage added: {x.swords['Melee']['Value']}\nAccuracy: {x.weapon_values.get(x.swords['Melee']['Name'], [0, 100, 0])[1]}\nTraining Damage Boost: {x.weapon_values.get(x.swords['Melee']['Name'], [0, 100, 0])[2]}")
                elif name == 'ranged':
                    embed.set_author(name=f'{x.name}\'s ranged weapon', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.swords['Ranged']['Name'].capitalize()}:**", value=f"Damage added: {x.swords['Melee']['Value']}\nAccuracy: {x.ranged_values.get(x.swords['Ranged']['Name'], [0, 100, 0])[1]}\nTraining Damage Boost: {x.ranged_values.get(x.swords['Ranged']['Name'], [0, 100, 0])[2]}")
                elif name == 'armour':
                    embed.set_author(name=f'{x.name}\'s armour', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.armour['Armour1']['Name'].capitalize()}**", value=f"Protection: {x.armour['Armour1']['Value']}")
                elif name == 'axe':
                    embed.set_author(name=f'{x.name}\'s axe', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.swords['Axe']['Name'].capitalize()}**", value=f"Multiplier: {x.swords['Axe']['Value']}")
                elif name == 'pickaxe':
                    embed.set_author(name=f'{x.name}\'s pickaxe', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.swords['Pickaxe']['Name'].capitalize()}**", value=f"Multiplier: {x.swords['Pickaxe']['Value']}")
                elif name == 'rod':
                    embed.set_author(name=f'{x.name}\'s rod', icon_url = ctx.author.avatar_url)
                    embed.add_field(name=f"**{x.swords['Rods']['Name'].capitalize()}**", value=f"Multiplier: {x.swords['Rods']['Value']}")
                else:
                    embed.add_field(name=f"Sorry. That isn't a valid category. :(", value='The categories are: `melee`, `ranged`, `armour`, `axe`, `pickaxe` and `rod`')
                await ctx.channel.send(embed=embed)

@client.command(name = 'map', brief = 'Shows your progress through the stages', description = 'This shows your progress through the areas of the island.', aliases = ['progress'], usage = 'adv map')
async def map(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            await ctx.channel.send('https://i.imgur.com/C1kPQvc.png')
            await ctx.channel.send(f'**{x.name}**, you are on Area {x.stage}: {areas[x.stage-1]}')

@client.command(name = 'trade', brief = 'Trade with NPCs throughout the game!', description = 'Gives you a screen where you reply with the trade you want and the amount. Use \'quit\' to quit. The traders have limits though...', aliases = ['barter'], usage = 'adv trade')
@commands.cooldown(1, 60, BucketType.user)
async def trade(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if x.stage == 1:
                await ctx.channel.send('You are only on Area 1. Nobody wants to trade with you. :sob:')
                return
            if x.finished_trade == True:
                x.finished_trade = False
                x.trading_stage = 0
                return
            x.count = 0
            x.items_prevalues = []
            x.items_values = {}
            for value in trades[x.stage-1]:
                for p in range(x.count+1, trades[x.stage-1][value][1]+x.count+1):
                    x.items_prevalues.append(p)
                x.count += trades[x.stage-1][value][1]
                x.items_values[value] = x.items_prevalues
                x.items_prevalues = []
            x.randomator = random.randint(1, x.count)
            for v, j in x.items_values.items():
                if x.randomator in j:
                    x.current_trades = trades[x.stage-1][v]
                    if v == 'nothing':
                        await ctx.channel.send('You found nobody to trade with. Sadness...')
                        return
                    embed = discord.Embed(title='Trading',
                                        description=f'You have met a {v}! He wants to trade',
                                        colour = random.randint(0, 0xffffff)
                                        )
                    x.current_trade = v
                    break
            x.trade_amount = random.randint(x.current_trades[2], x.current_trades[2]*4)
            while x.finished_trade != True:
                if x.finished_trade == True:
                    x.finished_trade = False
                    x.trading_stage = 0
                    return
                embed = discord.Embed(title='Trading',
                                            description=f'You have met a {x.current_trade}! He wants to trade',
                                            colour = random.randint(0, 0xffffff)
                                            )
                embed.set_author(name=f'{x.name}\'s trade', icon_url=ctx.author.avatar_url)
                x.inventory_print = ''''''
                x.count = 0
                for trade in x.current_trades[0]:
                    x.inventory_print += f'`{alphabet[x.count]}` `{trade[0][1]}× {trade[0][0]}` --> `{trade[1][1]}× {trade[1][0]}`\n'
                    x.count += 1
                embed.set_footer(text=f'This trader has a total of {x.trade_amount} items...')
                embed.add_field(name='His trades are:', value=x.inventory_print, inline = False)
                embed.add_field(name='\u200b', value='Type the corresponding letter then the amount to trade. e.g. If you want to trade `A` twice, you type \'a 2\'.', inline=False)
                x.trading_stage = 1
                await ctx.channel.send(embed=embed)
                x.inventory_print = ''''''
                def check(message):
                    return x.trading_stage == 0
                try:
                    message = await client.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    x.trading_stage = 0
                    await ctx.channel.send('The trader got bored and walked away')
                    return
            x.finished_trade = False
            
@client.command(name = 'hunt', brief = 'Fighting monsters are good for your health...', description = 'You can fight a monster and kill it. (or not sometimes...)', aliases = [], usage = 'adv hunt')
@commands.cooldown(1, 60, BucketType.user)
async def hunt(ctx):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if x.monster_stage == 1:
                await ctx.channel.send('You are already fighting a monster!')
                return
            if x.running == True:
                x.monster_stage = 0
                return
            x.monster = random.choice(list(possible_monsters[x.stage-1]))
            if possible_monsters[x.stage-1][x.monster] != []:
                if random.randint(possible_monsters[x.stage-1][x.monster][1], possible_monsters[x.stage-1][x.monster][2]) == possible_monsters[x.stage-1][x.monster][2]:
                    x.monster_dropping = True
                    x.monster_drop = possible_monsters[x.stage-1][x.monster][0]
            x.current_monster_hp = round(random.randint(10, 15) * x.level/5 * x.stage, 0)
            x.damage = round((random.randint(5, 12) * x.level/10 * x.stage)/(x.defense/5), 0)
            await ctx.channel.send(f'You have encountered a {x.monster}! What do you want to do: `melee` or `ranged` or `run`?')
            while x.monster_alive == True:
                x.monster_stage = 1
                user = ctx.author
                def check(message):
                    return ctx.author == user and message.content == 'melee' or message.content == 'run' or message.content == 'ranged'
                try:
                    message = await client.wait_for('message', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    await ctx.channel.send('You took too long. The monster escaped...')
                    return
                else:
                    if x.running == True:
                        x.running = False
                        x.monster_stage = 0
                        return
                    if x.monster_alive == False:
                        x.monster_alive = True
                        await ctx.channel.send(f'{ctx.author.mention} You have killed the monster!')
                        x.hunt_no += 1
                        if x.monster_dropping == True:
                            x.monster_dropping = False
                            x.add_item(x.monster_drop, 1)
                            await ctx.channel.send(f'You got a **{x.monster_drop}**!')
                        coins = x.level*random.randint(10, 40)
                        xp = x.level*random.randint(10, 20)
                        x.coins += coins*area_buffs[x.stage-1].get('coins', 1)
                        x.xp += xp
                        x.try_hunt()
                        if x.inventory_print != '''''':
                            await ctx.channel.send(x.inventory_print)
                            x.inventory_print = ''''''
                        x.try_level()
                        if x.is_leveling == True:
                            await ctx.channel.send(f'{ctx.author.mention} has leveled up! DEF +1, ATK +1, HP +5')
                            x.is_leveling = False
                        if x.is_staging == True:
                            await ctx.channel.send(f'You have progressed to the next stage, **{areas[x.stage-1]}**. Great job!')
                            x.is_staging = False
                        
                        x.monster_stage = 0
                        return
                    if x.is_alive == False:
                        x.is_alive = True
                        x.monster_stage = 0
                        await ctx.channel.send(f'{ctx.author.mention} You died, losing a level.')
                        x.level -= 1
                        if x.level < 1:
                            x.level = 1
                        if (x.level)%10 == 0 or x.level == 3:
                            if x.level != 10:
                                x.stage -= 1
                        return
                    x.monster_stage = 1
                    await ctx.channel.send('The monster and you are both not dead! What do you want to do. `melee` or `ranged` or `run`?')

@client.command(name = 'donate', aliases = ['give'], brief = 'Give your friends items!', description = 'Donate coins or items to your friends with this command.', usage = 'adv donate @[name of player] [amount of items] [itemname]')
@commands.cooldown(1, 900, BucketType.user)
async def donate(ctx, member:discord.Member, amount, *, itemname):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            membery, dim = str(member).split('#')
            for y in profile_list:
                if membery == y.name:
                    if amount == 'all':
                        if itemname == 'coins':
                            amount = x.coins
                        else:
                            amount = x.items.get(itemname, 0)
                    else:
                        try:
                            amount = int(amount)
                        except TypeError:
                            await ctx.channel.send(f'{ctx.author.mention} That isn\'t a valid amount!')
                            return
                    if itemname == 'coins':
                        if x.coins >= amount:
                            x.coins -= amount
                            y.coins += amount
                            embed = discord.Embed(colour=random.randint(0, 0xffffff))
                            embed.set_author(name=f'{x.name}\'s donation', icon_url=ctx.author.avatar_url)
                            embed.add_field(name='**Donation Successful!**', value=f'{x.name} donated {amount} {itemname} to {y.name}.')
                            await ctx.channel.send(embed=embed)
                            for ach, value in x.donation_achievements.items():
                                if value[1] == False:
                                    x.current_achievement = [value, ach]
                                    break
                            if amount >= x.current_achievement[0][0]:
                                x.coins += x.current_achievement[0][2][0]
                                x.xp += x.current_achievement[0][2][1]
                                await ctx.channel.send(f'**{x.name}** has earned the achievement `{x.current_achievement[1]}` and gained {x.current_achievement[0][2][0]} COINS and {x.current_achievement[0][2][1]} XP!')
                                x.donation_achievements[x.current_achievement[1]][1] = True
                            return
                    else:
                        if x.items.get(itemname, 0) >= amount:
                            x.remove_item(itemname, amount)
                            y.add_item(itemname, amount)
                            embed = discord.Embed(colour=random.randint(0, 0xffffff))
                            embed.set_author(name=f'{x.name}\'s donation', icon_url=ctx.author.avatar_url)
                            embed.add_field(name='**Donation Successful!**', value=f'**{x.name}** donated {amount} {itemname} to **{y.name}**.')
                            await ctx.channel.send(embed=embed)
                            return
                        else:
                            await ctx.channel.send(f'{ctx.author.mention} You do not have enough of that item to donate!')

@client.command(name = 'travel', aliases = ['area', 'goto'], usage = 'adv travel [area]', brief = 'Travel to previous areas!', description = 'If you want to go back to previous areas, use trhis command to go back. Remember that all the commands will change according to your current area.')
async def travel(ctx, area : int):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            if area > x.max_stage:
                await ctx.channel.send(f'Your max area is only area {x.max_stage}!')
                return
            else:
                x.stage = area
                await ctx.channel.send(f'**{x.name}** has moved to area {area}...')
                return

@client.command()
async def fight(ctx, member : discord.Member):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            membery, dim = str(member).split('#')
            for y in profile_list:
                if membery == y.name:
                    if y.stage != x.stage:
                        await ctx.channel.send('You need to be on the same stage to fight!')
                        return
                    x.randomator = random.randint(0, len(fight1[x.stage-1])-1)
                    x.fight_map = x.randomator
                    y.fight_map = x.randomator
                    x.fight_stage = 1
                    y.fight_stage = 2
                    x.opponent = y
                    y.opponent = x
                    await ctx.channel.send(f'{x.name} is :one:\n{y.name} is :two:')
                    x.fight_stat = ':one:'
                    y.fight_stat = ':two:'
                    x.position = [1, 1]
                    y.position = [7, 6] #across, down
                    x.fight_hp = x.total_hp #just hp
                    y.fight_hp = y.total_hp
                    x.fight_hp2 = x.total_hp #total hp
                    y.fight_hp2 = y.total_hp
                    x.fight_turn = ctx.author
                    y.fight_turn = ctx.author
                    x.op_mem = member
                    y.op_mem = ctx.author
                    x.id = 1
                    y.id = 2
                    x.fight_def = x.defense
                    y.fight_def = y.defense
                    x.fight_atk = x.attack
                    y.fight_atk = y.attack
                    x.fight_map_pic = ''''''
                    x.fight_map_pic += f'{fight1[x.stage-1][x.fight_map]}\n'
                    x.fight_map_pic += f'{fight2[x.stage-1][x.fight_map]}\n'
                    x.fight_map_pic += f'{fight3[x.stage-1][x.fight_map]}\n'
                    x.fight_map_pic += f'{fight4[x.stage-1][x.fight_map]}\n'
                    x.fight_map_pic += f'{fight5[x.stage-1][x.fight_map]}\n'
                    x.fight_map_pic += f'{fight6[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight1[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight2[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight3[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight4[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight5[x.stage-1][x.fight_map]}\n'
                    y.fight_map_pic += f'{fight6[x.stage-1][x.fight_map]}\n'
                    while x.fight_fin != True:
                        if x.fight_stage == 1 or y.fight_stage == 1:
                            embed = discord.Embed(colour=random.randint(0, 0xffffff))
                            embed.add_field(name='MAP:', value=x.fight_map_pic, inline=False)
                            embed.add_field(name='LEGEND', value=':orange_circle: --> Wall\n:white_circle: --> Path\n:green_circle: --> Chance\n:sparkling_heart: --> Healing')
                            embed.add_field(name='What do you want to do?', value='`special`, `up`, `down`, `left` or `right`?')
                            embed.add_field(name=f'**{x.name}\'s stats**:', value=f'\nDEF: {x.fight_def}\nATK: {x.attack}\nHP: {x.fight_hp}/{x.fight_hp2}', inline=False)
                            embed.add_field(name=f'**{y.name}\'s stats**:', value=f'\nDEF: {y.fight_def}\nATK: {y.attack}\nHP: {y.fight_hp}/{y.fight_hp2}', inline=True)
                            embed.set_footer(text='Note that attack and defense gained in a fight will not be saved onto your real attack and defense.')
                            if x.fight_stage == 1:
                                await ctx.channel.send(content=f'It\'s {x.name}\'s turn!', embed=embed)
                            elif y.fight_stage == 1:
                                await ctx.channel.send(content=f'It\'s {y.name}\'s turn!', embed=embed)
                            x.inventory_print = ''''''
                            def check(msg):
                                return x.fight_stage == 3 or y.fight_stage == 3 or x.ended == True or y.ended == True
                            try:
                                await client.wait_for('message', check=check, timeout=120)
                            except asyncio.TimeoutError:
                                await ctx.channel.send('You\'re too slow! It\'s the opponent\'s turn!')
                                x.fight_turn = x.op_mem
                        elif x.fight_stage == 3 or y.fight_stage == 3:
                            def check(msg):
                                return x.fight_stage == 1 or y.fight_stage == 1
                            try:
                                await client.wait_for('message', check=check, timeout=120)
                            except asyncio.TimeoutError:
                                await ctx.channel.send('You\'re too slow! It\'s the opponent\'s turn!')
                                x.fight_turn = x.op_mem
                            
                            
                
@client.command(aliases=['tr', 'train'], usage='adv training [category]', name='training', brief = 'Train your skills with trainers to improve your damage and accuracy. (and xp)', description='There are 3 different categories to train and each one will cost more the more you train. Training on a weapon will make you better with that weapon but not other weapons.')
async def training(ctx, ty='xp'):
    username, d = str(ctx.author).split('#')
    for x in profile_list:
        if username == x.name:
            x.add_item('iron sword', 1)
            if ty == 'xp':
                embed = discord.Embed(colour=random.randint(0, 0xffffff))
                embed.set_author(name=f'{x.name}\'s training', icon_url=ctx.author.avatar_url)
                embed.add_field(name=f'The XP Trainer wants {x.xp_tr_cost} coins to train your xp.', value='Do you accept? (Type `yes` or `no`)')
                x.training_stage = 1
                x.training_type = 'xp'
                await ctx.channel.send(embed=embed)
                def check(msg):
                    return x.training_stage == 0
                try:
                    await client.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    x.training_stage = 0
                    await ctx.channel.send('Training cancelled.')
                    return
            elif ty == 'melee':
                embed = discord.Embed(colour=random.randint(0, 0xffffff))
                embed.set_author(name=f'{x.name}\'s training', icon_url=ctx.author.avatar_url)
                embed.add_field(name=f'The Melee Trainer wants {x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3]} coins to train your melee skill.', value='Do you accept? (Type `yes` or `no`)')
                x.training_stage = 1
                x.training_type = 'melee'
                await ctx.channel.send(embed=embed)
                def check(msg):
                    return x.training_stage == 0
                try:
                    await client.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    x.training_stage = 0
                    await ctx.channel.send('Training cancelled.')
                    return
            elif ty == 'ranged':
                embed = discord.Embed(colour=random.randint(0, 0xffffff))
                embed.set_author(name=f'{x.name}\'s training', icon_url=ctx.author.avatar_url)
                embed.add_field(name=f'The Ranger wants {x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3]} coins to train your ranged skill.', value='Do you accept? (Type `yes` or `no`)')
                x.training_stage = 1
                x.training_type = 'ranged'
                await ctx.channel.send(embed=embed)
                def check(msg):
                    return x.training_stage == 0
                try:
                    await client.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    x.training_stage = 0
                    await ctx.channel.send('Training cancelled.')
                    return
            else:
                await ctx.channel.send('That isn\'t a category! The three categories are: `melee`, `ranged` and `xp`')
        
@client.event
async def on_message(message):
    username, d = str(message.author).split('#')
    for x in profile_list:
        if username == x.name:
            if message.content.lower() == 'melee':
                if x.monster_stage == 1:
                    x.randomator = random.randint(1, 100)
                    if x.randomator <= x.weapon_values.get(x.swords['Melee']['Name'], [1, 100, 0])[1]:
                        x.inventory_print = 'You hit the monster!'
                        x.attack2 = round(random.randint(x.attack+x.weapon_values.get(x.swords['Melee']['Name'], [1, 100, 0])[2], (x.attack+x.weapon_values.get(x.swords['Melee']['Name'], [1, 100, 0])[2])*2)/(x.defense/5), 0)
                        x.current_monster_hp -= x.attack2
                    else:
                        x.inventory_print = 'You missed. HAHA'
                    x.total_damage += x.damage
                    x.hp -= x.damage
                    if x.hp < 1:
                        x.is_alive = False
                        x.hp = 0
                    if x.current_monster_hp < 1:
                        x.monster_alive = False
                        x.current_monster_hp = 0
                    embed = discord.Embed(title = 'Hunt',
                                          description = 'Your progress on your hunt...',
                                          colour = random.randint(0, 0xffffff))
                    embed.set_author(name=f'{x.name}\'s hunt', icon_url = message.author.avatar_url)
                    x.inventory_print2 += (f'**Monster name**: {x.monster}' + '\n')
                    x.inventory_print2 += (f'**Monster hp**: {int(x.current_monster_hp)}' + '\n')
                    x.inventory_print2 += (f'**Monster damage**: {int(x.damage)} DMG')
                    embed.add_field(name = 'Monster stats:', value = x.inventory_print2, inline = True)
                    x.inventory_print2 = ''''''
                    x.inventory_print2 += (f'**Player name**: {x.name}' + '\n')
                    x.inventory_print2 += (f'**Player hp**: {int(x.hp)}/{int(x.total_hp)}' + '\n')
                    x.inventory_print2 += (f'**Player damage**: {x.attack}')
                    embed.add_field(name = 'Your stats:', value = x.inventory_print2, inline = True)
                    x.inventory_print2 = ''''''
                    await message.channel.send(content=x.inventory_print, embed=embed)
                    x.inventory_print2 = ''
                    x.inventory_print = ''''''
                    x.monster_stage = 0
                    return
            if message.content.lower() == 'ranged':
                if x.monster_stage == 1:
                    x.randomator = random.randint(1, 100)
                    if x.randomator <= x.ranged_values.get(x.swords['Ranged']['Name'], [1, 100, 0])[1]:
                        x.inventory_print = 'You hit the monster!'
                        x.attack2 = round(random.randint(x.attack+x.ranged_values.get(x.swords['Ranged']['Name'], [1, 100, 0])[2], (x.attack+x.ranged_values.get(x.swords['Ranged']['Name'], [1, 100, 0])[2])*2)/(x.defense/5), 0)
                        x.current_monster_hp -= x.attack2
                    else:
                        x.inventory_print = 'You missed. HAHA'
                    x.total_damage += x.damage
                    x.hp -= x.damage
                    if x.hp < 1:
                        x.is_alive = False
                        x.hp = 0
                    if x.current_monster_hp < 1:
                        x.monster_alive = False
                        x.current_monster_hp = 0
                    embed = discord.Embed(title = 'Hunt',
                                          description = 'Your progress on your hunt...',
                                          colour = random.randint(0, 0xffffff))
                    embed.set_author(name=f'{x.name}\'s hunt', icon_url = message.author.avatar_url)
                    x.inventory_print2 += (f'**Monster name**: {x.monster}' + '\n')
                    x.inventory_print2 += (f'**Monster hp**: {int(x.current_monster_hp)}' + '\n')
                    x.inventory_print2 += (f'**Monster damage**: {int(x.damage)} DMG')
                    embed.add_field(name = 'Monster stats:', value = x.inventory_print2, inline = True)
                    x.inventory_print2 = ''''''
                    x.inventory_print2 += (f'**Player name**: {x.name}' + '\n')
                    x.inventory_print2 += (f'**Player hp**: {int(x.hp)}/{int(x.total_hp)}' + '\n')
                    x.inventory_print2 += (f'**Player damage**: {x.ranged_attack}')
                    embed.add_field(name = 'Your stats:', value = x.inventory_print2, inline = True)
                    x.inventory_print2 = ''''''
                    await message.channel.send(content=x.inventory_print, embed=embed)
                    x.inventory_print2 = ''
                    x.inventory_print = ''''''
                    x.monster_stage = 0
                    return
            elif message.content.lower() == 'run':
                if x.monster_stage == 1:
                    x.running = True
                    await message.channel.send('You ran away from the fight.')
                    x.monster_stage = 0
                    return
            elif x.trading_stage == 1:
                if message.content == 'quit':
                    x.finished_trade = True
                    x.trading_stage = 0
                    await message.channel.send('You have quit...')
                    x.finished_trade = True
                    return
                if message.content.upper().split()[0] not in alphabet:
                    x.trading_stage = 0
                    await message.channel.send('That isn\'t a valid trade!')
                    return
                x.letter_check = alphabet.find(message.content.upper().split()[0]) + 1
                if len(x.current_trades[0]) >= x.letter_check:
                    if message.content.split()[1] == 'all':
                        x.the_trade_amount = x.items.get(x.current_trades[0][x.letter_check-1][0][0], 0)
                    else:
                        x.the_trade_amount = int(message.content.split()[1])
                    if x.the_trade_amount > x.trade_amount:
                        x.trading_stage = 0
                        await message.channel.send(f'The trader doesn\'t have that many items. He only can trade a total of {x.trade_amount} things.')
                        return
                    x.the_trade = x.current_trades[0][x.letter_check-1]
                    if x.items.get(x.the_trade[0][0], 0) >= x.the_trade_amount*x.the_trade[0][1]:
                        x.finished_trade = True
                        x.remove_item(x.the_trade[0][0], x.the_trade[0][1]*x.the_trade_amount)
                        x.add_item(x.the_trade[1][0], x.the_trade[1][1]*x.the_trade_amount)
                        embed = discord.Embed(title = 'Trading', description = 'What you are receiving.')
                        embed.set_author(name=f'{x.name}\'s deal', icon_url=message.author.avatar_url)
                        embed.add_field(name='**DEAL**', value=f'{x.the_trade[0][1]*x.the_trade_amount} × {x.the_trade[0][0]} --> {x.the_trade[1][1]*x.the_trade_amount} × {x.the_trade[1][0]}', inline=False)
                        await message.channel.send(embed=embed)
                        x.finished_trade = True
                        x.trading_stage = 0
                        return
                    else:
                        x.trading_stage = 0
                        await message.channel.send('You do not have enough materials for that!')
                        return
                else:
                    x.trading_stage = 0
                    await message.channel.send('That isn\'t within the trade range!')
                    return
            elif x.training_stage == 1:
                if x.training_type == 'xp':
                    if message.content.lower() == 'yes':
                        if x.coins < x.xp_tr_cost:
                            await message.channel.send('XP Trainer: GRRR. You\'re trying to scam me eh? Go check your profile before you come for training.')
                            x.training_stage = 0
                            return
                        x.coins -= x.xp_tr_cost
                        xp = random.randint(int(x.xp_tr_cost/4), int(x.xp_tr_cost/2))
                        embed=discord.Embed(colour=random.randint(0, 0xffffff))
                        x.xp_tr_cost = x.xp_tr_cost*2 - x.level*x.stage*20
                        x.xp += xp
                        x.try_level()
                        embed.add_field(name='Successful training!', value = f'You have gained {xp} XP! (Next training: `{x.xp_tr_cost}` coins)')
                        await message.channel.send(embed=embed)
                        x.training_stage = 0
                        return
                    elif message.content.lower() == 'no':
                        await message.channel.send('Training cancelled.')
                        x.training_stage = 0
                        return
                    else:
                        await message.channel.send('That isn\'t `yes` or `no`!')
                        x.training_stage = 0
                        return
                elif x.training_type == 'melee':
                    if message.content.lower() == 'yes':
                        if x.coins < x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3]:
                            await message.channel.send('Melee Trainer: GRRR. You don\'t have that many coins. Go check your profile before you come for training.')
                            x.training_stage = 0
                            return
                        if x.swords['Melee']['Name'] == 'None':
                            await message.channel.send('You don\'t have a weapon to train for yet!')
                            x.training_stage = 0
                            return
                        x.coins -= x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3]
                        incr1 = random.randint(2, 5)
                        incr2 = random.randint(0, x.stage)
                        embed=discord.Embed(colour=random.randint(0, 0xffffff))
                        x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3] = x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3]*3 - (x.level*x.stage)**2
                        x.swords['Melee']['Value'] += incr2
                        x.weapon_values.get(x.swords['Melee']['Name'], [1, 100, 0])[2] += incr2
                        x.weapon_values.get(x.swords['Melee']['Name'], [1, 100, 0])[1] += incr1
                        x.try_level()
                        embed.add_field(name='Successful training!', value = f'You have gained {incr2} sword attack and {incr1} accuracy! (Next training: `{x.weapon_values.get(x.swords["Melee"]["Name"], [0, 100, 0, 0])[3]}` coins)')
                        embed.set_footer(text='Quick tip: Don\'t try to train your melee too much on the wooden sword. It resets for each new sword.')
                        await message.channel.send(embed=embed)
                        x.training_stage = 0
                        return
                    elif message.content.lower() == 'no':
                        await message.channel.send('Training cancelled.')
                        x.training_stage = 0
                        return
                    else:
                        await message.channel.send('That isn\'t `yes` or `no`!')
                        x.training_stage = 0
                        return
                elif x.training_type == 'ranged':
                    if message.content.lower() == 'yes':
                        if x.coins < x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3]:
                            await message.channel.send('Ranger: DUDE. You don\'t have that many coins. Go check your profile before I shoot you down.')
                            x.training_stage = 0
                            return
                        if x.swords['Ranged']['Name'] == 'None':
                            await message.channel.send('You don\'t have a weapon to train for yet!')
                            x.training_stage = 0
                            return
                        x.coins -= x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3]
                        incr1 = random.randint(2, 5)
                        incr2 = random.randint(0, x.stage)
                        embed=discord.Embed(colour=random.randint(0, 0xffffff))
                        x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3] = x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3]*3 - x.level*x.stage*20
                        x.swords['Ranged']['Value'] += incr2
                        x.weapon_values.get(x.swords['Ranged']['Name'], [1, 100, 0])[2] += incr2
                        x.weapon_values.get(x.swords['Ranged']['Name'], [1, 100, 0])[1] += incr1
                        x.try_level()
                        embed.add_field(name='Successful training!', value = f'You have gained {incr2} ranged attack and {incr1} accuracy! (Next training: `{x.ranged_values.get(x.swords["Ranged"]["Name"], [0, 100, 0, 0])[3]}` coins)')
                        embed.set_footer(text='Quick tip: Train a lot on your better ranged weapons. They don\'t have much accuracy...')
                        await message.channel.send(embed=embed)
                        x.training_stage = 0
                        return
                    elif message.content.lower() == 'no':
                        await message.channel.send('Training cancelled.')
                        x.training_stage = 0
                        return
                    else:
                        await message.channel.send('That isn\'t `yes` or `no`!')
                        x.training_stage = 0
                        return
            elif x.fight_stage == 1:
                if message.content == 'special':
                    x.can_attack = True
                    if x.can_attack == True:
                        x.inventory_print = ''''''
                        x.inventory_print += '`coin rain` - Does your money divided by 10 000 amount of damage\n'
                        x.inventory_print += '`slash` - Does your attack amount of damage\n'
                        x.inventory_print += '`shoot` - Does your ranged attack divided by 2 amount of damage over the maximum distance of 3\n'
                        x.inventory_print += '`catapult` - You can shoot over over the distance of two and over walls, dealing your attack divided by 5 amount of damage\n'
                        x.inventory_print += '`heal` - You heal your level amount of health (around that number)\n'
                        x.inventory_print += '`shield` - Increases your defense for this fight by your level.\n'
                        x.inventory_print += '`surrender` - Do I have to explain this one?'
                        embed = discord.Embed(title='POSSIBLE ATTACKS: (Reply with one to use)', description=x.inventory_print, inline=False)
                        await message.channel.send(embed=embed)
                        x.fight_stage = 3
                        x.can_attack = False
                elif message.content == 'up':
                    x.opponent.fight_stage = 1
                    if x.position[1] == 1:
                        x.ended = True
                        await message.channel.send('You can\'t walk off the map!')
                        x.ended = False
                        return
                    if fightcal(x.position[0], x.position[1]-1, x.fight_map_pic) == '🟠':
                        x.ended = True
                        await message.channel.send('That\'s a wall you\'re walking into.')
                        x.ended = False
                        return
                    if fightcal(x.position[0], x.position[1]-1, x.fight_map_pic) == '🟢':
                        x.is_chancing = True
                    if fightcal(x.position[0], x.position[1]-1, x.fight_map_pic) == '💖':
                        x.is_healing = True
                    x.fight_map_pic_edits = x.fight_map_pic.split()
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1]-1)*9)))
                    x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-1)*9)), '⚪')
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1]-2)*9)))
                    if x.id == 1:
                        x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-2)*9)), '1️⃣')
                    else:
                        x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-2)*9)), '2️⃣')
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.position = [x.position[0], x.position[1]-1]
                    x.fight_map_pic = ''
                    x.count = 0
                    x.fight_map_pic = ''
                    for item in x.fight_map_pic_edits:
                        if x.count%9 == 0 and x.count != 0:
                            x.fight_map_pic += '\n'
                        x.fight_map_pic += item
                        x.fight_map_pic += ' '
                        x.count += 1
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.fight_stage = 2
                    if x.is_healing == False and x.is_chancing == False:
                        x.ended = True
                    await message.channel.send(f'{x.name} has walked upwards!')
                    if x.is_healing == True:
                        x.is_healing = False
                        x.randomator = random.randint(x.level, x.level*4)
                        x.fight_hp += x.randomator
                        if x.fight_hp > x.fight_hp2:
                            x.fight_hp = x.fight_hp2
                        x.ended = True
                        await message.channel.send(f'{x.name} has walked on a healing area and healed {x.randomator} HP.')
                    if x.is_chancing == True:
                        x.is_chancing = False
                        x.randomator = random.randint(1, 4)
                        if x.randomator == 1:
                            x.randomator = random.randint(x.level, x.level*5)
                            x.fight_hp -= x.randomator
                            if x.fight_hp < 1:
                                x.fight_hp = 0
                                x.fight_fin = True
                            x.ended = True
                            await message.channel.send(f'{x.name}! The chance shot spiky rocks at you and you took {x.randomator} damage!')
                        elif x.randomator == 2:
                            x.ended = True
                            await message.channel.send('The chance disappeared, leaving behind nothing.')
                        elif x.randomator == 3:
                            x.fight_def += 20
                            x.ended = True
                            await message.channel.send(f'{x.name}, the gods have granted you some protection. You have gained 20 defense...')
                        elif x.randomator == 4:
                            x.xp += x.level*100
                            x.coins += x.level*100
                            x.try_level()
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.level*100} EXP and {x.level*100} coins. I don\'t know why this has anything to do with the fight but...')
                        elif x.randomator == 5:
                            x.randomator = random.randint(x.stage, x.level)
                            x.fight_atk += x.randomator
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.randomator} attack as a result of pure luck. :P')
                            
                    x.ended = False
                    x.opponent.fight_stage = 1
                    return
                    return
                elif message.content == 'down':
                    x.opponent.fight_stage = 1
                    if x.position[1] == 6:
                        x.ended = True
                        await message.channel.send('You can\'t walk off the map!')
                        x.ended = False
                        return
                    if fightcal(x.position[0], x.position[1]+1, x.fight_map_pic) == '🟠':
                        x.ended = True
                        await message.channel.send('That\'s a wall you\'re walking into.')
                        x.ended = False
                        return
                    if fightcal(x.position[0], x.position[1]+1, x.fight_map_pic) == '🟢':
                        x.is_chancing = True
                    if fightcal(x.position[0], x.position[1]+1, x.fight_map_pic) == '💖':
                        x.is_healing = True
                    x.fight_map_pic_edits = x.fight_map_pic.split()
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1]-1)*9)))
                    x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-1)*9)), '⚪')
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1])*9)))
                    if x.id == 1:
                        x.fight_map_pic_edits.insert((x.position[0]+((x.position[1])*9)), '1️⃣')
                    else:
                        x.fight_map_pic_edits.insert((x.position[0]+((x.position[1])*9)), '2️⃣')
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.position = [x.position[0], x.position[1]+1]
                    x.fight_map_pic = ''
                    x.count = 0
                    x.fight_map_pic = ''
                    for item in x.fight_map_pic_edits:
                        if x.count%9 == 0 and x.count != 0:
                            x.fight_map_pic += '\n'
                        x.fight_map_pic += item
                        x.fight_map_pic += ' '
                        x.count += 1
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.fight_stage = 2
                    if x.is_healing == False and x.is_chancing == False:
                        x.ended = True
                    await message.channel.send(f'{x.name} has walked downwards!')
                    if x.is_healing == True:
                        x.is_healing = False
                        x.randomator = random.randint(x.level, x.level*4)
                        x.fight_hp += x.randomator
                        if x.fight_hp > x.fight_hp2:
                            x.fight_hp = x.fight_hp2
                        x.ended = True
                        await message.channel.send(f'{x.name} has walked on a healing area and healed {x.randomator} HP.')
                    if x.is_chancing == True:
                        x.is_chancing = False
                        x.randomator = random.randint(1, 4)
                        if x.randomator == 1:
                            x.randomator = random.randint(x.level, x.level*5)
                            x.fight_hp -= x.randomator
                            if x.fight_hp < 1:
                                x.fight_hp = 0
                                x.fight_fin = True
                            x.ended = True
                            await message.channel.send(f'{x.name}! The chance shot spiky rocks at you and you took {x.randomator} damage!')
                        elif x.randomator == 2:
                            x.ended = True
                            await message.channel.send('The chance disappeared, leaving behind nothing.')
                        elif x.randomator == 3:
                            x.fight_def += 20
                            x.ended = True
                            await message.channel.send(f'{x.name}, the gods have granted you some protection. You have gained 20 defense...')
                        elif x.randomator == 4:
                            x.xp += x.level*100
                            x.coins += x.level*100
                            x.try_level()
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.level*100} EXP and {x.level*100} coins. I don\'t know why this has anything to do with the fight but...')
                        elif x.randomator == 5:
                            x.randomator = random.randint(x.stage, x.level)
                            x.fight_atk += x.randomator
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.randomator} attack as a result of pure luck. :P')
                    x.ended = False
                    x.opponent.fight_stage = 1
                    return
                    return
                elif message.content == 'left':
                    x.opponent.fight_stage = 1
                    if x.position[0] == 1:
                        x.ended = True
                        await message.channel.send('You can\'t walk off the map!')
                        x.ended = False
                        return
                    if fightcal(x.position[0]-1, x.position[1], x.fight_map_pic) == '🟠':
                        x.ended = True
                        await message.channel.send('That\'s a wall you\'re walking into.')
                        x.ended = False
                        return
                    if fightcal(x.position[0]-1, x.position[1], x.fight_map_pic) == '🟢':
                        x.is_chancing = True
                    if fightcal(x.position[0]-1, x.position[1], x.fight_map_pic) == '💖':
                        x.is_healing = True
                    x.fight_map_pic_edits = x.fight_map_pic.split()
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1]-1)*9)))
                    x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-1)*9)), '⚪')
                    x.fight_map_pic_edits.pop((x.position[0]-1+((x.position[1]-1)*9)))
                    if x.id == 1:
                        x.fight_map_pic_edits.insert((x.position[0]-1+((x.position[1]-1)*9)), '1️⃣')
                    else:
                        x.fight_map_pic_edits.insert((x.position[0]-1+((x.position[1]-1)*9)), '2️⃣')
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.position = [x.position[0]-1, x.position[1]]
                    x.fight_map_pic = ''
                    x.count = 0
                    x.fight_map_pic = ''
                    for item in x.fight_map_pic_edits:
                        if x.count%9 == 0 and x.count != 0:
                            x.fight_map_pic += '\n'
                        x.fight_map_pic += item
                        x.fight_map_pic += ' '
                        x.count += 1
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.fight_stage = 2
                    if x.is_healing == False and x.is_chancing == False:
                        x.ended = True
                    await message.channel.send(f'{x.name} has walked to the left!')
                    if x.is_healing == True:
                        x.is_healing = False
                        x.randomator = random.randint(x.level, x.level*4)
                        x.fight_hp += x.randomator
                        if x.fight_hp > x.fight_hp2:
                            x.fight_hp = x.fight_hp2
                        x.ended = True
                        await message.channel.send(f'{x.name} has walked on a healing area and healed {x.randomator} HP.')
                    if x.is_chancing == True:
                        x.is_chancing = False
                        x.randomator = random.randint(1, 4)
                        if x.randomator == 1:
                            x.randomator = random.randint(x.level, x.level*5)
                            x.fight_hp -= x.randomator
                            if x.fight_hp < 1:
                                x.fight_hp = 0
                                x.fight_fin = True
                            x.ended = True
                            await message.channel.send(f'{x.name}! The chance shot spiky rocks at you and you took {x.randomator} damage!')
                        elif x.randomator == 2:
                            x.ended = True
                            await message.channel.send('The chance disappeared, leaving behind nothing.')
                        elif x.randomator == 3:
                            x.fight_def += 20
                            x.ended = True
                            await message.channel.send(f'{x.name}, the gods have granted you some protection. You have gained 20 defense...')
                        elif x.randomator == 4:
                            x.xp += x.level*100
                            x.coins += x.level*100
                            x.try_level()
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.level*100} EXP and {x.level*100} coins. I don\'t know why this has anything to do with the fight but...')
                        elif x.randomator == 5:
                            x.randomator = random.randint(x.stage, x.level)
                            x.fight_atk += x.randomator
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.randomator} attack as a result of pure luck. :P')
                    x.ended = False
                    x.opponent.fight_stage = 1
                    return
                elif message.content == 'right':
                    x.opponent.fight_stage = 1
                    if x.position[0] == 7:
                        x.ended = True
                        await message.channel.send('You can\'t walk off the map!')
                        x.ended = False
                        return
                    if fightcal(x.position[0]+1, x.position[1], x.fight_map_pic) == '🟠':
                        x.ended = True
                        await message.channel.send('That\'s a wall you\'re walking into.')
                        x.ended = False
                        return
                    if fightcal(x.position[0]+1, x.position[1], x.fight_map_pic) == '🟢':
                        x.is_chancing = True
                    if fightcal(x.position[0]+1, x.position[1], x.fight_map_pic) == '💖':
                        x.is_healing = True
                    x.fight_map_pic_edits = x.fight_map_pic.split()
                    x.fight_map_pic_edits.pop((x.position[0]+((x.position[1]-1)*9)))
                    x.fight_map_pic_edits.insert((x.position[0]+((x.position[1]-1)*9)), '⚪')
                    x.fight_map_pic_edits.pop((x.position[0]+1+((x.position[1]-1)*9)))
                    if x.id == 1:
                        x.fight_map_pic_edits.insert((x.position[0]+1+((x.position[1]-1)*9)), '1️⃣')
                    else:
                        x.fight_map_pic_edits.insert((x.position[0]+1+((x.position[1]-1)*9)), '2️⃣')
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.position = [x.position[0]+1, x.position[1]]
                    x.fight_map_pic = ''
                    x.count = 0
                    x.fight_map_pic = ''
                    for item in x.fight_map_pic_edits:
                        if x.count%9 == 0 and x.count != 0:
                            x.fight_map_pic += '\n'
                        x.fight_map_pic += item
                        x.fight_map_pic += ' '
                        x.count += 1
                    x.opponent.fight_map_pic = x.fight_map_pic
                    x.fight_stage = 2
                    if x.is_healing == False and x.is_chancing == False:
                        x.ended = True
                    await message.channel.send(f'{x.name} has walked to the right!')
                    if x.is_healing == True:
                        x.is_healing = False
                        x.randomator = random.randint(x.level, x.level*4)
                        x.fight_hp += x.randomator
                        if x.fight_hp > x.fight_hp2:
                            x.fight_hp = x.fight_hp2
                        x.ended = True
                        await message.channel.send(f'{x.name} has walked on a healing area and healed {x.randomator} HP.')
                    if x.is_chancing == True:
                        x.is_chancing = False
                        x.randomator = random.randint(1, 5)
                        if x.randomator == 1:
                            x.randomator = random.randint(x.level, x.level*5)
                            x.fight_hp -= x.randomator
                            if x.fight_hp < 1:
                                x.fight_hp = 0
                                x.fight_fin = True
                            x.ended = True
                            await message.channel.send(f'{x.name}! The chance shot spiky rocks at you and you took {x.randomator} damage!')
                        elif x.randomator == 2:
                            x.ended = True
                            await message.channel.send('The chance disappeared, leaving behind nothing.')
                        elif x.randomator == 3:
                            x.fight_def += 20
                            x.ended = True
                            await message.channel.send(f'{x.name}, the gods have granted you some protection. You have gained 20 defense...')
                        elif x.randomator == 4:
                            x.xp += x.level*100
                            x.coins += x.level*100
                            x.try_level()
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.level*100} EXP and {x.level*100} coins. I don\'t know why this has anything to do with the fight but...')
                        elif x.randomator == 5:
                            x.randomator = random.randint(x.stage, x.level)
                            x.fight_atk += x.randomator
                            x.ended = True
                            await message.channel.send(f'{x.name} has gained {x.randomator} attack as a result of pure luck. :P')
                    x.ended = False
                    x.opponent.fight_stage = 1
                    return
            elif x.fight_stage == 3:
                if message.content == 'coin rain':
                    if x.position[0] == x.opponent.position[0] and x.position[1] == x.opponent.position[1] + 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] and x.position[1] == x.opponent.position[1] - 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] + 1 and x.position[1] == x.opponent.position[1]:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] - 1 and x.position[1] == x.opponent.position[1]:
                        x.can_attack = True
                    else:
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You cannot reach {x.opponent.name}!')
                        return
                    x.opponent.fight_stage = 1
                    x.opponent.fight_hp -= round(x.coins/10000, 0)
                    if x.opponent.fight_hp < 1:
                        x.opponent.fight_dead = True
                    await message.channel.send(f'**{x.name}** hit **{x.opponent.name}** of {int(round(x.coins/10000, 0))} damage. {x.opponent.name} has {x.opponent.fight_hp} health left!')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
                elif message.content == 'slash':
                    if x.position[0] == x.opponent.position[0] and x.position[1] == x.opponent.position[1] + 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] and x.position[1] == x.opponent.position[1] - 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] + 1 and x.position[1] == x.opponent.position[1]:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] - 1 and x.position[1] == x.opponent.position[1]:
                        x.can_attack = True
                    else:
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You cannot reach {x.opponent.name}!')
                        return
                    x.opponent.fight_stage = 1
                    x.opponent.fight_hp -= round(x.fight_atk/(x.fight_def/5),0)
                    if x.opponent.fight_hp < 1:
                        x.opponent.fight_dead = True
                        return
                    await message.channel.send(f'**{x.name}** hit **{x.opponent.name}** of {x.fight_atk} damage. {x.opponent.name} has {x.opponent.fight_hp} health left!')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
                elif message.content == 'shoot':
                    if x.position[0] - x.opponent.position[0] == x.opponent.position[1] - x.position[1]:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] + 1 and x.position[1] == x.opponent.position[1] + 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] + 1 and x.position[1] == x.opponent.position[1] + 1:
                        x.can_attack = True
                    elif x.position[0] == x.opponent.position[0] + 1 and x.position[1] == x.opponent.position[1] + 1:
                        x.can_attack = True
                    else:
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You cannot reach {x.opponent.name}!')
                        return
                    x.opponent.fight_stage = 1
                    x.opponent.fight_hp -= round(x.ranged_attack/2, 0)
                    if x.opponent.fight_hp < 1:
                        x.opponent.fight_dead = True
                        return
                    await message.channel.send(f'**{x.name}** hit **{x.opponent.name}** of {int(round(x.ranged_attack/2, 0))} damage. {x.opponent.name} has {x.opponent.fight_hp} health left!')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
                elif message.content == 'catapult':
                    if abs(x.position[0] - x.opponent.position[0]) < 3  and x.position[1] == x.opponent.position[1]:
                        x.can_attack = True
                    elif abs(x.position[1] - x.opponent.position[1]) < 3 and x.position[0] == x.opponent.position[0]:
                        x.can_attack = True
                    else:
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You cannot reach {x.opponent.name}!')
                        return
                    x.opponent.fight_stage = 1
                    x.opponent.fight_hp -= round(x.fight_atk/2/(x.fight_def/5),0)
                    await message.channel.send(f'**{x.name}** yeeted a cannonball onto **{x.opponent.name}** and dealed {int(round(fight_atk/2, 0))} damage. {x.opponent.name} has {x.opponent.fight_hp} health left!')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
                elif message.content == 'heal':
                    if x.heal_count%3 != 0:
                        x.heal_count += 1
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You have already healed in the previous 2 turns!')
                        return
                    else:
                        x.heal_count += 1
                    x.opponent.fight_stage = 1
                    x.randomator = random.randint(x.level-1, x.level+2)
                    x.fight_hp += x.randomator
                    if x.fight_hp > x.fight_hp2:
                        x.fight_hp = x.fight_hp2
                    await message.channel.send(f'**{x.name}** healed {x.randomator} health. \n**REMAINING HEALTH:** {int(x.fight_hp)}/{int(x.fight_hp2)}')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
                elif message.content == 'shield':
                    if x.shield_count%3 != 0:
                        x.shield_count += 1
                        x.fight_stage = 1
                        await message.channel.send(f'{x.name}! You have already shielded in the previous 2 turns!')
                        return
                    else:
                        x.shield_count += 1
                    x.opponent.fight_stage = 1
                    x.fight_def += x.level
                    await message.channel.send(f'{x.name} has gained {x.level} defense.')
                    x.fight_stage = 2
                    x.opponent.fight_stage = 1
                    x.fight_turn = x.op_mem
                    return
            if x.monster_stage == 1 and message.content.lower() != 'fight' and message.content.lower() != 'run':
                await message.channel.send('Remember you are still fighting the monster!')
                x.monster_stage = 0
                return
    await client.process_commands(message)
                    


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        in_hours = calculate(round(error.retry_after, 0))
        await ctx.channel.send(f'Your command is on cooldown. Please wait `{in_hours}`')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send('You are missing one or more required arguments!')



client.run('NzQ1NTEzODc3OTUyOTIxNjAw.Xzy35w.E3EAABaBMSxm_dOi3kX9GlJv3fU')
