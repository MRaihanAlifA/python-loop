book_count = 10

print('Mom tell me to read all the books')

book_read_and_understand_count = 0

attempt_read = 0

"""
for book_read_count in range (1 , book_count+1):
    print(f'{book_read_count} book is being read')
    book_read_count += 1
"""
while book_read_and_understand_count < book_count:
    attempt_read += 1
    print(attempt_read)
    if book_read_and_understand_count == 9:
        print(f'i cant understand the {book_read_and_understand_count} book')
    else:
        book_read_and_understand_count += 1
        print(f'{book_read_and_understand_count} book is being read and understand')
        attempt_read = 0
    if attempt_read == 3:
        book_read_and_understand_count += 1
        print(f'{book_read_and_understand_count} book is being read and understand')


print(' ')
print(f'{book_read_and_understand_count}')
