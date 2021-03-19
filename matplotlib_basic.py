import matplotlib.pyplot as plt
import numpy as np

x = range(6)
plt.plot(x, [i ** 2 for i in x])
plt.show()

# x = np.arange(0.0, 0.6, 0.01)
x = np.linspace(0.0, 0.6, 61)
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.show()  # more smooth

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y)
plt.plot(x, cos_y)
plt.show()

x = np.arange(1, 5)
plt.plot(x, x * 1.5, x, x * 3.0, x, x / 2.0)
plt.grid(True)
plt.axis()
plt.show()

x = np.arange(1, 5)
plt.plot(x, x * 1.5, x, x * 3.0, x, x / 2.0)
plt.grid(True)
plt.axis([0, 5, -1, 13])
plt.show()  # zoom out

x = np.arange(1, 5)
plt.plot(x, x * 1.5, x, x * 3.0, x, x / 2.0)
plt.grid(True)
plt.axis([2, 3, 6, 10])
plt.show()  # zoom in

plt.plot([1, 3, 2, 4])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("stock")
plt.show()

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend()
plt.title('Sirius signal')
plt.show()

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend(loc=(1, 0))
# plt.legend(loc=(0.5, 0.5))
plt.title('Sirius signal')
plt.show()

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, color='r', linewidth=3, label='sin', linestyle=":")
plt.plot(x, cos_y, color='b', linewidth=3, label='cos', linestyle='-')
plt.legend(loc=(1, 0))
# plt.legend(loc=(0.5, 0.5))
plt.title('Sirius signal')
plt.show()

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend()
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.yticks([-1, 0, 1])
plt.title('Sirius signal')
plt.show()

x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend()
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
plt.savefig('myplot.png')
plt.title('Sirius signal')
plt.show()

plt.subplot(2, 1, 1)  # 2 row, 1 column, 1st
plt.plot([1, 3, 2, 4])
plt.xlabel("this is x axis")
plt.ylabel("this is y axis")
plt.title('Sirius signal')

plt.subplot(2, 1, 2)  # 2 row, 1 column, 2nd
x = np.linspace(-np.pi, np.pi, 256)
sin_y = np.sin(x)
cos_y = np.cos(x)
plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend()
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
plt.show()

plt.subplot(2, 2, 1)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 1)', ha='center', va='center', size=20, alpha=.5)

plt.subplot(2, 2, 2)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 2)', ha='center', va='center', size=20, alpha=.5)

plt.subplot(2, 2, 3)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 3)', ha='center', va='center', size=20, alpha=.5)

plt.subplot(2, 2, 4)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2, 2, 4)', ha='center', va='center', size=20, alpha=.5)
plt.show()

# statistics diagram
# histogram
y = np.random.randn(1000)
plt.hist(y, 25)
plt.title("price of burgers")
plt.show()

x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.show()

plt.scatter(x, y, s=50 * abs(np.random.randn(1000)), c=np.random.randn(1000))
plt.show()

plt.bar([1, 2, 3], [4, 2, 6])
plt.show()

x = [20, 30, 50]
labels = ['cat', 'dog', 'sheep']
plt.pie(x, labels=labels)
plt.show()

x = np.arange(0, 4, 0.2)
y = np.exp(-x)
e = 0.1 * abs(np.random.randn(len(y)))
plt.errorbar(x, y, yerr=e, fmt='.-')  # uncertainty
plt.title('random')
plt.show()
