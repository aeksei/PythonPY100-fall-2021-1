BYTES_ONE_CHAR = 1

pages = 100
lines = 50
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars  # TODO общее количество символов в книге
total_bytes = total_chars * BYTES_ONE_CHAR  # TODO размер одной книги в байтах

disk_size = 1.44 * 1024 * 1024  # TODO размер дискеты в байтах

print(disk_size // total_bytes)  # TODO найти количество книг, которое поместится на дискете
