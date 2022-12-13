import os, re, threading
import time

class jumlah(threading.Thread):
    def __init__(self, awal, akhir):
        threading.Thread.__init__(self)
        self.awal=awal
        self.akhir=akhir

    def run(self):
        self.hasil=0
        for suffix in range (self.awal, self.akhir+1):
            self.hasil = self.hasil + self.suffix
            print(self.suffix, "=", self.hasil)

    def hasil(self):
        return self.hasil

start = time.time

#memanggil thread
hitung1=jumlah(1, 5000000)
hitung2=jumlah(500001, 10000)

#menjalankan thread
hitung1.start()
hitung2.start()

#menampilkan hasil thread
hitung1.hasil()


end = time.time()
print(end-start)