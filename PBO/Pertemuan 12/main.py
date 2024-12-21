from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
#Import Library Mysql-Connector
import mysql.connector

class InputForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mydb = mysql.connector.connect(
            host    = "localhost",
            user    = "root",
            password= "",
            database="sikampus"
        )
        self.mycursor = self.mydb.cursor()
        self.update_id = None
    def show_data(self):
        try:
            # Ambil data dari text input
            nama = self.ids.nama_input.text
            nim = self.ids.nim_input.text
            jurusan = self.ids.jurusan_input.text
            #Validasi Inputan tidak kosong
            if not nama or not nim or not jurusan:
                popup = Popup(title="Error", 
                content=Label(text="Semua field harus diisi."), 
                size_hint=(0.8, 0.4), auto_dismiss=True)
                popup.open()
                return

            #Insert data ke database
            sql = "INSERT INTO tbl_mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)"
            val = (nama, nim, jurusan)
            try:
                self.mycursor.execute(sql, val)
                self.mydb.commit()
            except Exception as e:
                popup = Popup(
                    title="Database Error",
                    content=Label(text=f"Error: {e}"),
                    size_hint=(0.8, 0.4),
                    auto_dismiss=True
                )
                popup.open()
                return

            #RESET
            self.ids.nama_input.text = ""
            self.ids.nim_input.text = ""
            self.ids.jurusan_input.text = ""
            self.show_table()
        except Exception as e:
            popup = Popup(
                title ="Error",
                content=Label(text=f"Error: {e}"),
                size_hint=(0.8, 0.4),
                auto_dismiss=True
        )
            popup.open()
    def show_table(self):
        self.mycursor.execute("SELECT nama, nim, jurusan FROM tbl_mahasiswa")
        data_mahasiswa = self.mycursor.fetchall()
        self.ids.tabel_mahasiswa.clear_widgets()
        self.ids.tabel_mahasiswa.add_widget(Label(text="No", bold=True, size_hint_x=None, width=40))
        self.ids.tabel_mahasiswa.add_widget(Label(text="Nama", bold=True, size_hint_x=None, width=120))
        self.ids.tabel_mahasiswa.add_widget(Label(text="Nim", bold=True, size_hint_x=None, width=80))
        self.ids.tabel_mahasiswa.add_widget(Label(text="Jurusan", bold=True, size_hint_x=None, width=150))
        self.ids.tabel_mahasiswa.add_widget(Label(text="Aksi", bold=True, size_hint_x=None, width=50))
        self.ids.tabel_mahasiswa.add_widget(Label(text="", bold=True, size_hint_x=None, width=50))
        for index, row in enumerate(data_mahasiswa, start=1):
            self.ids.tabel_mahasiswa.add_widget(Label(text=str(index), size_hint_x=None, width=40))
            self.ids.tabel_mahasiswa.add_widget(Label(text=row[0], size_hint_x=None, width=120))
            self.ids.tabel_mahasiswa.add_widget(Label(text=row[1], size_hint_x=None, width=80))
            self.ids.tabel_mahasiswa.add_widget(Label(text=row[2], size_hint_x=None, width=150))
            delete_btn = Button(text="DELETE", size_hint_x=None, width=50, font_size=10)
            delete_btn.bind(on_release=lambda btn, row=row: self.delete_data(row[1])) 
            self.ids.tabel_mahasiswa.add_widget(delete_btn)
            update_btn = Button(text="UPDATE", size_hint_x=None, width=50, font_size=10)
            update_btn.bind(on_release=lambda btn, row=row: self.update_data(row[1])) 
            self.ids.tabel_mahasiswa.add_widget(update_btn)
    
    def update_data(self, nim):
        try:
            query= "SELECT nama, nim, jurusan FROM tbl_mahasiswa WHERE nim = %s"
            self.mycursor.execute(query, (nim,))
            result = self.mycursor.fetchone()
            if result:
                self.ids.nama_input.text = result[0]
                self.ids.nim_input.text = result[1]
                self.ids.jurusan_input.text = result[2]
                self.update_id = nim
                self.ids.tombol_simpan.text = "Update Data"
                self.ids.nim_input.readonly = True
                self.ids.tombol_simpan.unbind(on_release=self.show_data)
                self.ids.tombol_simpan.bind(on_release=self.update_data_submit)
            else:
                self.show_error_popup("Data tidak ditemukan")
        except Exception as e:
            self.show_error_popup(f"Error: {e}")
    
    def update_data_submit(self, instance):
        try:
            nama = self.ids.nama_input.text
            nim = self.ids.nim_input.text
            jurusan = self.ids.jurusan_input.text
            if not nama or not nim or not jurusan:
                self.show_error_popup("Semua kolom harus diisi!")
                return
            query = "UPDATE tbl_mahasiswa SET nama = %s, nim = %s, jurusan = %s WHERE nim = %s"
            values = (nama, nim, jurusan, nim)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            #RESET form dan tombol
            self.ids.nama_input.text=""
            self.ids.nim_input.text=""
            self.ids.jurusan_input.text=""
            self.ids.tombol_simpan.text = "Simpan"
            self.ids.tombol_simpan.unbind(on_release=self.update_data_submit)
            self.ids.tombol_simpan.bind(on_release=self.show_data)
            #REFRESH
            self.show_table()
            self.show_success_popup("Data berhasil diupdate!")
        except Exception as e:
            self.show_error_popup(f"Gagal memperbarui data: {e}")
    
    def show_error_popup(self, message):
        popup = Popup(
            title="Error",
            content=Label(text=message),
            size_hint=(0.6, 0.4))
        popup.open()
    def show_success_popup(self, message):
        popup = Popup(
            title="Success",
            content=Label(text=message),
            size_hint=(0.6, 0.4))
        popup.open()
    def delete_data(self, nim):
        try:
            confirm_popup = Popup(
                title="Konfirmasi Hapus",
                content=Label(text="Apakah Anda yakin ingin menghapus dengan NIM = {nim}?"),
                size_hint=(0.6, 0.4)
            )
            btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=40)
            btn_yes = Button(text="Ya", size_hint_x=0.5)
            btn_no = Button(text="Batal", size_hint_x=0.5)

            #Konfirmasi
            btn_yes.bind(on_press=lambda instanse: self.confirm_delete(nim, confirm_popup))
            btn_no.bind(on_press=confirm_popup.dismiss)
            btn_layout.add_widget(btn_yes)
            btn_layout.add_widget(btn_no)
            confirm_popup.content = BoxLayout(orientation='vertical', spacing=10)
            confirm_popup.content.add_widget(Label(text=f"Apakah Anda yakin ingin menghapus data dengan NIM = {nim}?"))
            confirm_popup.content.add_widget(btn_layout)
            confirm_popup.open()
        except Exception as e:
            self.show_error_popup(f"Gagal Menghapus Data{str(e)}")
    
    def confirm_delete(self, nim, confirm_popup):
        try:
            sql = "DELETE FROM tbl_mahasiswa WHERE nim = %s"
            val = (nim,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            confirm_popup.dismiss()
            self.show_table()
        except Exception as e:
            self.show_error_popup(f"Gagal Menghapus Data: {str(e)}")
    # def show_data(self):
    #     # Ambil data dari text input
    #     nama = self.ids.nama_input.text
    #     nim = self.ids.nim_input.text
    #     jurusan = self.ids.jurusan_input.text
    #     # Format data untuk ditampilkan
    #     data = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}"
    #     # Buat PopUp
    #     popup = Popup(
    #         title="Data Mahasiswa",
    #         content=Label(text=data), 
    #         size_hint=(0.8, 0.4),
    #         auto_dismiss=True,
    #     )

    #     # Tambahkan tombol untuk menutup pop-up
    #     content = BoxLayout(orientation='vertical')
    #     content.add_widget(Label(text=data))
    #     close_btn = Button(text="Tutup", size_hint_y=None, height=40)
    #     close_btn.bind(on_release=popup.dismiss)
    #     popup.content.add_widget(close_btn)

        
    #     # Tampilkan pop-up
    #     popup.open()
        
    def on_close(self):
        self.mycursor.close()
        self.mydb.close()
        
class form2(App):
    def build(self):
        self.get_color_from_hex = get_color_from_hex # Utility Warna
        self.root_widget = InputForm()
        return self.root_widget

    def on_start(self):
        Window.size = (1000, 600)
        self.title = "Formulir Pendaftaran Mahasiswa"
        self.icon = 'logo.png'
        self.root_widget.show_table()
    def on_stop(self):
        self.root_widget.on_close()
if __name__ == "__main__":
    form2().run()