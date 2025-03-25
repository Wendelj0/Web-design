
books = []
fav_book = ""

while fav_book.lower() != "done":
    fav_book = input("whats your fav book: ")
    books.append(fav_book)
books.remove("done")
    
for book in books:
    print(f"* {books}")


print("\nThese are your favorite books")
for i, book in enumerate(books):
    print(f" {i + 1}. {books[i]}")