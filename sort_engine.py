
#Algorithmes de Tri
#Contient plusieurs méthodes de tri pour les livres.

# Tri à bulles
def bubble_sort(books, key):
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j][key] > books[j+1][key]:
                books[j], books[j+1] = books[j+1], books[j]
    return books

# Tri par insertion
def insertion_sort(books, key):
    for i in range(1, len(books)):
        current = books[i]
        j = i - 1
        while j >= 0 and books[j][key] > current[key]:
            books[j+1] = books[j]
            j -= 1
        books[j+1] = current
    return books
