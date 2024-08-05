# Selection sort - Unstable

# Enter list of integers
a = [64, 25, 12, 22, 11]

print("a is : ",a)

for i in range(len(a)-1):
    lowest_ind = i
    print("---Pass: ",lowest_ind)

    for j in range(i+1, len(a)):
        if a[lowest_ind] <= a[j]:
            continue
        else:
            print("a[lowest_ind]: " + str(a[lowest_ind]) + " is greater than" + str(a[j]) + " so we updating the lowest value's index")
            lowest_ind = j
    a[i], a[lowest_ind] = a[lowest_ind], a[i]
    print("'a' after pass " + str(i) + " is : ",a)

print(a)
