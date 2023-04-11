import sys

def chong(infile: str, outfile: str):
    lines_seen = set()
    chong_count = 0
    outfile = open(outfile, 'w', encoding='utf-8')
    f = open(infile, 'r', encoding='utf-8')
    for line in f:
        print("ele =----", line)
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
        else:
            chong_count = chong_count + 1
    print(" chong_count = ", chong_count)



if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile + '.out'

    chong(infile, outfile)
    print("finish.")



