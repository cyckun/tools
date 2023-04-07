import csv
import hashlib

def sha256(x):
    s = hashlib.sha256(x.encode('utf-8'))
    return s.hexdigest()

def gen_rand_data(length):
    rand_set = ['raw_id']

    for i in range(1, length):
        rand_set.append(sha256(str(i)))
        if i % 100000 == 0:
            print('------------------------', i)

    
    return rand_set

if __name__== '__main__':
    try:
        rand_set = gen_rand_data(1000000)
        # print(rand_set)
    
        with open('./testdata_1b.csv', 'w', newline='') as csvfile:
            writer  = csv.writer(csvfile)
            for row in rand_set:
                writer.writerow([row])
    except Exception as e:
        print("err = ", e)
