import threading
import time
import datetime


word_number = 0
def write_words(word_count, file_name):
    time.sleep(0.1)
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1} \n')
    print(f'Завершилась запись в файл {file_name}')


dct = {10: 'example1.txt', 30: 'example2.txt', 200: 'example3.txt', 100: 'example4.txt'}

beginning_time = datetime.datetime.now()
for i, j in dct.items():
    write_words(i, j)
ending_time = datetime.datetime.now()
print(f'Работа потоков {ending_time - beginning_time} ')

beginning_time = datetime.datetime.now()
thred1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thred2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thred3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thred4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thred1.start()
thred1.join()
thred2.start()
thred2.join()
thred3.start()
thred3.join()
thred4.start()
thred4.join()
ending_time = datetime.datetime.now()
print(f'Работа потоков {ending_time - beginning_time}')