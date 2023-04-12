import sys
import os

def chong(infile: str, outfile: str):
    lines_seen = set()
    chong_count = 0
    outfile = open(outfile, 'w', encoding='utf-8')
    f = open(infile, 'r', encoding='utf-8')
    for line in f:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
        else:
            chong_count = chong_count + 1
    if chong_count != 0:
        print('err file =', infile)
    print(" chong_count = ", chong_count)



if __name__ == '__main__':
    infile = sys.argv[1]
       
    if os.path.isdir(infile):
        for file in os.listdir(infile):
            input_file = os.path.abspath(os.path.join(infile, file))
            output_file = os.path.abspath(os.path.join(infile, file))
            output_file = output_file + '.out'
            chong(input_file, output_file)
    else:
        output_file = infile + '.out'
        chong(infile, output_file)
    print("finish.")



