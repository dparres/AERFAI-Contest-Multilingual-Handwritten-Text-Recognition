import fastwer

def calculate_wer(list_hyps, list_refs):
    return round(fastwer.score(list_hyps, list_refs), 2)

def calculate_cer(list_hyps, list_refs):
    return round(fastwer.score(list_hyps, list_refs, char_level=True), 2)