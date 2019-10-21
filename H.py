import numpy as np
import scipy
<<<<<<< Updated upstream
# import matplotlib.pyplot as plt
# from matplotlib import rc
=======
import matplotlib.pyplot as plt
from matplotlib import rc
>>>>>>> Stashed changes
# rc('text', usetex=True)
# rc('text.latex',preamble = \
# [
#     r'\usepackage[russian]{babel}',
#     r'\usepackage{amsmath}',
#     r'\usepackage{amssymb}',
# ])
# rc('font',family='serif')
<<<<<<< Updated upstream
def H(x):
    I = np.array([55, 135]) # мА
    H = np.array([1250,3000]) # Гс
    f = np.polyfit(I,H,deg=1)
    F = np.poly1d(f)
    return F(x)

print(H(160))
print(H(160)-H(164))
=======
# def H(x):
#     I = np.array([55, 135]) # мА
#     H = np.array([1250,3000]) # Гс
#     f = np.polyfit(I,H,deg=1)
#     F = np.poly1d(f)
#     return F(x)


>>>>>>> Stashed changes
# I = np.array([55, 135])
# plt.plot(I,H(I),color='darkblue')
# fontsize = 12
# plt.ylabel(r'$I, \text{ мА}$',fontsize = fontsize)
# plt.xlabel(r'$H, \text{ Гс}$',fontsize = fontsize)
# plt.grid(which='major',linestyle = '-')
# plt.grid(which='minor',linestyle = ':')
# plt.minorticks_on()
# plt.savefig('fig/fig1.pdf')
# plt.show()
<<<<<<< Updated upstream
=======
dH = 10
beta = 927*10**(-23)
h = 1 * 10**(-27)
g = 2
domega = g * beta / h * dH / 10**9
print(domega)
>>>>>>> Stashed changes
