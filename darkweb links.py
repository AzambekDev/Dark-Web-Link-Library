from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random
import pyperclip
from kivy.config import Config
Config.set('graphics', 'width', '980')
Config.set('graphics', 'height', '500')

class DarkWebLinksLibrary(App):
    def build(self):
        
        self.external_list = self.read_external_list()
        self.shown_links = []

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        header_label = Label(text="Welcome to DWLL or Dark Web Links Library", font_size=35, bold=True, color=[1, 1, 1, 1])
        disclaimer_label = Label(text="With over a thousand links, you can find anything you desire.\n"
                                      "Creator: itszxiety\n"
                                      "DISCLAIMER: LINKS MAY LEAD TO ILLEGAL WEBSITES. USE AT YOUR OWN RISK!!!",
                                 color=[1, 1, 1, 1])
        self.result_label = Label(text="", font_size=18, color=[1, 1, 1, 1])

        random_button = Button(text="Get Random Link", on_press=self.get_random_link)
        copy_button = Button(text="Copy Link", on_press=self.copy_link)
        exit_button = Button(text="Exit", on_press=self.on_exit)

        layout.add_widget(header_label)
        layout.add_widget(disclaimer_label) 
        layout.add_widget(self.result_label)
        layout.add_widget(random_button)
        layout.add_widget(copy_button)
        layout.add_widget(exit_button)

        return layout

    def read_external_list(self):
        try:
            with open("python\external_list.txt", "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print("External list file not found.")
            return []

    def get_random_link(self, instance):
        if self.external_list:
            remaining_links = list(set(self.external_list) - set(self.shown_links))
            if remaining_links:
                random_item = random.choice(remaining_links)
                self.shown_links.append(random_item)
                random_item
            else:
                random_item = "No more links remaining."
        else:
            random_item = "The list is empty."

    def copy_link(self, instance):
        link_to_copy = self.result_label.text[17:]
        pyperclip.copy(link_to_copy)

    def on_exit(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    DarkWebLinksLibrary().run()                                          
