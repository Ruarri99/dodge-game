class MenuManager:
    def __init__(self, display):
        self.display = display
        self.menus = {
            "main": self.loadMainMenu,
            "credits": self.loadCreditsMenu,
            "local_game": self.loadLocalGameMenu,
            "local_gameplay": self.loadLocalGameplay,
            "end_game": self.loadEndGameMenu
        }
        self.current_menu = self.menus["main"]()


    def changeMenu(self, menu_name, data=None):
        if menu_name in self.menus:
            self.current_menu = self.menus[menu_name](data or {})
        else:
            raise ValueError(f"Unknown menu: {menu_name}")


    def loadMainMenu(self, data=None):
        from menus.main_menu import MainMenu
        return MainMenu(self.display, self)


    def loadCreditsMenu(self, data=None):
        from menus.credits_menu import CreditsMenu
        return CreditsMenu(self.display, self)


    def loadLocalGameMenu(self, data=None):
        from menus.local_game_menu import LocalGameMenu
        return LocalGameMenu(self.display, self)


    def loadLocalGameplay(self, data=None):
        from menus.local_gameplay import LocalGameplay
        return LocalGameplay(self.display, self, **data)


    def loadEndGameMenu(self, data=None):
        from menus.end_game_menu import EndGameMenu
        return EndGameMenu(self.display, self, **data)


    def handleEvents(self, events):
        result = self.current_menu.handleEvents(events)
        if isinstance(result, tuple):
            menu_name, data = result
            self.changeMenu(menu_name, data)
        elif isinstance(result, str):
            self.changeMenu(result)


    def update(self):
        self.current_menu.update()


    def draw(self):
        self.current_menu.draw()