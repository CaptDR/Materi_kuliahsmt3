from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
class HelloWorld(BoxLayout):
    pass
class HelloWorldApp(App):
    def build (self):
        Builder.load_file('main.kv')
        return HelloWorld()
if __name__ == '__main__':
    HelloWorldApp().run()