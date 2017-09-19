import jieba
import codecs
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

jieba.enable_parallel(32)

def process(indir, outdir):
    instream = codecs.open(indir, "r", "utf-8")
    outstream = codecs.open(outdir, "w", "utf-8")
    inistr = instream.read(100000)
    #print inistr
    iniseg = jieba.cut(inistr)
    for s in iniseg:
        if s == "\n" or s == " ":
            continue
        outstream.write(s + "\n")

os.system('rm -r /Users/lijinning/Desktop/MLJIEBAtestdata')
os.system('mkdir /Users/lijinning/Desktop/MLJIEBAtestdata')


cnt = 0

for root,dirs,files in os.walk("/Users/lijinning/Desktop/MLtestdata"):
    for file in files:
        if file.__str__() == '.DS_Store':
            continue
        inpath = root + "/" +file
        outpath = "/Users/lijinning/Desktop/MLJIEBAtestdata/" + file
        process(inpath, outpath)
        cnt += 1
        if cnt % 100 == 0:
            print cnt
#
# for root, dirs, files in os.walk("/Users/lijinning/Desktop/MLstddata/0"):
#     for file in files:
#         if file.__str__() == '.DS_Store':
#             continue
#         inpath = root + "/" + file
#         outpath = "/Users/lijinning/Desktop/MLJIEBAstddata/0/" + file
#         process(inpath, outpath)
#         cnt += 1
#         if cnt % 100 == 0:
#             print cnt