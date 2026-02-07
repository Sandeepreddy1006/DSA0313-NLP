# Tiny grammar
grammar = {
    "S": [["NP","VP"]],
    "NP": [["DET","NOUN"]],
    "VP": [["VERB","NP"],["VERB"]],
    "DET": [["the"],["a"]],
    "NOUN": [["cat"],["dog"]],
    "VERB": [["sees"],["pets"]]
}

def parse(sym, tokens):
    if sym not in grammar:  # terminal
        return (sym, tokens[1:]) if tokens and tokens[0]==sym else None
    for prod in grammar[sym]:
        rem=tokens; children=[]
        for s in prod:
            r=parse(s,rem)
            if not r: break
            node,rem=r; children.append(node)
        else: return ((sym,children),rem)
    return None

def parse_sentence(sent):
    r=parse("S",sent.split())
    return r[0] if r and not r[1] else None

print(parse_sentence("the cat sees a dog"))