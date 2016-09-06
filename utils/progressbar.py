#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw
import sys

def printProgress (iteration, total, prefix = '[', suffix = ']', decimals = 2, barLength = 10):
    """
    prints terminal progress bar
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '=' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r')
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
