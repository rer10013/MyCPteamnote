import math
import sys
input = sys.stdin.readline

def E(x):
  real = math.cos(2 * math.pi * x)
  imag = -math.sin(2 * math.pi * x)
  return complex(real, imag)

def FFT(y, invert):
  length = len(y)
  bLength = 1
  while 2 ** bLength < length:
    bLength += 1
  N = 2 ** bLength
  y.extend([0] * (N - length))


  order = []
  for i in range(1, N): # 여기 최적화
    order[i] = order[i >> 1] >> 1
    if i&1:
      order[i] = order[i]|(N>>1)
    if i < order[i]:
      y[i], y[order[i]] = y[order[i]], y[i]

  for i in range(1, bLength + 1):
    loop_size = 2 ** i
    for j in range(0, N, loop_size):
      for k in range(loop_size//2):
        val1 = y[j + k]
        val2 = E(k / loop_size * invert) * y[j + k + loop_size//2]
        y[j+k] = val1 + val2
        y[j+k+loop_size//2] = val1 - val2

  if (invert == -1):
    return list(map(lambda x : (x/length), y))
  else :
    return y