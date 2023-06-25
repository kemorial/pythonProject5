from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.font_style = "H1"
        return (

                MDLabel(
                    text="Hello, World",

                )

        )


MainApp().run()