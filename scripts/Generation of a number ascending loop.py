import time

start_time = time.time()
correct_number = 3458400
number = 1

if number != correct_number:
    while number != correct_number:
        number += 1
        formatted_number = str(number).zfill(5)
        print(formatted_number)
    if number == correct_number:
        print('correct number is', number)

print(f'Time taken: {time.time() - start_time:.2f} seconds')