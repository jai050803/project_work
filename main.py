from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex


class EMSApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the heading label
        heading_label = Label(
            text='EMS App',
            font_size=30,
            color=get_color_from_hex('#00FF00'),  # Green color
            bold=True,
            halign='center',
            valign='middle'
        )

        # Add the heading label to the layout
        layout.add_widget(heading_label)

        # Create a box layout for the buttons with spacing
        button_box = BoxLayout(orientation='vertical', spacing=10)

        # Create five buttons with associated functions
        for i in range(1, 6):
            button_text = f'Button {i}'
            button = Button(
                text=button_text,
                background_normal='',
                background_color=get_color_from_hex('#00FF00'),  # Green color
                color=(0, 0, 0, 1),  # Black text
                font_size=20,
                bold=True,
                size_hint=(None, None),
                size=(200, 50),  # Set the size of the buttons
                padding=(10, 10)
            )
            button.bind(on_press=self.on_button_press)  # Bind the function to the button
            button_box.add_widget(button)

        # Add the button box to the main layout
        layout.add_widget(button_box)

        return layout

    def on_button_press(self, instance):
        print(f'Button "{instance.text}" pressed!')


if __name__ == '__main__':
    EMSApp().run()
