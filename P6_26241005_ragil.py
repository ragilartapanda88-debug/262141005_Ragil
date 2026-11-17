a = int(input("Digit A: "))
b = int(input("Digit B: "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print(f"Kondisi 1: {kondisi1}")
print(f"Kondisi 2: {kondisi2}")

# 4 operasi logika
print(f"NOT: {not kondisi1}")
print(f"AND: {kondisi1 and kondisi2}")
print(f"OR : {kondisi1 or kondisi2}")
print(f"XOR: {kondisi1 ^ kondisi2}")

# Komentar: OR bernilai True jika salah satu atau kedua kondisi True, sedangkan XOR hanya True jika kondisinya berbeda, jadi ketika kedua True, OR=True tapi XOR=False