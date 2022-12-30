import powerlaw
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab

def powerlaw():
    with open(r'C:\zhgren\BrightKite\xydata\countlist.txt', 'r') as f:
        array = []
        for line in f:
            newline = line.rstrip().split('\t')
            array.append(newline)
    f.close()

    alphalist = []
    plist = []
    j = 0
    for inputlist in array:
        fit = powerlaw.Fit(inputlist)
        a = fit.power_law.alpha
        p = fit.power_law.sigma
        print(a)
        print(j)
        alphalist.append(a)
        plist.append(p)
        j += 1

    print('calculation finished')

    i = 0

    with open(r'C:\zhgren\BrightKite\xydata\Powerlaw.txt', 'w') as output:
        output.write('alpha' + '\t' + 'p\n')
        while (i < len(alphalist)):
            output.write(str(alphalist[i]) + '\t' + str(plist[i]) + '\n')
            i += 1

    output.close()
    print('file saved')
# fit = powerlaw.Fit(freqlist)
# a=fit.power_law.alpha
# xmin=fit.power_law.xmin
# sig=fit.power_law.sigma
# print('alpha= ',a,'  Xmin= ',xmin,'  sigma= ',sig)

# fit.distribution_compare('power_law', 'lognormal')
# fig1 = fit.plot_pdf(linewidth=3, color='blue', linestyle='solid',label='empirical pdf')
# fit.power_law.plot_pdf(linewidth=1, color='blue', linestyle='dashed', ax=fig1,label='powerlaw pdf')
# fit.plot_ccdf(linewidth=3, color='red', linestyle='solid', ax=fig1,label='empirical ccdf')
# fit.power_law.plot_ccdf(linewidth=1, color='red', linestyle='dashed', ax=fig1,label='powerlaw ccdf')
# plt.legend()
# plt.title('UK hashtags frequecy in June')
# plt.show()
#
# fig2 = fit.plot_ccdf(linewidth=3, color='blue', linestyle='solid',label='empirical ccdf',)
# fit.power_law.plot_ccdf(linewidth=1, color='red', linestyle='dashed', label='powerlaw ccdf',ax=fig2)
# fit.lognormal.plot_ccdf(linewidth=1, color='green', linestyle='dashed',label='lognormal ccdf',ax=fig2)
# plt.legend()
# plt.title('UK hashtags frequecy in June')
# plt.show()
if __name__ == '__main__':
    powerlaw()
