from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from notmain import validate_email
from client import c


class analyserApp(MDApp):
    format = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.screen = Builder.load_file("analyser360.kv")
        l = ["Word document", "PDF"]
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.do(x),
            }
            for i in l
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )

    def do(self, text_item):
        self.format = text_item
        self.screen.ids.welcome_label.text = "Click on done to send file"

    def send(self):
        filename = self.screen.ids.filename.text
        email = self.screen.ids.user.text
        c(filename, email, self.format)

    def build(self):
        self.screen.ids.user.bind(
            on_text_validate=self.set_error_message, on_focus=self.set_error_message
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        email = self.screen.ids.user.text
        if validate_email(email):
            self.screen.ids.user.error = False
        else:
            self.screen.ids.user.error = True


analyserApp().run()
