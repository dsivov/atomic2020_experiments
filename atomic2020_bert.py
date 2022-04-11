import glob
import csv
kg = []
relations = ['oWant', 'AtLocation', 'oReact', 'xWant', 'ObjectUse', 'HinderedBy', 'oEffect', 'xIntent', 'isFilledBy', 'xAttr', 
'HasSubEvent', 'isAfter', 'HasProperty', 'xReact', 'Desires', 'xEffect', 'xNeed', 'Causes', 'isBefore', 'CapableOf', 'xReason', 
'NotDesires', 'MadeUpOf']
print(len(relations))

print(relations)
files = glob.glob('atomic2020_data/*.tsv')
for file in files:
    with open(file) as in_file:
        tsv_file = csv.reader(in_file, delimiter="\t")
        for i, line in enumerate(tsv_file):
            sentence = ""
            #kg['node'] = line
            head = line[0]
            relation = line[1]
            tail = line[2]
            if relation == 'isFilledBy':
                sentence = head.replace('___', tail)
                sentence = sentence.replace('___', '')
            if relation == 'AtLocation':
                sentence = head + ' located at ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'oWant' and tail != 'none':
                sentence = head + ' he want ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xWant' and tail != 'none':
                sentence = head + ' he want ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'oReact' and tail != 'none':
                sentence = head + ' and then ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'ObjectUse' and tail != 'none':
                sentence = head + ' used for ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'HinderedBy' and tail != 'none':
                sentence = head + ', this would not happen if ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'oEffect' and tail != 'none':
                sentence = head + ' so he ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xIntent' and tail != 'none':
                sentence = head + ' in order ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xAttr' and tail != 'none':
                sentence = head + ' so he is ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'HasSubEvent' and tail != 'none':
                sentence = head + ' and ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'isAfter' and tail != 'none':
                sentence = head + ', before ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'HasProperty' and tail != 'none':
                sentence = head + ' is ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xReact' and tail != 'none':
                sentence = head + ' and then ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'Desires' and tail != 'none':
                sentence = head + ' desires ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xEffect' and tail != 'none':
                sentence = head + ' so he ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'xNeed' and tail != 'none':
                sentence = head + ', he need ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'Causes' and tail != 'none':
                sentence = head + ' causes ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'isBefore' and tail != 'none':
                sentence = head + ' and then ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'CapableOf' and tail != 'none':
                sentence = head + ' is capable of ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'NotDesires' and tail != 'none':
                sentence = head + ' does not desire ' + tail
                sentence = sentence.replace('___', '')
            if relation == 'MadeUpOf' and tail != 'none':
                sentence = head + ' is made up from ' + tail
                sentence = sentence.replace('___', '')
            kg.append({'entity': line, 'sentence': sentence})
#print(kg)
# list_set = set(relations)
# uniq_rel = list(list_set)
# print(uniq_rel)
