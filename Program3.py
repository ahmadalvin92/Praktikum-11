#3

from datetime import *
import Program1

fileTeks = open('List Daftar Peminjam Buku.txt', 'r')
isiTeks = fileTeks.readlines()

kodeBuku = input('Masukkan Kode Member : ')

for x in range(len(isiTeks)) :
    if (kodeBuku in isiTeks[x]) :
        membagi = isiTeks[x].split('|')
        statusBuku = 'ada'
        break
    
    else :
        statusBuku = 'tidak ada'
        continue

if (statusBuku == 'ada'):
    print('Data Peminjam Buku')
    print('Kode Member   : ', membagi[0])
    print('Nama Member  : ', membagi[1])
    print('Judul Buku          : ', membagi[2])
    print('Tanggal Mulai Peminjaman         : ', membagi[3])
    print('Tangal Pengambilan Maksimal    : ', membagi[4])
    print('Tanggal Pengembalian Buku        : ', datetime.date(datetime.now()))

    telatPengembalian = Program1. diffDate(membagi[4])
    dendaTelat = 2000 * abs(telatPengembalian)

    if(telatPengembalian >= 0 ) :
        print('Terlambat : 0 hari')
        print('Denda       : 0')
    else :
        print('Terlambat : ', abs(telatPengembalian))
        print('Denda       : ', dendaTelat)
else :
    print('Peminjaman Buku Tidak Ada')
            
