# -*- coding:utf-8 -*-
import codecs
import os
import string

'''
NEWSSTEP = 2000


def unicode_read(stream, length):
    str = stream.read(length)
    if str == '':
        return ''
    while 1:
        try:
            str.decode('unicode_escape')
        except UnicodeDecodeError:
            str += stream.read(1)
        else:
            break
    return str.decode('unicode_escape')

std_input = codecs.open('test.json', 'r', 'utf-8')############ train / test
#std_output = codecs.open('out_test','a','utf-8')
def new_transform(outstream):
    while 1:
        sstr = unicode_read(std_input, NEWSSTEP)
        if sstr == '':
            break
        outstream.write(sstr)
    return

#new_transform(std_output)
#std_output.close()
std_input.close()
'''

#temp_input = codecs.open('out_test','r','utf-8')
#temp_output = codecs.open('out_test2.txt','w','utf-8')
#temp_output.write(temp_input.read(50000))




Read_Once = 10000

def stdlize():
    txt_in = codecs.open('out.txt', 'r', 'utf-8')
    sstr = txt_in.read(Read_Once)
    processed = 0
    while 1:
       # if (sstr == ''):
        #    return
        tit = sstr.find('\"title\"')
        if(tit == -1):
            nr = txt_in.read(Read_Once)
            if nr == '':
                break
            sstr += nr
            continue
        end = sstr.find('}', tit)
        if end == -1 :
            newread = txt_in.read(Read_Once)
            if newread == '':
                break
            else:
                sstr += newread
            continue
        #print 'SSTR: ' + sstr + '\n'
        substr = sstr[0:end + 1]
        substr = substr.replace('<p>','')
        substr = substr.replace('</p>','')
        substr = substr.replace('<strong>','')
        substr = substr.replace('</strong>','')
        substr = substr.strip()
        while 1:
            pic = substr.find('<img src=')
            if pic != -1:
                pic_end = substr.find('>',pic)
                if pic_end != -1:
                    substr = substr[:pic] +u'图片图片图片图片图片'+substr[pic_end + 1:]
                else:
                    break
            else:
                break
        '''
        while 1:
            stg = substr.find('<strong>')
            if stg != -1:
                stg_end = substr.find('</strong>')
                if stg_end != -1:
                    print substr
                    print substr[stg]
                    print substr[stg_end]
                    print substr[:stg]
                    print substr[stg + 8:stg_end]
                    print substr[stg_end + 9:]
                    substr = substr[:stg] + substr[stg + 8:stg_end] + substr[stg + 8:stg_end] + substr[stg + 8:stg_end] +substr[stg_end + 9:]
                else:
                    break
            else:
                break
        '''
        # print substr
        if end != len(sstr) - 1:
            sstr = sstr[end + 2:len(sstr)-1]
        else:
            sstr += txt_in.read(Read_Once)
        #print substr
        start = substr.find('content') + 11
        title_start = substr.find('\"title\"')
        end = title_start - 4

        content = substr[start:end + 1]
        #print 'c: %d\t%d'%(start, end)
        start = title_start + 10
        id_start = substr.find('\"id\"')
        end = id_start - 4

        title = substr[start:end + 1]
        #print 't: %d\t%d'%(start, end)
        label_start = substr.find('\"label\"')
        id_start += 7
        id_end = label_start - 4

        ID = substr[id_start:id_end + 1]
        #print 'I: %d\t%d'%(id_start, id_end)
        #print 'SUBSTR: ' + substr + '\n'
        #print 'content: ' + content + '\n'
        if ID.find('\\u') > 0:
            pass
        try:
            label = substr[label_start + 10]
        except:
            continue
        #print label
        if label == '1':
            try:
                output = codecs.open('/Users/lijinning/Desktop/MLstddata/1/'+ID+'.txt', 'w', 'utf-8')
            except:
               # print 'SSTR: ' + sstr + '\n'
               # print 'SUBSTR: ' + substr + '\n'
               # print 'ID: ' + ID + '\n'
                continue
        elif label == '0':
            try:
                output = codecs.open('/Users/lijinning/Desktop/MLstddata/0/'+ID+'.txt', 'w', 'utf-8')
            except:
               # print 'SSTR2: ' + sstr + '\n'
               # print 'SUBSTR2: ' + substr + '\n'
               # print 'ID2: ' + ID + '\n'
                continue
        else:
            continue
        for i in range(0, 5):
            output.write(title)
        output.write(content)
        output.close()
        processed += 1
        print 'Number. '+str(processed)+'\t\tTitle:'+ title +'\t\tID:'+ID
    txt_in.close()


