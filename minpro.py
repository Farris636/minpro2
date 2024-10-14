# pilih role
def pilih():
    print("==========LOGIN==========")
    print("1. Admin")
    print("2. User")
    print("=========================")
    login = input("Login sebagai: ")
    if login == "1":
        admin()
    elif login == "2":
        user()
    else:
        print("role anda tidak ada")
print()

# tabel
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["nama", "ip address", "subnetmask", "network address", "DNS"]
def tambah_data(nama, ip, subnetmask, network, dns):
    table.add_row([nama, ip, subnetmask, network, dns])

tambah_data("adit","192.168.10.10", "255.255.255.0", "192.168.10.0", "8.8.8.8")
tambah_data("andi","192.168.20.10", "255.255.255.0", "192.168.20.0", "8.8.8.8")
tambah_data("bima","192.168.30.10", "255.255.255.0", "192.168.30.0", "8.8.8.8")
tambah_data("anto","192.168.40.10", "255.255.255.0", "192.168.40.0", "8.8.8.8")

# untuk menambahkan
def tambah():
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("===============================================================")
    nama = input("masukkan nama: ")
    ip = input("masukkan ip: ")
    subnetmask = input("masukkan subnetmask: ")
    network = input("masukkan network address: ")
    dns = input("masukkan DNS: ")
    tambah_data(nama, ip, subnetmask, network, dns)
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("===============================================================")

# untuk melihat table
def lihat_table():
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("========================================================================")

# untuk mengubah table
def update():
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("===============================================================")
    nama = input("Masukkan nama device yang ingin diupdate: ")
    for update in table._rows:
        if update[0] == nama:
            ip = input("Masukan ip address: ")
            subnetmask = input("Masukkan subnetmask: ")
            network = input("Masukkan ip broadcast: ")
            dns = input("Masukkan DNS: ")
            update[1] = ip
            update[2] = subnetmask
            update[3] = network
            update[4] = dns
            print("Connection berhasil diupdate1")
            print("\n==========================DEVICE CONNECTION===========================")
            print(table)
            print("===============================================================")
            break
    else:
        print("Nama tidak tidak terdapat pada cenection.")

# untuk menghapus data
def hapus_ip():
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("===============================================================")
    nama = input("Masukkan nama device yang ingin dihapus: ")
    for hapus in table._rows:
        if hapus[0] == nama:
            table._rows.remove(hapus)
    print("\n==========================DEVICE CONNECTION===========================")
    print(table)
    print("===============================================================")

# untuk login admin
def admin():
    nama = str(input("masukkan nama: "))
    password = str(input("masukkan password admin: "))
    if nama == "farris" and password == "admin123":
        print("\nHallo", nama)
        print("=====Mode admin==========")
        print("===silahkan pilih menu===")
        print("1. Tambah ip address")
        print("2. Lihat ip address")
        print("3. Ubah ip address")
        print("4. Hapus ip address")
        print("========================")
        pilihan = input("pilih menu nomer: ")
        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            lihat_table()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            hapus_ip()
        else:
            print("pilihan tidak tersedia")
    else:
        ("anda tidak terdaftar")

# untuk login user
def user():
    nama = str(input("masukkan nama anda: "))
    password = str(input("masukkan password anda: "))
    if password == "user123":
        print("\nHallo",nama)
        print("=====Mode user=====")
        print("==silahkan pilih menu==")
        print("1. Tambah ip address")
        print("2. Lihat ip address")
        pilihan = input("pilih menu: ")
        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            lihat_table()

pilih()