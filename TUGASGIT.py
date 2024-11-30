data_panen = {
    'lokasi1' : {
        'nama_lokasi':'Kebun A',
        'hasil_panen' : {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2' : {
        'nama_lokasi':'Kebun B',
        'hasil_panen' : {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3' : {
        'nama_lokasi':'Kebun C',
        'hasil_panen' : {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4' : {
        'nama_lokasi':'Kebun D',
        'hasil_panen' : {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5' : {
        'nama_lokasi':'Kebun E',
        'hasil_panen' : {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    },
    #perubahan1
    'lokasi6' : {
        'nama_lokasi':'Kebun F',
        'hasil_panen' : {
            'padi': 1500,
            'jagung': 1000,
            'kedelai': 500
        }
    },
    'lokasi7' : {
        'nama_lokasi':'Kebun G',
        'hasil_panen' : {
            'padi': 1470,
            'jagung': 870,
            'kedelai': 470
        }
    }
}

for i,j in data_panen.items() :
    print(i,j)

hasil = data_panen['lokasi2']['hasil_panen']['jagung']
print(hasil)

nama = data_panen['lokasi3']['nama_lokasi']
print(nama)

for nama, hasil in data_panen.items() :
    nama_lok = hasil['nama_lokasi']
    padi = hasil['hasil_panen']['padi']
    kedelai = hasil['hasil_panen']['kedelai']

    if padi > 1300 or kedelai > 800 :
        print(f"lokasi {nama_lok} memerlukan perhatian khusus")
    else :
        print(f"lokasi {nama_lok} aman")

print('TEST BRANCH')