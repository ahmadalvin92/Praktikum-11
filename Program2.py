#2

from datetime import  *
import os


if (os.path.exists('List Daftar Peminjam Buku.txt')) :
    fileTeksMode = 'a'
else :
    fileTeksMode = 'w'
fileTeks = open('List Daftar Peminjam Buku.txt', fileTeksMode)


while True :

    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member : ')
    judul = input('Masukkan Judul Buku          : ')

    hariPeminjaman = date.today()
    hariDikembalikan = hariPeminjaman + timedelta(days = 7 )

    dataDiriPeminjam = [kode, nama, judul, str(hariPeminjaman), str(hariDikembalikan), '\n']
    fileTeks.write('|'.join(dataDiriPeminjam))

    ulang = input('Ulangi lagi (y/n) : ')

    if (ulang == 'y' or ulang == 'Y') :
        continue
    elif (ulang == 'n' or ulang == 'N') :
        break
    else :
        print('masukkan input yang benar')

fileTeks.close()
