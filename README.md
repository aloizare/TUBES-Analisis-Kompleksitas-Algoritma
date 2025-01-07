# TUGAS BESAR ANALISIS KOMPLEKSITAS ALGORITMA 2025
*Analisis Kinerja Performa Metode Rekursif dan Metode Iteratif dalam Algoritma Sorting: Quick Sort*

### Penjelasan Singkat Tentang *Quick Sort*
Algoritma *sorting* memiliki peran penting dalam pengolahan data, terutama ketika berhadapan dengan *dataset* yang besar. Salah satu algoritma* sorting* yang paling efisien dan sering digunakan adalah *Quick Sort*. *Quick Sort* merupakan metode pengurutan berbasis ***divide and conquer*** yang bekerja dengan memilih elemen *pivot*, kemudian membagi elemen-elemen lainnya ke dalam dua *sub-array* berdasarkan apakah elemen-elemen tersebut lebih kecil atau lebih besar dari *pivot*. Proses ini diulangi secara rekursif hingga seluruh array terurut.

### Requirement
`Python3`

### Implementasi Algoritma
Untuk mendapatkan *dataset* kami membuat kode khusus yang akan memberikan kami *dataset* bilangan acak, kode tersebut dapat dilihat di bawah ini.

    def generate_random_number(ran_num):
    arr = []
    a = 900		#a adalah batas dari bilangan acak yang akan dibuat oleh source code
    for i in range(ran_num):
        arr.append(random.randint(1, a))
    return arr

Di bawah ini merupakan algoritma yang kami gunakan dalam tugas besar kali ini. Terdapat *source code quick sort* secara iteratif dan rekursif, kemudian terdapat juga *best case* dan *worst case scenario* untuk masing-masing algoritma. Tetapi sebelum masuk ke algoritma utama, terdapat algoritma awal yaitu fungsi `partition` yang fungsinya untuk membagi array menjadi dua bagian berdasarkan nilai pivot yang dipilih.

Fungsi *Partition*
```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
*Quick sort* secara iteratif
```python
def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
```
*Quick sort* secara rekursif
```python
def quickSortRecursive(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quickSortRecursive(arr, low, piv - 1)
        quickSortRecursive(arr, piv + 1, high)
```
### Metode Pengujian
Pengujian akan dilakukan terhadap parameter *running time* . Skema pengujian dilakukan sebanyak 2 kasus yaitu *best* dan *worst case* untuk masing-masing algoritma iteratif dan rekursif. *Best case scenario* akan terdiri dari 10, 100, 1.000, 10.000, 100.000, 1 Juta, 10 Juta, dan 100 Juta data, sedangkan *worst case* hanya terdiri dari 10, 50, 100, 250, 500, dan 900 data bilangan acak.
### Analisis
Berdasarkan hasil pengujian, algoritma *quick sort* secara rekursif menunjukkan waktu eksekusi yang lebih cepat dibandingkan metode iteratif pada berbagai ukuran dataset. Sebagai contoh, waktu eksekusi untuk dataset berukuran 10 juta data adalah 85.739 s untuk metode rekursif, sedangkan untuk metode iteratif adalah 85.917 s. Hal yang sama berlaku untuk dataset lainnya, dengan metode rekursif secara konsisten menunjukkan waktu eksekusi yang lebih cepat. Hasil pengujian berupa waktu eksekusi dalam detik (*second*) dapat dilihat pada tabel di bawah.

Tabel hasil *running time best case scenario* dari algoritma* quick sort* secara iteratif dan rekursif

|Data | Iteratif | Rekursif |
| ------------- | ------------- | ------------- |
| 10  | 0.000131 | 0.000117 | 
| 100 | 0.000381 | 0.000378 |
| 1.000  | 0.003748 | 0.003697 | 
| 10.000 | 0.034260 | 0.029233  |
| 100.000  | 0.431911 | 0.431421 | 
| 1.000.000 | 7.092582 | 5.696597 |
| 10.000.000  | 85.916852 | 85.739131 | 
| 100.000.000 | 2200.680902 | 2126.456566 |

Tabel hasil *running time worst case scenario* dari algoritma* quick sort* secara iteratif dan rekursif 

|Data | Iteratif | Rekursif |
| ------------- | ------------- | ------------- |
| 10  | 0.000024 | 0.000025 | 
| 50 | 0.000114 | 0.000192 |
| 100 | 0.000640 | 0.000695 | 
| 250 | 0.003578 | 0.003724 |
| 500 | 0.025569 | 0.021572 | 
| 900 | 0.059421 | 0.053577 |

Kami juga menyediakan grafik perbandingan untuk tabel di atas, grafik dapat dilihat di bawah ini.

![image](https://github.com/user-attachments/assets/f63a6600-4377-457e-9314-96de7147d0c2)

Grafik *running time best case scenario* dari algoritma *quick sort* secara iteratif dan rekursif

![image](https://github.com/user-attachments/assets/ae1d7669-ce3e-4c83-9caa-10259158260d)

Grafik *running time worst case scenario* dari algoritma *quick sort* secara iteratif dan rekursif

### Kompleksitas Waktu
Algoritma quick sort secara rekursif dan iteratif memiliki kompleksitas waktu yang sama, yaitu $$O(n log n)$$ pada kasus terbaik dan rata-rata, serta $$O(n^2)$$ pada kasus terburuk. Namun, dari hasil analisis tabel yang diperoleh, kedua metode menunjukkan perbedaan waktu eksekusi pada berbagai skenario walaupun perbedaan tersebut tidak terlalu signifikan.

### Author
|No. | Nama | NIM |
| ------------- | ------------- | ------------- |
| 1 | M. Raditya Faturrahman | 1304221050 |
| 2 | Muhammad Yasin | 1304211078 |
