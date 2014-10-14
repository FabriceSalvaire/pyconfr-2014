####################################################################################################

import matplotlib.pyplot as plt

import numpy as np

####################################################################################################

from FigureSize import configure
figure_size = configure(document_fontsize=11, available_width=307.28987)
print 'figure size:', figure_size()

####################################################################################################

mesa_completion = np.array([[4.0, 22, 25],
                            [4.1, 4, 6],
                            [4.2, 10, 11],
                            [4.3, 13, 22],
                            [4.4, 6, 9],
                            [4.5, 2, 12],
                            # ES
                            [3.1, 8, 24],
                        ]).T

labels = [str(x) for x in mesa_completion[0]]
labels[-1] = 'ES ' + labels[-1]
index = np.arange(mesa_completion.shape[1])

####################################################################################################

dpi = 100
width = 1600 / dpi
height = 900 / dpi

# figure, axe = plt.subplots()
figure = plt.figure(figsize=(width,height), dpi=dpi)
# figure = plt.figure(figsize=figure_size())
axe = figure.add_subplot(111)

y_max = max(mesa_completion[2]) +1
plt.ylim(0, y_max)

bar_width = .8
axe.bar(index, mesa_completion[2], bar_width, color='red')
axe.bar(index, mesa_completion[1], bar_width, color='green')

axe.plot(index + bar_width/2,
         mesa_completion[1]/mesa_completion[2]*y_max,
         'o', color='blue')

# axe.xlabel('')
# axe.ylabel('')
# axe.title('')

plt.xticks(index + bar_width/2, labels)

axe_percent = axe.twinx()
axe_percent.set_ylim(0, 100)

figure.tight_layout(pad=0.1)

# plt.show()
figure.savefig(__file__.replace('.py', '.pdf'))

####################################################################################################
# 
# End
# 
####################################################################################################
