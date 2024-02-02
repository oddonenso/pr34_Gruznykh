from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class RainbowApp(App):
    # Define rainbow_colors as a class attribute
    rainbow_colors = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff8800",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#00ffff",
        "Синий": "#0000ff",
        "Фиолетовый": "#ff00ff"
    }

    def build(self):
        # Основной макет
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Текстовое поле для отображения кода цвета
        color_code_input = TextInput(multiline=False, readonly=True, font_size=20)
        layout.add_widget(color_code_input)

        # Метка для отображения названия цвета
        color_name_label = Label(text="Выберите цвет", font_size=24)
        layout.add_widget(color_name_label)

        # Создание кнопок для каждого цвета радуги
        for color_name, color_code in self.rainbow_colors.items():
            button = Button(text=color_name, background_color=self.hex_to_rgb(color_code))
            button.bind(on_press=self.update_color_info)
            layout.add_widget(button)

        return layout

    def hex_to_rgb(self, hex_code):
        # Преобразование шестнадцатеричного кода в RGB формат
        hex_code = hex_code.lstrip("#")
        return [int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2, 4)]

    def update_color_info(self, instance):
        # Обновление текстового поля и метки при нажатии на кнопку
        color_name = instance.text
        color_code = self.rainbow_colors[color_name]
        self.root.children[0].text = color_code
        self.root.children[1].text = color_name

if __name__ == '__main__':
    RainbowApp().run()
