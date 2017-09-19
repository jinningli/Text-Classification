import codecs

NEWSSTEP = 2000


def unicode_read(stream, length):
    str = stream.read(length)
    if str == '':
        return ''
    while 1:
        try:
            str.encode('utf-8')
        except UnicodeEncodeError:
            str += stream.read(1)
        else:
            break
    return str

std_input = codecs.open('/Users/lijinning/Downloads/SogouR.reduced.txt', 'r', 'gbk')############ train / test
std_output = codecs.open('/Users/lijinning/Desktop/SougouStd.txt','a','utf-8')

def new_transform(outstream):
    while 1:
        sstr = unicode_read(std_input, NEWSSTEP)
        if sstr == '':
            break
        outstream.write(sstr)
    return

new_transform(std_output)
std_output.close()
std_input.close()