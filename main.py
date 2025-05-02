import json
import functions as func

file='LFA-Assignment2_Regex_DFA_v2.json'
with open(file, 'r') as f:
    data = json.load(f)


for case in data:
    name = case['name']
    regex = case['regex']

    print(name)

    dex=func.alfabet(regex)

    a=func.add_operatori_concatenare(regex)
    a=func.forma_poloneza(a)

    nfa=func.thompson_nfa(a)
    dfa=func.nfa_to_dfa(nfa,dex)

    pairs=case['test_strings']
    for d in pairs:
        word=d['input']
        ans=d['expected']
        if ans==func.simulate_dfa(dfa,word):
            print(word,' ✅')
        else:
            print(word,' ❌')

    print()
