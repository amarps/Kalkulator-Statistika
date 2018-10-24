'''
CopyRight By Senjaya 2018 All Right Reserved
'''
# for make true division
from __future__ import division
# import module from kivy
from kivy.app import App
from kivy.config import Config

# configuration for device size
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '420')
Config.set('graphics', 'resizable', '0')

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# import Internal Library
import statistics, math, random

class statistika(App):

# like constructor but for kivy application
    def on_start(self):
        self.input_distribusi = self.root.ids.input_distribusi

# Button Handler
        self.root.ids.submit_distribusi.bind(
            on_release=self.hitungdatadistribusi)

# Register Font To Application
        LabelBase.register(name='Roboto',
                            fn_regular='Roboto-Medium.ttf',
                            fn_bold='Roboto-Bold.ttf')

# Basic Function
    def change_btn_color(self, *args):
        color = [random.random() for i in range(3) + [1]]
        self.menu_btn_color = color 

    def hitungjangkauan(self, num):
        a = num.sort()
        a = num[-1] - num[0]
        return a

    def hitungjumlahkelas(self, num):
        a = 1 + 3.322 * math.log10(len(num))
        math.floor(a)
        return a

    def hitunginterval(self, jangkauan, jumlahkelas):
        a = jangkauan / jumlahkelas
        return a

    def hitungmodus(self, a):
        for i in a:
            if a.count(i) >= 2:
                try:
                    modus = str(statistics.mode(a))
                except Exception as err:
                    modus = 'lebih dari 1'
            else:
                modus = 'ngga ada modus'
        return modus

    def median(self, data):
        l_data = len(data)
        idx_tengah = int(l_data / 2)
        if l_data % 2 != 0:
            return data[idx_tengah]
        return (data[idx_tengah-1] + data[idx_tengah]) / 2

    def nilai_set_bawah(self, data):
        idx_tengah = math.floor(len(data) / 2)    
        return(data[0:idx_tengah])

    def nilai_set_atas(self, data):
        idx_tengah = math.ceil(len(data) / 2)
        return(data[idx_tengah:])

    def quartile(self, data):
        data.sort()
        q1 = self.median(self.nilai_set_bawah(data))
        q2 = self.median(data)
        q3 = self.median(self.nilai_set_atas(data))
        qr = q3 - q1
        return q1, q2, q3, qr

    def hitungdatadistribusi(self, *args):
        a = self.input_distribusi.text
        a = self.data_filter(a)
        modus = self.hitungmodus(a)
        median = statistics.median(a)
        mean = statistics.mean(a)
        jangkauan = self.hitungjangkauan(a)
        jumlahKelas = math.ceil(self.hitungjumlahkelas(a))
        interval = self.hitunginterval(jangkauan, jumlahKelas)
        q1, q2, q3, qr = self.quartile(a)

        self.root.ids.hasil_data_distribusi.text = str(jangkauan) + '\n\n' + str(
        jumlahKelas) + '\n\n' + str(interval) + '\n\n'+ str(math.ceil(interval)) + '\n\n' + str(
        statistics.mean(a)) + '\n\n' + str(statistics.median(a)) + '\n\n' + modus + '\n\n' + str(
        q1) + '\n\n' + str(q2) + '\n\n' + str(q3) +'\n\n' + str(qr)

    def data_filter(self, a, func=None):
        a = a.replace(' ', '').split(',')
        if len(a) <= 1:
            return 'Masukan lebih dari 1 data'
        if a[0].isalpha():
            return 'Masukan angka bukan teks'
        for i in a:
            if i == '':
                a.remove('')
        a = list(map(int, a))
        return a


if __name__ == '__main__':
# coloring the background application
    Window.clearcolor = get_color_from_hex('#fefeff')
# application Running
    statistika().run()