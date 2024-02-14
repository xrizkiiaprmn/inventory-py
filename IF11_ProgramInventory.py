import json
from prettytable import PrettyTable

def inputData():
    count = input('Berapa data yang ingin kamu masukkan? ')
    with open('inventory.json', 'r') as openfile:
        data = json.load(openfile)

    for i in range(int(count)):
        print(f'\n===== INPUT DATA {i+1} =====')
        nama = input('Masukkan nama barang\t\t: ')
        kuantitas = int(input('Masukkan kuantitas barang\t: '))
        harga = int(input('Masukkan harga barang\t\t: '))
        jumlah = harga * kuantitas

        barang = {
            "nama": nama,
            "kuantitas": kuantitas,
            "harga": harga,
            "jumlah": jumlah
        }

        data.append(barang)
    
    json_object = json.dumps(data, indent=4)
 
    with open("inventory.json", "w") as outfile:
        outfile.write(json_object)

    print('\nBerhasil, data tersimpan!')

def printData(data):
    t = PrettyTable(['No', 'Nama', 'Kuantitas', 'Harga', 'Jumlah'])
    no = 0
    
    for i in data:
        no += 1
        t.add_row([no, i["nama"], i["kuantitas"], i["harga"], i["jumlah"]])

    print('\n============= DATA INVENTORY =============') 
    print(t)

def printAllData():
    with open('inventory.json', 'r') as openfile:
        data = json.load(openfile)

    t = PrettyTable(['No', 'Nama', 'Kuantitas', 'Harga', 'Jumlah'])
    no = 0
    
    for i in data:
        no += 1
        t.add_row([no, i["nama"], i["kuantitas"], i["harga"], i["jumlah"]])

    print('\n============= DATA INVENTORY =============') 
    print(t)

def filterData():
    print('''============= FILTER DATA =============
      
Filter Berdasarkan :
1. Abjad A-Z
2. Abjad Z-A
3. Harga Terkecil - Terbesar
4. Harga Terbesar - Terkecil''')
    chosee = input('\nMasukkan pilihan\t\t: ')
    with open('inventory.json', 'r') as openfile:
        data = json.load(openfile)

    match chosee:
        case '1':
            data.sort(key=lambda x: x["nama"])
            printData(data)
        case '2':
            data.sort(key=lambda x: x["nama"], reverse=True)
            printData(data)
        case '3':
            data.sort(key=lambda x: x["harga"])
            printData(data)
        case '4':
            data.sort(key=lambda x: x["harga"], reverse=True)
            printData(data)
        case _:
            print('Masukkan dengan pilihan yang ada')

def searchData():
    print('\n============== SEARCH DATA ==============')
    searchKey = input('Masukkan kata kunci\t\t: ')

    with open('inventory.json', 'r') as openfile:
        data = json.load(openfile)

    searchData = []
    for sub in data:
        if searchKey.lower() in sub['nama'].lower():
            searchData.append(sub)
            
    
    printData(searchData)


print('''================= PROGRAM INVENTORY =================
      
Program Menu :
1. Masukkan Data
2. Tampilkan Data
3. Tampilkan Data Berdasarkan Filter
4. Pencarian Data''')

chosee = input('\nMasukkan pilihan\t\t: ')

match chosee:
    case '1':
        inputData()
    case '2':
        printAllData()
    case '3':
        filterData()
    case '4':
        searchData()
    case _:
        print('Masukkan dengan pilihan yang ada!')
