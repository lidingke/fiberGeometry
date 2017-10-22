from time import sleep

import pynir
import pdb

assert "get_darrat" in dir(pynir)

data = pynir.get_darrat()
# data = data.reshape((2,3))
print(data)
#
data = pynir.get_spectrum(500000)
# sleep(1)
# print "1"
len_data = len(data)
# # data = data.reshape((2,len_data//2))
pdb.set_trace()
datal = data.tolist()
# print data.shape
# print data[:10][0]
# #
# # print datal
# print data[:10][1]
w ,l =datal
print(w)
print(l)