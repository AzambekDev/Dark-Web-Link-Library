from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random
import pyperclip
from kivy.config import Config
from kivy.core.window import Window
from datetime import datetime
from kivy.animation import Animation

class AnimatedButton(Button):
    def __init__(self, **kwargs):
        super(AnimatedButton, self).__init__(**kwargs)

    def start_animation(self):
        anim = Animation(background_color=(0.1, 0.6, 0.3, 1), duration=0.5) + Animation(background_color=(0, 0, 0, 1), duration=0.5)
        anim.repeat = True
        anim.start(self)

class DarkWebLinksLibrary(App):
    def __init__(self, **kwargs):
        super(DarkWebLinksLibrary, self).__init__(**kwargs)
        self.external_list = self.read_external_list()
        self.shown_links = []
        self.time_label = Label(font_size=20, color=[0, 1, 0, 1])

    def build(self):
        self.setup_window()
        layout = self.setup_layout()
        self.setup_widgets(layout)
        Clock.schedule_interval(self.update_time, 1)  # Update time every second
        return layout

    def setup_window(self):
        # Dynamically set window size based on content
        min_width = 300
        min_height = 200
        content_width = 980
        content_height = 500

        text_width = len("Welcome to DWLL or Dark Web Links Library") * 35  # Assuming the largest label is the header
        max_content_width = max(text_width, content_width)
        max_content_height = content_height  # Assuming the height is constant

        width = max(min_width, max_content_width)
        height = max(min_height, max_content_height)

        Config.set('graphics', 'width', str(width))
        Config.set('graphics', 'height', str(height))

    def setup_layout(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.bind(size=self._update_sizes)
        return layout

    def setup_widgets(self, layout):
        header_label = self.create_label("Welcome to DWLL or Dark Web Links Library", font_size=35, bold=True, color=[0, 1, 0, 1])
        disclaimer_label = self.create_label("With over a thousand links, you can find anything you desire.\n"
                                   "Creator: AzambekDev\n"
                                   "DISCLAIMER: LINKS MAY LEAD TO ILLEGAL WEBSITES. USE AT YOUR OWN RISK!!!", color=[0, 1, 0, 1])

        self.result_label = self.create_label("", font_size=18, color=[0, 1, 0, 1])

        random_button = self.create_button("Get Random Link", self.get_random_link, background_color=[0.1, 0.6, 0.3, 1])
        copy_button = self.create_button("Copy Link", self.copy_link, background_color=[0.1, 0.6, 0.3, 1])
        exit_button = self.create_button("Exit", self.on_exit, background_color=[0.1, 0.6, 0.3, 1])
        
        # Add social media buttons
        Programmer_Network_button = self.create_social_button("Programmer.Network", "https://programmer.network/azambekdev", background_color=[0.1, 0.6, 0.3, 1])
        instagram_button = self.create_social_button("Instagram", "https://instagram.com/thymustcode", background_color=[0.1, 0.6, 0.3, 1])
        github_button = self.create_social_button("GitHub", "https://github.com/AzambekDev", background_color=[0.1, 0.6, 0.3, 1])

        layout.add_widget(header_label)
        layout.add_widget(disclaimer_label)
        layout.add_widget(self.result_label)
        button_layout = BoxLayout(spacing=10)
        button_layout.add_widget(random_button)
        button_layout.add_widget(copy_button)
        button_layout.add_widget(exit_button)
        layout.add_widget(button_layout)
        
        social_layout = BoxLayout(spacing=10)
        social_layout.add_widget(Programmer_Network_button)
        social_layout.add_widget(instagram_button)
        social_layout.add_widget(github_button)
        layout.add_widget(social_layout)
        
        layout.add_widget(self.time_label)

    def create_label(self, text, **kwargs):
        label = Label(text=text, **kwargs)
        anim = Animation(color=[1, 1, 1, 1], duration=1) + Animation(color=[0, 1, 0, 1], duration=1)
        anim.repeat = True
        anim.start(label)
        return label

    def create_button(self, text, callback, **kwargs):
        button = AnimatedButton(text=text, on_release=callback, **kwargs)
        button.background_normal = ''
        button.background_color = (0, 0, 0, 1)  # Initial color is black
        button.color = [1, 1, 1, 1]
        button.font_size = 20
        button.padding = [15, 5]
        button.start_animation()  # Start the background animation
        return button
    
    def create_social_button(self, text, link, **kwargs):
        button = AnimatedButton(text=text, on_release=lambda x: self.open_url(link), **kwargs)
        button.background_normal = ''
        button.background_color = (0, 0, 0, 1)  # Initial color is black
        button.color = [1, 1, 1, 1]
        button.font_size = 20
        button.padding = [15, 5]
        button.start_animation()  # Start the background animation
        return button

    def read_external_list(self):
        try:
            with open("python/external_list.txt", "r") as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("External list file not found.")
            return []

    def get_random_link(self, instance):
        if self.external_list:
            remaining_links = list(set(self.external_list) - set(self.shown_links))
            if remaining_links:
                random_item = random.choice(remaining_links)
                self.shown_links.append(random_item)
                self.result_label.text = random_item
            else:
                self.result_label.text = "No more links remaining."
        else:
            self.result_label.text = "The list is empty."

    def copy_link(self, instance):
        link_to_copy = self.result_label.text
        pyperclip.copy(link_to_copy)

    def on_exit(self, instance):
        self.stop()
        
    def _update_sizes(self, instance, value):
        # When the layout size changes, adjust the window size accordingly
        Window.size = value
    
    def update_time(self, dt):
        # Update the time label with current time
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.text = "Current Time: " + current_time
        
    def open_url(self, link):
        import webbrowser
        webbrowser.open(link)

if __name__ == '__main__':
    DarkWebLinksLibrary().run()
