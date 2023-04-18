from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRectangleFlatIconButton, MDFillRoundFlatButton, MDRoundFlatIconButton, MDFloatingActionButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.card import MDCard
from time import sleep
from kivy.core.window import Window
import math
Window.size = (768, 800)

drinklist = ['wódka','whiskey','rum','tequila','gin',
             'cola','tonic','sok grejfrutowy','sok pomarańczowy','cordial']
dr = drinklist

class Menu(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    
    def changelogo(self):
        if self.ids['logo'].source == "data/logo.png":
            self.ids['logo'].source = "data/logoOG.png"
        else:
            self.ids['logo'].source = "data/logo.png"

class ImageButton(ButtonBehavior, Image):pass

class MenuItem(TwoLineIconListItem):
    text_polish: str = StringProperty()
    text_english: str = StringProperty()
    icon_name: str = StringProperty()
    next_screen_name: str = StringProperty()

class Tab(MDFloatLayout, MDTabsBase):
    icon_name: str = StringProperty()

class DrinkBox(MDCard):
    ingredients = [
    f'- {dr[0]} 40ml\n- {dr[8]} 80ml',
    f'- {dr[0]} 40ml\n- {dr[7]} 80ml',
    f'- {dr[0]} 40ml\n- {dr[5]} 80ml',
    f'- {dr[0]} 40ml\n- {dr[6]} 80ml',
    f'- {dr[0]} 40ml\n- {dr[9]} 40ml',
    f'- {dr[1]} 40ml\n- {dr[5]} 80ml',
    f'- {dr[1]} 40ml\n- {dr[6]} 80ml',
    f'- {dr[1]} 40ml\n- {dr[9]} 40ml',
    f'- {dr[2]} 40ml\n- {dr[5]} 80ml\n- {dr[9]} 20ml',
    f'- {dr[2]} 40ml\n- {dr[7]} 80ml',
    f'- {dr[3]} 40ml\n- {dr[6]} 80ml',
    f'- {dr[3]} 40ml\n- {dr[7]} 80ml\n- {dr[9]} 20ml',
    f'- {dr[3]} 40ml\n- {dr[9]} 40ml',
    f'- {dr[4]} 40ml\n- {dr[6]} 80ml',
    f'- {dr[4]} 40ml\n- {dr[7]} 80ml',
    f'- {dr[4]} 40ml\n- {dr[8]} 80ml',
    f'- {dr[4]} 40ml\n- {dr[9]} 40ml',
    f'- wódka święcona 200ml']

    img: str = StringProperty()
    index: int = NumericProperty()
    text_polish: str = StringProperty()
    text_english: str = StringProperty()

class ChooseBtn(MDRectangleFlatIconButton):
    text_polish: str = StringProperty()
    icon_name: str = StringProperty()

class ThemeBtn(MDCard, ButtonBehavior):pass

class BankBtn(MDFlatButton):
    text_: str = StringProperty()

class MlBtn(MDFlatButton):pass

class DrinkNameBtn(MDRectangleFlatIconButton):
    text_: str = StringProperty()
    icon_name: str = StringProperty()

class SSlider(MDSlider):pass

class BorderBottom(MDBoxLayout):pass

class DropTha(MDDropDownItem):
    text_: str = StringProperty()

class Padding(MDBoxLayout):pass

class Container_1_1(MDBoxLayout):pass

class TranslatedBtn(MDFillRoundFlatButton):
    text_polish: str = StringProperty()
    text_english: str = StringProperty()

class VerticalBox(MDBoxLayout):pass

class WhiteBox(MDCard):pass

class RoundBox(MDCard):pass

class ToggleBtn(MDToggleButton, MDRoundFlatIconButton):pass

class LightsBtn(MDFloatingActionButton):pass

class DrinkScreen(MDScreen):
    def clearall(self):
        for i in range(10):
            self.ids[f'slider{i}'].value = 0
            self.updatevalue(i)
        self.get_sum()

    def updatevalue(self,id):
        self.ids[f'sldval{id}'].text = str(math.floor(self.ids[f'slider{id}'].value)) + ' ml'   # zaokraglona wartość slider'a jako str
        self.get_sum()

    def choosereadydrink(self, drink):
        drink_banks_and_amount = {
            "Screwdriver": [0, 40, 8, 80],
            "Greyhound": [0, 40, 7, 80],
            "Whiskey z colą": [1, 40, 5, 80],
            "Whiskey Sour": [1, 40, 9, 40],
            "Czerwony Rum": [2, 40, 7, 80],
            "TNT": [3, 40, 6, 80],
            "G&T": [4, 40, 6, 80],
            "The Salty Dog": [4, 40, 7, 80],
            "Wódka z colą": [0, 40, 5, 80],
            "Wódka z tonic'iem": [0, 40, 6, 80],
            "Vodka sour": [0, 40, 9, 40],
            "Whiskey z tonic'iem": [1, 40, 6, 80],
            "Tequila z Cordialem": [3, 40, 6, 40],
            "Gin pomarańczowy": [4, 40, 8, 80],
            "Gimlet": [4, 40, 9, 90]
        }
        def updatetwosliders(self, array):
            index1, amount1, index2, amount2 = array[0], array[1], array[2], array[3]
            print(drinklist[index1], amount1, drinklist[index2], amount2)
            self.clearall()
            self.ids[f'slider{index1}'].value, self.ids[f'slider{index2}'].value = amount1, amount2
            self.updatevalue(index1)
            self.updatevalue(index2)

        self.clearall()
        match drink:
            case "Cuba Libre":
                self.ids['slider2'].value = 40
                self.updatevalue(2)
                self.ids['slider5'].value = 80
                self.updatevalue(9)
                self.ids['slider9'].value = 20
                self.updatevalue(9)
            case "Paloma":
                self.ids['slider3'].value = 40
                self.updatevalue(3)
                self.ids['slider7'].value = 80
                self.updatevalue(7)
                self.ids['slider9'].value = 20
                self.updatevalue(9)
            case "Drink Ojca Pijo":
                self.ids['slider0'].value = 200
                self.updatevalue(0)
            case _:
                updatetwosliders(self,drink_banks_and_amount[drink])
        self.makedrink()

    def makedrink(self):
        potion = []
        mlsum = 0
        for i in range(10):
            if self.ids[f'slider{i}'].value != 0:
                mlsum += int(self.ids[f'sldval{i}'].text[0:len(self.ids[f'sldval{i}'].text)-3]) # wartość slider'a bez fragmentu 'ml'
                potion.append(
                    {"bank": drinklist.index(self.ids[f'label{i}'].text.lower()), 
                    "ilosc": int(self.ids[f'sldval{i}'].text[0:len(self.ids[f'sldval{i}'].text)-3])
                    })
        if mlsum > 250:
            self.dialog = MDDialog(
                title="Zwolnij",
                text=f"Wyleje ci się to wszystko ({mlsum}/250 ml)",
                buttons=[
                    MDRectangleFlatButton(
                        text="sory", on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        else:
            print(potion)
            self.dialog = MDDialog(
                title=f"Do nalania {mlsum} ml",
                text='Nalewam drina',
                on_open=self.wart,
                buttons=[
                    MDRectangleFlatButton(
                        text="ok", on_release=self.close_dialog, opacity=0
                    ),
                ],
            )
            self.dialog.open()

    def wart(self,_):
        sleep(2)
        self.dialog.text = 'Gotowe'
        self.dialog.buttons[0].opacity = 1

    def close_dialog(self, _):
        self.dialog.dismiss()
        self.clearall()

    def get_sum(self):
        sum = 0
        for i in range(10):
            if self.ids[f'slider{i}'].value != 0:
                sum += int(self.ids[f'sldval{i}'].text[0:len(self.ids[f'sldval{i}'].text)-3])
        self.ids['amount'].text = str(sum) + ' ml'
        self.ids['amount'].color = 0,0,0,0
        if sum > 250:
            self.ids['amount'].color = "indianred"

class LedScreen(MDScreen):
    on = True
    chosen = False
    def on_color(self, value):
        if self.on:
            it = 0
            val = list(value)
            for i in val:
                if it != 3:
                    val[it] = math.floor(val[it] * 255)
                it += 1
            val[3] = 1
            print("RGBA = ", str(val))
            self.ids.colordisplay.md_bg_color = list(value)
            self.ids.colordisplay.opacity = 1
            self.chosen = True

    def colortoggle(self):
        if self.on:
            self.ids.colorlabel.opacity, self.ids.colordisplay.opacity = 0, 0
            self.ids['picker'].pos_hint, self.ids['cover'].pos_hint = {"center_x": 10}, {"center_x": 0.495}
            self.on = False
        else:
            self.ids.colorlabel.opacity = 1
            if self.chosen: self.ids.colordisplay.opacity = 1
            self.ids['picker'].pos_hint, self.ids['cover'].pos_hint = {"center_x": 0.5}, {"center_x": 10}
            self.on = True

class ChoiceScreen(ButtonBehavior, MDScreen):
    chosen, chosenbank, prev = 0, 0, 10
    opened = False
    def editsumshi(self, ind, content):
        if self.ids['banks'].pos_hint != {"center_y": 10} and self.prev == ind:
            self.ids['banks'].pos_hint = {"center_y": 10}
            self.prev = 10
        else:
            if not self.opened: self.refresh()
            self.prev = ind
            if ind == 7: ind = 6.3
            elif ind == 8: ind = 6.4
            elif ind == 9: ind = 6.5
            self.ids['banks'].pos_hint = {"center_x": 1.2, "center_y":1.18-ind*0.105}
            self.chosen = content

    def refresh(self):
        for i in range(10):
            self.ids[f'drop{i}'].text = str(drinklist.index(self.ids[f'drinkname{i}'].text.lower()))
        self.opened = True

    def closemenu(self):
        self.ids['banks'].pos_hint = {"center_y": 10}

    def choosenum(self,indtxt):
        self.closemenu()
        self.chosenbank = int(indtxt)
        print(drinklist)
        drinklist[self.chosen], drinklist[self.chosenbank] = drinklist[self.chosenbank], drinklist[self.chosen]
        print(drinklist)
        self.refresh()

class ThemeScreen(MDScreen):pass

class AboutScreen(MDScreen):pass

class CleanScreen(MDScreen):
    bankcontentlist = drinklist
    def getlist(_,self):
        for i in range(10):
            self.ids[f'clean{i}'].text = drinklist[i].capitalize()
            if drinklist[i] in ['wódka','whiskey','rum','tequila','gin']:
                self.ids[f'clean{i}'].icon = 'water'
            else:
                self.ids[f'clean{i}'].icon = 'water-off'

    def cleanbank(self, index):
        print(f'pouring from bank {index}')
    def stopcleaning(self, index):
        print(f'stopped pouring')

class RootScreen(MDScreen):pass