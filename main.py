from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import socket

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15
    
    TextInput:
        id: ip_input
        hint_text: 'IP сервера'
        font_size: '18sp'
    
    TextInput:
        id: port_input
        hint_text: 'Порт'
        input_filter: 'int'
        font_size: '18sp'
    
    TextInput:
        id: msg_input
        hint_text: 'Сообщение для локальной сети'
        font_size: '18sp'
    
    Button:
        text: 'Отправить сообщение'
        font_size: '24sp'
        on_press: app.send_command(ip_input.text, int(port_input.text), msg_input.text)
    
    Label:
        id: status
        text: 'Статус: ожидание'
'''

class SocketApp(App):
    def send_command(self, ip, port, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)  # Таймаут 3 секунды
                s.connect((ip, port))
                s.sendall(message.encode("UTF-8"))
                response = s.recv(1024)
                self.root.ids.status.text = f"Успешно! Ответ: {response.decode()}"
        except Exception as e:
            self.root.ids.status.text = f"Ошибка: {str(e)}"

    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    SocketApp().run()
