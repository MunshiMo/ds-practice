import demo_array

test_arr = demo_array.Array()

test_arr.append(55)

print(test_arr.get(0))

arr = demo_array.Array()
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.delete(1)
print(arr)  # should print Array([10, 30, 40])