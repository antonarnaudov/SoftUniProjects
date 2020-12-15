# from guild_system.project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        check = [p for p in self.players if p.name == player_name]
        if check:
            self.players.remove(check[0])
            return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for p in self.players:
            result += p.player_info()
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild('UGT')
# print(guild.assign_player(player))
# print(guild.kick_player("George"))
# print(guild.guild_info())