def stdlize_test():
    txt_in = codecs.open('out_test', 'r', 'utf-8')
    sstr = txt_in.read(Read_Once)
    processed = 0
    while 1:
       # if (sstr == ''):
        #    return
        tit = sstr.find('\"title\"')
        if(tit == -1):
            nr = txt_in.read(Read_Once)
            if nr == '':
                break
            sstr += nr
            continue
        end = sstr.find('}', tit)
        if end == -1 :
            newread = txt_in.read(Read_Once)
            if newread == '':
                break
            else:
                sstr += newread
            continue
        substr = sstr[0:end + 1]    # -----------edited
        #print sstr + '\n'
        if end != len(sstr):
            sstr = sstr[end + 2:]
        else:
            sstr += txt_in.read(Read_Once)
        #print substr
        start = substr.find('content') + 14
        id_start = substr.find('\"id\"')
        end = id_start - 4

        content = substr[start:end + 1]

        start = id_start + 7
        title_start = substr.find('\"title\"')
        end = title_start - 4

        ID = substr[start:end + 1]

        title = substr[title_start + 10:len(substr)-2]
       # try:
        output = codecs.open('/Users/lijinning/Desktop/MLtestdata/' + ID + '.txt', 'a', 'utf-8')
       # except:
        #    print sstr +'\n\n'
        #    print substr
        for i in range(0, 5):
            output.write(title)
        output.write(content)
        output.close()
        processed += 1
        print 'Number. '+str(processed)+'\t\tTitle:'+ title +'\t\tID:'+ID
    txt_in.close()


def stdlize_ans():
    anstxt_out = codecs.open('/Users/lijinning/Desktop/Submission.csv','w','utf-8')
    anstxt_out.write('id,pred\n')
    anstxt_in = codecs.open('/Users/lijinning/Desktop/report.txt','r','utf-8')
    while 1:
        sstr = anstxt_in.readline()
        if sstr == '':
            break
        txtpos = sstr.find('.txt')
        if txtpos != -1:
            ID = sstr[txtpos - 24 : txtpos]
            if sstr[txtpos + 8] == '1':
                sstr = sstr[txtpos + 9:]
                sstr.strip()
                anstxt_out.write(ID + ',')
                b = '%.20f'%float(sstr)
                anstxt_out.write(str(b)+'\n')
                continue
            sstr = anstxt_in.readline()
            onepos = sstr.find('1')
            sstr = sstr[onepos + 2:]
            sstr.strip()
            anstxt_out.write(ID+',')
            b = '%.20f'%float(sstr)
            anstxt_out.write(str(b)+'\n')
           # anstxt_out.write(str(float(sstr)))
    anstxt_out.close()
    anstxt_in.close()
#stdlize_ans()
#txt_out = codecs.open('temp.txt','w','utf-8')
#chips = txt_in.read(3000)
#txt_out.write(chips)

def main():
    '''
    print '\n**************************Initially Standardlize Processing**************************\n'
    os.system('rm -r /Users/lijinning/Desktop/MLstddata')
    os.system('mkdir /Users/lijinning/Desktop/MLstddata')
    os.system('mkdir /Users/lijinning/Desktop/MLstddata/0')
    os.system('mkdir /Users/lijinning/Desktop/MLstddata/1')
    stdlize()
    print '\n**************************Initially Standardlize Success**************************\n'

    print '\n**************************Test Data Standardlize Processing**************************\n'
    os.system('rm -r /Users/lijinning/Desktop/MLtestdata')
    os.system('mkdir /Users/lijinning/Desktop/MLtestdata')
    stdlize_test()
    print '\n**************************Test Data Standardlize Success**************************\n'
    '''
    #
    # print '\n**************************Java Modeling Processing**************************\n'

    print '\n**************************Training**************************\n'
    os.system('rm -r /Users/lijinning/Desktop/Model')
    os.system('mkdir /Users/lijinning/Desktop/Model')
    os.system('java -jar -Xms16g -Xmx16g /Users/lijinning/Desktop/Classification.jar')
    print '\n**************************Training Finished**************************\n'


    # print '\n**************************Java Classifying**************************\n'
    # os.system('rm /Users/lijinning/Desktop/report.txt')
    # os.system('java -jar /Users/lijinning/Desktop/THUCTC_java_v1_run.jar -l /Users/lijinning/Desktop/Model -classify /Users/lijinning/Desktop/MLtestdata -n 2 > /Users/lijinning/Desktop/report.txt')
    # print '\n**************************Java Classifying Finished**************************\n'
    # print '\n**************************Java Modeling Process Success**************************\n'


    print '\n**************************Submission Standardlize Processing**************************\n'
    stdlize_ans()
    print '\n**************************Submission Standardlize Success**************************\n'


    print '\n**************************All Process Success**************************\n'
main()