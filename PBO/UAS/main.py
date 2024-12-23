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
            database="deltaromeo"
        )
        self.mycursor = self.mydb.cursor()
        self.update_id = None
    def show_data(self):
        try:
            # Ambil data dari text input
            id_brg = self.ids.idbarang_input.text
            nama_barang = self.ids.nmbarang_input.text
            harga = self.ids.harga_input.text
            stok = self.ids.stok_input.text
            #Validasi Inputan tidak kosong
            if not nama_barang or not id_brg or not stok or not harga:
                popup = Popup(title="Error", 
                content=Label(text="Semua field harus diisi."), 
                size_hint=(0.8, 0.4), auto_dismiss=True)
                popup.open()
                return

            #Insert data ke database
            sql = "INSERT INTO barang (id_brg, nama_barang, harga, stok) VALUES (%s, %s, %s, %s)"
            val = (id_brg, nama_barang, harga, stok)
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
            self.ids.idbarang_input.text = ""
            self.ids.nmbarang_input.text = ""
            self.ids.harga_input.text = ""
            self.ids.stok_input.text = ""
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
        self.mycursor.execute("SELECT id_brg, nama_barang, harga, stok FROM barang")
        barang = self.mycursor.fetchall()
        self.ids.tabel_barang.clear_widgets()
        self.ids.tabel_barang.add_widget(Label(text="No", bold=True, size_hint_x=None, width=40))
        self.ids.tabel_barang.add_widget(Label(text="ID Barang", bold=True, size_hint_x=None, width=120))
        self.ids.tabel_barang.add_widget(Label(text="Nama Barang", bold=True, size_hint_x=None, width=80))
        self.ids.tabel_barang.add_widget(Label(text="Harga", bold=True, size_hint_x=None, width=150))
        self.ids.tabel_barang.add_widget(Label(text="Stok", bold=True, size_hint_x=None, width=150))
        self.ids.tabel_barang.add_widget(Label(text="Aksi", bold=True, size_hint_x=None, width=50))
        self.ids.tabel_barang.add_widget(Label(text="", bold=True, size_hint_x=None, width=50))
        for index, row in enumerate(barang, start=1):
            self.ids.tabel_barang.add_widget(Label(text=str(index), size_hint_x=None, width=40))
            self.ids.tabel_barang.add_widget(Label(text=row[0], size_hint_x=None, width=120))
            self.ids.tabel_barang.add_widget(Label(text=row[1], size_hint_x=None, width=80))
            self.ids.tabel_barang.add_widget(Label(text=row[2], size_hint_x=None, width=150))
            self.ids.tabel_barang.add_widget(Label(text=row[3], size_hint_x=None, width=150))
            # self.ids.tabel_barang.add_widget(Label(text=row[4], size_hint_x=None, width=150))
            # self.ids.tabel_barang.add_widget(Label(text=row[5], size_hint_x=None, width=150))
            delete_btn = Button(text="DELETE", size_hint_x=None, width=50, font_size=10)
            delete_btn.bind(on_release=lambda btn, row=row: self.delete_data(row[1])) 
            self.ids.tabel_barang.add_widget(delete_btn)
            update_btn = Button(text="UPDATE", size_hint_x=None, width=50, font_size=10)
            update_btn.bind(on_release=lambda btn, row=row: self.update_data(row[1])) 
            self.ids.tabel_barang.add_widget(update_btn)
    def update_data(self, id_brg):
        try:
            query= "SELECT id_brg, nama_barang, harga, stok FROM barang WHERE id_brg = %s"
            self.mycursor.execute(query, (id_brg,))
            result = self.mycursor.fetchone()
            if result:
                self.ids.idbarang_input.text = result[0]
                self.ids.nmbarang_input.text = result[1]
                self.ids.harga_input.text = result[2]
                self.ids.stok_input.text = result[3]
                self.update_id = id_brg
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
            id_brg = self.ids.idbarang_input.text
            nama_barang = self.ids.nmbarang_input.text
            harga = self.ids.harga_input.text
            stok = self.ids.stok_input.text
            if not nama_barang or not id_brg or not harga or not stok:
                self.show_error_popup("Semua kolom harus diisi!")
                return
            query = "UPDATE barang SET nama_barang = %s, id_brg = %s, harga = %s WHERE id_brg = %s"
            values = (nama_barang, id_brg, harga, stok, id_brg)
            self.mycursor.execute(query, values)
            self.mydb.commit()
            #RESET form dan tombol
            self.ids.idbarang_input.text=""
            self.ids.nmbarang_input.text=""
            self.ids.harga_input.text=""
            self.ids.stok_input.text=""
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
    def delete_data(self, id_brg):
        try:
            confirm_popup = Popup(
                title="Konfirmasi Hapus",
                content=Label(text="Apakah Anda yakin ingin menghapus dengan ID Barang = {id_brg}?"),
                size_hint=(0.6, 0.4)
            )
            btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=40)
            btn_yes = Button(text="Ya", size_hint_x=0.5)
            btn_no = Button(text="Batal", size_hint_x=0.5)

            #Konfirmasi
            btn_yes.bind(on_press=lambda instance: self.confirm_delete(id_brg, confirm_popup))
            btn_no.bind(on_press=confirm_popup.dismiss)
            btn_layout.add_widget(btn_yes)
            btn_layout.add_widget(btn_no)
            confirm_popup.content = BoxLayout(orientation='vertical', spacing=10)
            confirm_popup.content.add_widget(Label(text=f"Apakah Anda yakin ingin menghapus data dengan ID Barang = {id_brg}?"))
            confirm_popup.content.add_widget(btn_layout)
            confirm_popup.open()
        except Exception as e:
            self.show_error_popup(f"Gagal Menghapus Data{str(e)}")
    
    def confirm_delete(self, id_brg, confirm_popup):
        try:
            sql = "DELETE FROM barang WHERE id_brg = %s"
            val = (id_brg,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            confirm_popup.dismiss()
            self.show_table()
        except Exception as e:
            self.show_error_popup(f"Gagal Menghapus Data: {str(e)}")
        
    def on_close(self):
        self.mycursor.close()
        self.mydb.close()
        
class deltaromeo(App):
    def build(self):
        self.get_color_from_hex = get_color_from_hex # Utility Warna
        self.root_widget = InputForm()
        return self.root_widget

    def on_start(self):
        Window.size = (1000, 600)
        self.title = "DELTAROMEO"
        self.icon = 'logo.png'
        self.root_widget.show_table()
    def on_stop(self):
        self.root_widget.on_close()
if __name__ == "__main__":
    deltaromeo().run()