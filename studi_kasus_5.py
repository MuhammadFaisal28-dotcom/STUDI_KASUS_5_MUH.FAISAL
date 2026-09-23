from datetime import datetime

def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar.lower() == "standar":
        tarif = 200000
    elif jenis_kamar.lower() == "deluxe":
        tarif = 350000
    else:
        return 0

    total = tarif * lama_menginap
    return total

jenis_kamar = input("pilih jenis kamar (standar/deluxe): ")
check_in = input("masukkan tanggal check_in (DD-MM-YYYY): ")
check_out = input("masukkan tanggal check_out (DD-MM-YYYY): ")

tanggal_masuk = datetime.strptime(check_in, "%d-%m-%Y")
tanggal_keluar = datetime.strptime(check_out, "%d-%m-%Y")

lama_menginap = (tanggal_keluar - tanggal_masuk).days

total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

print("="*30)
print("     STRUK PEMESANAN")
print("="*30)
print("jenis kamar          :", jenis_kamar)
print("tanggal check in     :", check_in)
print("tanggal check out    :", check_out)
print("lama menginap        :", lama_menginap, "malam")
print("="*30)
print("total harga          :Rp.", format(total_biaya, ","))
print("="*30)