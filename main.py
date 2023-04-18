from kivymd.app import MDApp
from custom_widgets import TranslatedBtn


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.selecttheme("LightGreen")
        self.theme_cls.theme_style = "Light"
        self.lights()

    scr1 = ''
    def lights(self):
        self.scr1 = self.root.ids.screen_manager.get_screen("scr 1")
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            self.scr1.ids.tabs.background_color = self.theme_cls.primary_color
            self.scr1.ids.tabs.icon_color = self.theme_cls.bg_normal
            self.root.ids.toolbar.md_bg_color = self.theme_cls.primary_color
            self.scr1.ids.tabs.text_color_normal = "gainsboro"
            self.root.ids.screen_manager.get_screen("scr 7").ids['togglelight'].text = 'Dark'
        else:
            self.theme_cls.theme_style = "Dark"
            self.darken()
            self.root.ids.screen_manager.get_screen("scr 7").ids['togglelight'].text = 'Light'

    def darken(self):
        self.scr1.ids.tabs.background_color = self.theme_cls.bg_normal
        self.scr1.ids.tabs.text_color_normal = self.theme_cls.primary_color
        self.scr1.ids.tabs.icon_color = self.theme_cls.primary_color
        self.root.ids.toolbar.md_bg_color = self.theme_cls.bg_normal

    def selecttheme(self, theme):
        self.theme_cls.primary_palette = theme
        if self.theme_cls.theme_style == "Dark":
            self.darken()

    colors = ['Pink', 'Purple', 'Indigo',
              'Blue', 'LightBlue', 'Teal', 'Green',
              'LightGreen', 'Lime', 'Orange', 'Brown']

    def thememenuon(self):
        screen = self.root.ids.screen_manager.get_screen("scr 7")
        for i in range(11):
            if self.colors[i] == 'Pink':
                screen.ids[f'theme{i}'].md_bg_color = '#eb005e'
                screen.ids[f'theme{i}'].line_color = '#eb005e'
            elif self.colors[i] == 'LightBlue':
                screen.ids[f'theme{i}'].md_bg_color = '#22a4d4'
                screen.ids[f'theme{i}'].line_color = '#22a4d4'
            elif self.colors[i] == 'Blue':
                screen.ids[f'theme{i}'].md_bg_color = 'dodgerblue'
                screen.ids[f'theme{i}'].line_color = 'dodgerblue'
            elif self.colors[i] == 'Lime':
                screen.ids[f'theme{i}'].md_bg_color = '#cde05c'
                screen.ids[f'theme{i}'].line_color = '#cde05c'
            elif self.colors[i] == 'Indigo':
                screen.ids[f'theme{i}'].md_bg_color = 'darkslateblue'
                screen.ids[f'theme{i}'].line_color = 'darkslateblue'
            elif self.colors[i] == 'Brown':
                screen.ids[f'theme{i}'].md_bg_color = '#704f3b'
                screen.ids[f'theme{i}'].line_color = '#704f3b'
            elif self.colors[i] == 'LightGreen':
                screen.ids[f'theme{i}'].md_bg_color = 'yellowgreen'
                screen.ids[f'theme{i}'].line_color = 'yellowgreen'
            elif self.colors[i] == 'Green':
                screen.ids[f'theme{i}'].md_bg_color = '#51a64b'
                screen.ids[f'theme{i}'].line_color = '#51a64b'
            else:
                screen.ids[f'theme{i}'].md_bg_color = self.colors[i].lower()
                screen.ids[f'theme{i}'].line_color = self.colors[i].lower()
            screen.ids[f'theme{i}'].children[0].text = self.colors[i]
    def refreshcleanwindow(self):
        self.root.ids.screen_manager.get_screen("scr 8").getlist(self.root.ids.screen_manager.get_screen("scr 8"))

MainApp().run()
