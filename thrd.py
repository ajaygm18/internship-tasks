import threading
import requests
import string
import random

def download(url: str):
    f = requests.get(url)._content
    with open(''.join(random.choices(string.ascii_letters, k=5))+'.jpeg', 'wb') as file:
        file.write(f)



urls = [
    'https://www.royalchallengers.com/PRRCB01/public/styles/1374_771_landscape/public/2026-02/AJ021844.jpg?itok=EwAhDkUa',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe4csvA0ilNoXAvO6x-PI9no41NwCkMnmorQ&s',
    'https://media.zigcdn.com/media/model/2025/Nov/bmw-m511.jpg',
    'https://prod.cosy.bmw.cloud/bmwweb/cosySec?COSY-EU-100-73315jAvmZ7dgMyDkRUQunKeNWJeihsPIgpnXJCpLMXTCBb419kVObHi4T4qY9%25wc3cLKiftxdxbqw178z8R8tECUkdEo7slGAzjJCrXpFkszlZQ6KAnkXRaYWFObQ5nmP%25eIagOybfgmnvIT91vlO2B3iEHqIjedwsniBDMztrOReqhk7ZFaMLoACewShJHFlMILou%25KXhu7HSfWQoOU%25V1PaHqffNEbn%258a10s9OfqtE4riI1l3scZwBE4irxRteajcZ857Mn68RUgChOYW5GvloImQgp2XHBRbv6jQ%25JE82YDafu3Rjmqn1Sd9DyLOEVzwqTJIsN76L3uBr0NMJdSeZ4btuzVMRcp9SkNh5x6MVA0og9ZTNF4HviDd0Kc%252wn44Wxfjtq%25cP81D86SxbUEqUuV89GsLGeHUiprJpXBGw6Zu6VnptYRSYN167m5VmtoYCygNXpgmlTv0QCUyX324alzTQLDrg2jCil6JTYYXbH8IAeb6qVhFUwlkIVrgyfYgMEG1xcPrweIdLBy2okj2uzHuxXgEsUrOUqQliGwgYXcjnWqVskbNDOBeagd56reMnTNIu8dtE6MJeiKMZcN889RGlLbuUrOQhqzVAfvXYuImptvwkyT365ecr93KgDaBVKL3hqsVL2JeiHZ',
    r'https://bmw.scene7.com/is/image/BMW/The%20New%202GC_16x7?qlt=80&wid=1024&fmt=webp'

]

threads = [threading.Thread(target=download, args=(urls[i],)) for i in range(5)]

for th in threads:
    th.start()

for th in threads:
    th.join()

