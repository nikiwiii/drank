from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class Menu(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MenuItem(TwoLineIconListItem):
    text_polish: str = StringProperty()
    text_english: str = StringProperty()
    icon_name: str = StringProperty()
    next_screen_name: str = StringProperty()


class DrinkScreen(MDScreen):
    pass


class LedScreen(MDScreen):
    pass


class RootScreen(MDScreen):
    pass
