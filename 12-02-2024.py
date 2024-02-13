#break

for counter in range(10):
    if counter == 6:

        break
print(counter)
print("outside loop")



#continue

for counter in range(10):
    if counter == 6:

        continue
print(counter)
print("outside loop")

#pass

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
#break
for i in range(10):
    if i == 5:
        break
    else:
        print(i)

