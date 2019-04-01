import csv
from operator import itemgetter
candidate_results= []
candidates = []
total = 0
with open('election_data.csv') as csvfile:

    read_csv = csv.reader(csvfile, delimiter= ',')
    header = next(read_csv)
    for row in read_csv:
        total = total + 1
        if row[2] not in candidates:
            candidates.append(row[2])   
    for candidate in candidates:
        csvfile.seek(0)
        read_csv = csv.reader(csvfile, delimiter= ',')
        next(read_csv)
        candidate_total= 0
        for row in read_csv:
            if row[2] == candidate:
                candidate_total += 1
        candidate_results.append([candidate, candidate_total/total,total])
candidate_results = sorted(candidate_results,key= itemgetter(1))
print('TOTAL',total)
print('Candidate Results',candidate_results)
print('Winner',candidate_results[-1])

outputname = 'output.txt'

with open(outputname, 'w') as f:
    f.write('TOTAL: '+str(total)+"\n")
    f.write('Candidate Results: '+str(candidate_results)+"\n")
    f.write('Winner: '+str (candidate_results[-1])+"\n")
    print('File written: {}'.format(outputname))
