import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from plyer import tts

class AIMB3(App):
    def build(self):
        # Cấu hình nền tối cho đỡ mỏi mắt trên S24 Ultra
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        # Tiêu đề linh bảo
        self.label = Label(
            text='[b]AI-MB-3 CORE[/b]', 
            markup=True,
            font_size='30sp', 
            color=(0, 0.8, 1, 1),
            size_hint=(1, 0.2)
        )
        
        # Ô nhập liệu thông minh
        self.input = TextInput(
            text='Chào Minh Chủ, hệ thống AI-MB-3 đã sẵn sàng xuất thế!',
            font_size='22sp',
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            multiline=True,
            padding=[20, 20]
        )
        
        # Nút kích hoạt pháp trận giọng nói
        btn = Button(
            text='KÍCH HOẠT GIỌNG NÓI',
            size_hint=(1, 0.25),
            background_normal='',
            background_color=(0, 0.5, 0.8, 1),
            font_size='20sp',
            bold=True
        )
        btn.bind(on_press=self.speak_now)
        
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def speak_now(self, instance):
        try:
            val = self.input.text
            if val:
                tts.speak(val)
        except Exception as e:
            self.label.text = "Lỗi linh lực: Hệ thống đang bận"

if __name__ == "__main__":
    AIMB3().run()

