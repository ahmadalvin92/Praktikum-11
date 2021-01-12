#1

from datetime import *

def diffDate (x) :
    membagi = x.split('-')
    listHari = []
    
    for y in membagi :
        listHari.append(int(y))

    hari = date(listHari[0], listHari[1], listHari[2])
    hariIni = datetime.date(datetime.now())

    selisihHari = hari - hariIni
    hasilSelisih = abs(selisihHari.days)
    
    return hasilSelisih


'''
print(diffDate('2021-01-20'))
print(diffDate('2020-12-20'))
print(diffDate('2022-09-10'))
'''

'''
#Membuat Input dan mengatasi jika input tidak sesuai
try :
    hariSekarang = input('Silahkan Masukkan Tanggal , dengan Format (yyyy-mm-dd) : ')
    diff = diffDate(hariSekarang)
    #Membuat Output dari hasil perhitungan selisih
    print ('Selisih dengan tanggal yang di input adalah : ', diff, 'hari')
except ValueError :
    print('Jangan ada spasi/tidak valid')
'''
