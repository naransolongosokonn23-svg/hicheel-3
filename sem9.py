# import numpy as np
# array=np.array([1, 2, 3, 4, 5])
# print("array:", array)

# import numpy as np
# array=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print("array:", array)

# import numpy as np
# array=np.array([[[1, 2, 3], [6, 7, 8]], [[11, 12, 13], [16, 17, 18]]])
# print(array)

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# print(np.sort(arr))

# import numpy as np
# arr=np.array(["blue", "green", "red"])
# print(np.sort(arr)) 

# import numpy as np
# arr=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np.sort(arr))

# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# print("massiv", arr)
# print("dundaj:", np.mean(arr))
# print("niilber:", np.sum(arr))
# print("hamgiin ih too:", np.max(arr))
# print("hamgiin baga too:", np.min(arr))

# import numpy as np
# a = np.arange(1, 13)
# b = np.reshape(a, (3, 4))
# print("anhnii array:", a)
# print("3x4 array:")
# print(b)

# import numpy as np
# a = np.arange(1, 15)
# print("anhnii array:", a)
# b = a[a>5]
# print("b:", b)

# import numpy as np
# a = np.array([[1, 2, 3], 
#               [4, 5, 6],
#               [7, 8, 9]])
# print("matrix:", a)
# print("mor tus buriin niilber:", np.sum(a, axis=1))
# print("bagana tus buriin dundaj:", np.mean(a, axis=0))

# import numpy as np
# a = np.array([[1, 2, 3], 
#               [4, 5, 6],
#               [7, 8, 9]])
# print("massiv", a)
# print("dundaj:", np.mean(a))
# print("niilber:", np.sum(a))
# print("hamgiin ih too:", np.max(a))
# print("hamgiin baga too:", np.min(a))

# import numpy as np
# arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.mean(arr, axis=1))
# print(np.sum(arr))
# print(np.max(arr))
# print(np.min(arr))

import numpy as np
arr = np.arange(1, 21)
print(arr[arr % 2 != 0])
print(np.sum(arr))
print(np.mean(arr))

# import numpy as np
# arr=np.random.randint(1,11,10)
# print(arr)
# print(arr[arr>5])
# arr[arr>5] = 0
# print(arr)

# import numpy as np
# a = np.array(["apple", "banana", "kiwi"])
# print(len(a))
# print(min(a, key=len))
# print(max(a, key=len))
# print("".join(a))

# import numpy as np
# a = np.array([12, 7, 25, 18, 30, 9, 14, 21])
# print("Тэгш:", a[a % 2 == 0])
# print("Сондгой:", a[a % 2 != 0])
# print("Тэгш нийлбэр:", sum(a[a % 2 == 0]))
# print("Сондгой нийлбэр:", sum(a[a % 2 != 0]))

# import numpy as np
# a = np.array([65, 78, 90, 55, 88, 72, 95, 60, 83, 47])
# print("Дундаж:", np.mean(a))
# print("Их:", np.max(a))
# print("Бага:", np.min(a))
# print("70-аас дээш:", sum(a > 70))
# print("60-аас бага:", sum(a < 60))
# print("Эрэмбэ:", np.sort(a))

# import numpy as np
# A = np.array([[12,15,18],
#               [20,25,30],
#               [10,14,16]])
# print("Мөрийн нийлбэр:", np.sum(A, axis=1))
# print("Баганын дундаж:", np.mean(A, axis=0))
# print("Хамгийн их:", np.max(A))
# print("Нийт нийлбэр:", np.sum(A))


# import numpy as np
# a = np.array([250,320,180,400,350,500,280])
# print("Нийт:", np.sum(a))
# print("Дундаж:", np.mean(a))
# print("Хамгийн их:", np.max(a))
# print("Их борлуулалттай өдөр:", np.argmax(a)+1)
# print("300-аас дээш:", sum(a > 300))
# print("10% нэмэгдсэн:", a * 1.1)