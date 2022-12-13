import os, re
import time
start = time.time()

jumlah = 0 
for suffix in range(1, 10):
    jumlah = jumlah + suffix
    print("Jumlah ke-", suffix, "hasil", jumlah)

end = time.time()
print(end-start)
