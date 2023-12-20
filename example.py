from eval import calculate_wer, calculate_cer

list_hyps = ['This is an example .', 'This is another example .']
list_refs = ['This is the example :)', 'That is the example .']

wer = calculate_wer(list_hyps, list_refs)
cer = calculate_cer(list_hyps, list_refs)

print("wer: ", wer)
print("cer: ", cer)