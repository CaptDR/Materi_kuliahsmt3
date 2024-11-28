from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class HelloWorld(BoxLayout):
    pass
class HelloWorldApp(App):
    def build (self):
        return HelloWorld()
if __name__ == '__main__':
    HelloWorldApp().run()