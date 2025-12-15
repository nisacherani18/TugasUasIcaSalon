from models.user import User
from models.service import Service
from models.booking import Booking

while True:
    print("\n=== SISTEM BOOKING BARBERSHOP ===")
    print("1. Tambah Pelanggan")
    print("2. Lihat Layanan")
    print("3. Booking")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama: ")
        hp = input("No HP: ")
        user = User(nama, hp)
        user.add_user()
        print("Pelanggan berhasil ditambahkan")

    elif pilih == "2":
        service = Service()
        layanan = service.show_services()
        for l in layanan:
            print(l)

    elif pilih == "3":
        uid = input("ID User: ")
        sid = input("ID Service: ")
        tanggal = input("Tanggal (YYYY-MM-DD): ")
        booking = Booking(uid, sid, tanggal)
        booking.add_booking()
        print("Booking berhasil")

    elif pilih == "4":
        print("Terima kasih")
        break

    else:
        print("Menu tidak tersedia")
