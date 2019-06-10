import pylab
import scipy
x = scipy.linspace(-2,2,1500)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='green')
pylab.fill_between(x, y2, color='green')
pylab.xlim([-2.5, 2.5])
pylab.text(0, -0.4, 'We love Levi', fontsize=30, fontweight='bold',
           color='black', horizontalalignment='center')


pylab.text(-1.5, -4, '\n'.join([''.join([('Levi'[(x-y) % len('Levi')] if ((x*0.05)**2+(y*0.12)**2-1)**3-(x*0.05)**2*(y*0.12)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))

pylab.show()

# print('\n'.join([''.join([('Levi'[(x-y) % len('Levi')] if ((x*0.05)**2+(y*0.12)**2-1)**3-(x*0.05)**2*(y*0.12)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))