# Author: Eric Xu

# parse a sentence into a ngram dict
# key: ngram
# val: ngram count

def parse_sentence_ngram(sentence, ngram=1, toLowerCase=True, stripPunctuation=False):
#   prepare
    if stripPunctuation:
        sentence.replace('.','')
        sentence.replace(',','')
        sentence.replace('?','')
        sentence.replace('!','')
    if toLowerCase:
        bag_of_words = sentence.lower().split()
    else:
        bag_of_words = sentence.split()
    parse_sent = dict()
    for i in range(len(bag_of_words) - ngram + 1):
        word_list = bag_of_words[i:ngram+i]
        word = ''
        for i in word_list:
            word += i + ' '
        word = word[:-1]
        if word in parse_sent:
            parse_sent[word] += 1
        else:
            parse_sent[word] = 1
    return parse_sent

def bleu_ngram(ref_list, mt_out, ngram, toLowerCase=True, stripPunctuation=False):
    if ngram > len(mt_out.split()):
        return
    # get max count for all ref sentences
    max_count = dict()
    for sentence in ref_list:
    #   parse sentence into dict
        parse_sent = parse_sentence_ngram(sentence, ngram, toLowerCase, stripPunctuation)
    #   merge parse_sent into max_count
        for key, val in parse_sent.items():
            if key not in max_count or max_count[key] < val:
                max_count[key] = val

    # count bleu score 
    output_count = parse_sentence_ngram(mt_out, ngram, toLowerCase, stripPunctuation)
    total_count = sum(output_count.values())
    valid_keys = []
    for key in output_count.keys():
        if key in max_count:
            valid_keys.append(key)
    count_clip = sum(output_count[key] if output_count[key] < max_count[key] else max_count[key] for key in valid_keys)
    bleu_score = count_clip / total_count
    return bleu_score

from math import exp
def combined_exp_bleu_ngram(ref_list, mt_out, ngram, bp=True ,toLowerCase=True, stripPunctuation=False):
#   bleu score for each ngram
    bleu_list=[]
    for i in range(1,ngram+1):
        bleu_list.append(bleu_ngram(ref_list, mt_out, i, toLowerCase=True, stripPunctuation=False))
#         print(str(i) + 'gram is: ' + str(bleu_list[-1]))
        
#   bp penalty
    len_mt = len(mt_out)
    len_ref_min = min([len(sent.split()) for sent in ref_list])
    if len_mt > len_ref_min:
        bp = 1
    else:
        bp = exp(1-len_mt/len_ref_min)
        
#     print('bp is: ' + str(bp))
    
    if bp is False:
        bp = 1
        
    return bp * exp(sum(bleu_list) / ngram)


