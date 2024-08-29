'''Number Theoretic Transform(float FFT)'''

P = 998244353
w = 3

def NTT(y, invert=1):
  length = len(y)
  bLength = 1
  while 2 ** bLength < length:
    bLength += 1

  N = 2 ** bLength
  y.extend([0] * (N - length))

  order = [0] * N
  for i in range(1, N): # 여기 최적화
    order[i] = order[i >> 1] >> 1
    if i&1:
      order[i] = order[i]|(N>>1)
    if i < order[i]:
      y[i], y[order[i]] = y[order[i]], y[i]

  x = pow(w, (P-1)//N, P)
  if invert == -1:
    x = pow(x, P-2, P)

  root = [1]
  for i in range(1, 2 ** bLength):
    root.append(root[i-1]*x%P)

  for i in range(1, bLength + 1):
    loop_size = 2 ** i
    step = N // loop_size
    for j in range(0, N, loop_size):
      for k in range(loop_size//2):
        val1 = y[j + k]
        val2 = root[step * k] * y[j + k + loop_size//2] % P
        y[j+k] = (val1 + val2) % P
        y[j+k+loop_size//2] = (val1 - val2) % P
        if y[j+k+loop_size//2] < 0:
          y[j+k+loop_size//2] += P

  if (invert == -1):
    t = pow(N, P-2, P)
    return list(map(lambda x : x*t%P, y))
  else :
    return y