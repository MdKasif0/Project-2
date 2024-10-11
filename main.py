from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        text:" "
        halign:"center"
        
    MDRaisedButton:
        id: my_button
        text: 'Click me'
        pos_hint:{"center_x":0.5,"center_x":0.5}
        on_release: app.print_hello()
    MDLabel:
        id: output_label
        text: ''
        halign: 'center'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def print_hello(self):
        self.root.ids.output_label.text = "Md Kasif"

if __name__ == '__main__':
    MyApp().run()
