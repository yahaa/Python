# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(t)$",color="red",linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

# x = []
# z = []
# for i in boys:
#     x.append(i[0])
# for i in grils:
#     z.append(i[0])
# yb = stats.norm.pdf(x, bx, bq)
# yg = stats.norm.pdf(z, gx, gq)
# plt.plot(x, yb, 'v', color='red')
# plt.plot(z, yg, '^', color='green')
# plt.show()