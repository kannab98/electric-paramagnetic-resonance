import numpy as np
import scipy
# rc('text', usetex=True)
# rc('text.latex',preamble = \
# [
#     r'\usepackage[russian]{babel}',
#     r'\usepackage{amsmath}',
#     r'\usepackage{amssymb}',
# ])
# rc('font',family='serif')
def H(x):
    I = np.array([55, 135]) # мА
    H = np.array([1250,3000]) # Гс
    f = np.polyfit(I,H,deg=1)
    F = np.poly1d(f)
    return F(x)

# print(H(160))
# print(H(160)-H(164))

# dH = 10
# beta = 927*10**(-23)
# h = 1 * 10**(-27)
# g = 2
# domega = g * beta / h * dH 
# T2 =  2/domega 
# mu = 1
# T = 300
# omega0 = 9*10**9 * 2*np.pi
# k = 1.380 * 10**(-16)
# N = (3*k*T)/(8*np.pi*Q*mu**2*omega0*T2) * 200 * 2.3 / 84



