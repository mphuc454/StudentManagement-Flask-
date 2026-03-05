import numpy as np
my_arr = np.array([[5,3,1,8,9],
                   [-2,0,-2,11,3],
                   [0,9,-8,0,18]])
adults = my_arr[(my_arr > 4) & (my_arr < 10)]
checked = np.where(my_arr > 15, my_arr, 0)
print(checked)