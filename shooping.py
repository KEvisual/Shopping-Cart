foods = []
prices = []
total = 0

print("======= WARMING ROLZZZ =======")

while True:
    food = input("untuk beli makanan (f buat keluar aplikasi) :")
    if food.lower() == "f":
        break
    else:
        price = float(input(f"untuk mengetahui harga sebuah {food}: Rp."))
        foods.append(food)
        prices.append(price)
        
print("======= KERANJANG BELANJAAN ANDA =======")

for food in foods:
    print(food)
    
for price in prices:
    total += price

print("")
print(f"Total harga anda adalah Rp.{total}")