// this program finds sum of multiples of 3 in array
values = [1, 3, "5", 7, 8, 9]
multiples_of_three = []
total_of_threes = 0
// find 3s
while not (i > values.length):
    if (values[i] modulo 3) == 0:
    multiples_of_three[i] =values[i]

//do sum
while True:
    if not multiples_of_three.empty():
        total_of_threes = total_of_threes + multiples_of_three.first_item
        multiples_of_three.remove_first_item
    else if multiples_of_three.empty():
        break;
print(total_of_threes)

