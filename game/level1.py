from core.level import Level
from core.platform import Platform


class Level1(Level):
    def __init__(self, player):
        super().__init__(player)

        self.player.rect.x = 10
        self.player.rect.y = 365

        level = [(1000, 350, 0, 400)]
        for platform in level:
            created_platform = Platform(platform[0], platform[1])
            created_platform.rect.x = platform[2]
            created_platform.rect.y = platform[3]
            self.platform_list.add(created_platform)