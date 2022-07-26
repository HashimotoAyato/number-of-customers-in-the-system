import math

# from 22WM0205
lam = 205

h = 1500 * 8 / 5000000
rho = lam * h
K = 200

# calc b_k
b = []
frac = 1
for k in range(K):
    if 0 < k:
        frac *= rho/k
    b.append(frac*math.exp(-rho))

# calc pi_k
pi = [1]
for k in range(1, K+1):
    sigma = 0
    for j in range(1,k):
        sigma += pi[j]*b[k-j]
    pi.append((pi[k-1]-pi[0]*b[k-1]-sigma)/b[0])

total = sum(pi)
for k in range(K+1):
    pi[k] /= total

# calc p_k
p = []
for k in range(K+1):
    p.append(pi[k]/(pi[0]+rho))

# calc average
print(sum(p)/len(p))