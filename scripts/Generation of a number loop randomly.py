import random
import time

start_time = time.time()
Inputted_Code = 34584

while True:
    Correct_Code = random.randint(1, 99999)
    formatted_code = str(Correct_Code).zfill(5)
    print(formatted_code)
    if Correct_Code == Inputted_Code:
        print(f"The correct code is {Correct_Code}")
        break

print(f"Time taken: {time.time() - start_time:.2f}")
