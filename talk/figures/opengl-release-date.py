####################################################################################################

from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DayLocator, HourLocator, DateFormatter, drange
import matplotlib.dates as mdates

import numpy as np

####################################################################################################

from FigureSize import configure
figure_size = configure(document_fontsize=20, available_width=307.28987)
print 'figure size:', figure_size()

####################################################################################################

def get_x(dates):
    return [x[1] for x in dates]

def get_y(dates):
    return [x[0] for x in dates]

####################################################################################################

opengl_releases = (
    (1.0, datetime(1992, 1, 1), None), # day ?
    (1.1, datetime(1997, 3, 4), None),
    (1.2, datetime(1998, 3, 16), None),
    (1.3, datetime(2001, 8, 14), None),
    (1.4, datetime(2002, 7, 24), 'GLSL'),
    (1.5, datetime(2003, 7, 29), None),
    (2.0, datetime(2004, 9, 7), 'GLSL\nin core'),
    (2.1, datetime(2006, 7, 2), None),
    (3.0, datetime(2008, 8, 11), 'Programmable\npipeline'),
    (3.1, datetime(2009, 3, 24), None),
    (3.2, datetime(2009, 8, 3), None),
    (3.3, datetime(2010, 3, 11), None),
    (4.0, datetime(2010, 3, 11), None),
    (4.1, datetime(2010, 7, 26), None),
    (4.2, datetime(2011, 8, 6), None),
    (4.3, datetime(2012, 8, 6), None), # 'full compatibility\nwith\nES 3.0'
    (4.4, datetime(2013, 7, 22), None),
    (4.5, datetime(2014, 8, 11), None),
)

opengl_es_releases = (
    (1.0, datetime(2003, 7, 28), None),
    # 1.1
    (2.0, datetime(2007, 3, 1), None), # day ?
    (3.0, datetime(2012, 8, 1), 'implemented by\n4.3'), # day ?
    (3.1, datetime(2014, 3, 1), None), # day ?
)

mesa_releases = (
    (3.0, datetime(2012, 2, 9), 8.0),
    (3.1, datetime(2012, 10, 8), 9.0),
    (3.3, datetime(2013, 11, 30), 10.0),
    # Mesa 10.3 September 19, 2014 
)

i965_dates = (
    (4.1, datetime(2012, 1, 1), 'Ivy Bridge\nHD 2500/4000', (-5, 60)),
    (4.3, datetime(2013, 1, 1), 'Haswell', (0, 70)),
)

key_dates = (
    ('Phigs', datetime(1990, 1, 1), (0, 80)),
    ('Microsoft\nDirect3D', datetime(1995, 1, 1), (0, 50)),
    ('First GPU\nNvidia\nGeForce 256', datetime(1999, 10, 11), (0, 80)),
    ('Khronos', datetime(2006, 7, 1), (-15, 25)),
    ('Nvidia\nTesla', datetime(2006, 12, 31), (0, 50)),
)

####################################################################################################

dpi = 100
width = 1600 / dpi
height = 900 / dpi

# figure, axe = plt.subplots()
figure = plt.figure(figsize=(width,height), dpi=dpi)
# figure = plt.figure(figsize=figure_size())
axe = figure.add_subplot(111)

axe.hlines(y=1,
           xmin=mdates.date2num(datetime(1990, 1, 1)),
           xmax=mdates.date2num(datetime(1992, 1, 1)),
           linewidth=4, color='black')
axe.text(mdates.date2num(datetime(1991, 1, 1)), 1.3,
         'IRIS GL',
         horizontalalignment='center', color='black')

axe.hlines(y=1,
           xmin=mdates.date2num(datetime(2012, 1, 1)),
           xmax=mdates.date2num(datetime(2015, 1, 1)),
           linewidth=4, color='black')
axe.text(mdates.date2num(datetime(2013, 6, 1)), 1.1,
         'Hardware\nlifetime',
         horizontalalignment='center', color='black')

axe.plot_date(get_x(opengl_releases), get_y(opengl_releases), 'o-', color='green')
axe.plot_date(get_x(opengl_es_releases), get_y(opengl_es_releases), 'o-', color='blue')

axe.text(mdates.date2num(datetime(1995, 1, 1)), 2, 'OpenGL (Desktop)', horizontalalignment='center', color='green')
axe.text(mdates.date2num(datetime(2012, 1, 1)), 2, 'OpenGL ES (Mobile)', horizontalalignment='center', color='blue')

for api, date, text in opengl_releases:
    axe.text(mdates.date2num(date), api +.1, str(api), horizontalalignment='center', color='green')
    if text is not None:
        axe.annotate(text,
                     xy=(mdates.date2num(date), api +.2),
                     xytext=(0, 50), 
                     textcoords='offset points',
                     horizontalalignment='center',
                     arrowprops=dict(facecolor='black', arrowstyle='-|>'))

for api, date, text in opengl_es_releases:
    axe.text(mdates.date2num(date), api -.2,
             str(api),
             horizontalalignment='center', color='blue')
    if text is not None:
        axe.annotate(text,
                     xy=(mdates.date2num(date), api -.2),
                     xytext=(0, -70), 
                     textcoords='offset points',
                     horizontalalignment='center',
                     arrowprops=dict(facecolor='black', arrowstyle='-|>'))

for api, date, release in mesa_releases:
    i = get_y(opengl_releases).index(api)
    gl_date = get_x(opengl_releases)[i]
    axe.hlines(y=api, xmin=mdates.date2num(gl_date), xmax=mdates.date2num(date), linewidth=2, color='red')
    # axe.text(mdates.date2num(date), api,
    #          'Mesa {}'.format(release),
    #          horizontalalignment='center', color='black')
    axe.annotate('Mesa {}'.format(release),
                 xy=(mdates.date2num(date), api),
                 xytext=(0, 60), 
                 textcoords='offset points',
                 horizontalalignment='center',
                 arrowprops=dict(facecolor='black', arrowstyle='-|>'))

for api, date, text, offset in i965_dates:
    i = get_y(opengl_releases).index(api)
    gl_date = get_x(opengl_releases)[i]
    axe.hlines(y=api, xmin=mdates.date2num(gl_date), xmax=mdates.date2num(date), linewidth=2, color='red')
    axe.annotate(text,
                 xy=(mdates.date2num(date), api),
                 xytext=offset, 
                 textcoords='offset points',
                 horizontalalignment='center',
                 arrowprops=dict(facecolor='black', arrowstyle='-|>'))

for text, date, offset in key_dates:
    axe.annotate(text,
                 xy=(mdates.date2num(date), 1),
                 xytext=offset, 
                 textcoords='offset points',
                 horizontalalignment='center',
                 arrowprops=dict(facecolor='black', arrowstyle='-|>'))

axe.set_xlim(datetime(1989, 6, 1), datetime(2014, 12, 31))
axe.set_ylim(.7, 5)
axe.xaxis.set_major_locator(YearLocator())
# axe.xaxis.set_major_locator(MonthLocator())
axe.xaxis.set_major_formatter(DateFormatter('%Y'))
# axe.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
axe.get_yaxis().set_visible(False)
axe.grid()

figure.autofmt_xdate()
figure.tight_layout(pad=0.1)

# plt.show()
figure.savefig(__file__.replace('.py', '.pdf'))

####################################################################################################
# 
# End
# 
####################################################################################################
