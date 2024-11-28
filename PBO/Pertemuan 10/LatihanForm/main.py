from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix. button import Button

class InputForm(BoxLayout):
    def show_data(self):
        nama    = self.ids.nama_input.text
        nim     = self.ids.nim_input.text
        jurusan = self.ids.jurusan_input.text

        data    = f"Nama : {nama}\nNIM : {nim}\nJurusan : {jurusan}"

        popup = Popup(
            title="Data Mahasiswa",
            content=Label(text=data),
            size_hint=(0.8, 0.4),
            auto_dismiss=True,
        )

        close_btn = Button(text="CLOSE", size_hint_y=None, height=40)
        close_btn.bind(on_release=popup.dismiss)
        popup.content.add_widget(close_btn)

        popup.open()

class FormApp(App):
    def build(self):
        return InputForm()

if __name__ == "__main__":
    FormApp().run()