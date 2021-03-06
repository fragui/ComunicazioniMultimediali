import os
import stat

def filesize(file):
    info = os.stat(file)
    sz = info[stat.ST_SIZE]
    return sz

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2f TB' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2f GB' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2f MB' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2f KB' % kilobytes
    else:
        #size = '%.2f B' % bytes
        return ""
    return "(" + size + ")"

def dim(file):

    print "\t" + str(filesize(file)) + " B\t" + convert_bytes(filesize(file))

def check(file1,file2):

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    t1 = f1.read()
    t2 = f2.read()
    if t1 == t2:
        print '\033[92m' + "(Decodifica corretta)" + '\033[0m'
    else:
        print '\033[91m' + "(Decodifica non corretta)" + '\033[0m'

def perc_comp(f_orig,f_comp):

    ratio = (filesize(f_orig) - filesize(f_comp) + 0.0) / filesize(f_orig)

    perc = ratio * 100

    print '\t%.2f' % perc + ' %'