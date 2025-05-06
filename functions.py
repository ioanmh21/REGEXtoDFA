from collections import deque

def alfabet(regex):
    dex=set()
    for char in regex:
        if char.isalpha() or char.isdigit():
            dex.add(char)

    return dex

def add_operatori_concatenare(regex):
    result = ""
    operators = set(['*', '+', '?', '|'])
    for i in range(len(regex)):
        pos = regex[i]
        result += pos

        if i+1 < len(regex):
            next = regex[i+1]

            if pos=='(':
                pass
            if pos==')':
                if next=='(' or next.isalpha() or next.isdigit():
                    result+='.'
            if pos in operators and pos!='|':
                if next=='(' or next.isalpha() or next.isdigit():
                    result+='.'
            if pos.isalpha() or pos.isdigit():
                if next=='(' or next.isalpha() or next.isdigit():
                    result+='.'

    return result


def forma_poloneza(regex):
    priorities={'|':1, '.':2, '*':3, '+':3, '?':3}
    output=''
    stack=[]

    for char in regex:
        if char.isalpha() or char.isdigit():
            output+=char
        elif char=='(':
            stack.append(char)
        elif char==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        elif char in priorities:
            while (stack and stack[-1] != '(' and priorities.get(stack[-1], 0) >= priorities[char]):
                output += stack.pop()
            stack.append(char)
        else:
            raise ValueError('Error')

    while stack:
        output+=stack.pop()
        
    return output


class State:
    def __init__(self):
        self.transitions = {}
        self.epsilon = set()

class Fragment:
    def __init__(self, start, accepts):
        self.start = start
        self.accepts = accepts


def thompson_nfa(postfix):
    stack = []

    for char in postfix:
        if char.isalpha() or char.isdigit():
            start = State()
            accept = State()
            start.transitions[char] = {accept}
            stack.append(Fragment(start, {accept}))

        elif char == '.':
            frag2 = stack.pop()
            frag1 = stack.pop()
            for accept in frag1.accepts:
                accept.epsilon.add(frag2.start)
            stack.append(Fragment(frag1.start, frag2.accepts))

        elif char == '|':
            frag2 = stack.pop()
            frag1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.update([frag1.start, frag2.start])
            for a in frag1.accepts:
                a.epsilon.add(accept)
            for a in frag2.accepts:
                a.epsilon.add(accept)
            stack.append(Fragment(start, {accept}))

        elif char == '*':
            frag = stack.pop()
            start = State()
            accept = State()
            start.epsilon.update([frag.start, accept])
            for a in frag.accepts:
                a.epsilon.update([frag.start, accept])
            stack.append(Fragment(start, {accept}))

        elif char == '+':
            frag = stack.pop()
            start = State()
            accept = State()
            start.epsilon.add(frag.start)
            for a in frag.accepts:
                a.epsilon.update([frag.start, accept])
            stack.append(Fragment(start, {accept}))

        elif char == '?':
            frag = stack.pop()
            start = State()
            accept = State()
            start.epsilon.update([frag.start, accept])
            for a in frag.accepts:
                a.epsilon.add(accept)
            stack.append(Fragment(start, {accept}))

        else:
            raise ValueError("Error")

    return stack[0]

def epsilon_closure(states):
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return closure


def move(states, symbol):
    next_states = set()
    for state in states:
        if symbol in state.transitions:
            next_states.update(state.transitions[symbol])
    return next_states

def nfa_to_dfa(nfa, alphabet):
    def state_id(states):
        return frozenset(states)

    start_set = epsilon_closure({nfa.start})
    dfa_states = {state_id(start_set): 0}
    dfa_transitions = {}
    dfa_accepts = set()
    queue = deque([start_set])
    state_counter = 1

    while queue:
        current = queue.popleft()
        current_id = dfa_states[state_id(current)]
        dfa_transitions[current_id] = {}

        for symbol in alphabet:
            next_set = epsilon_closure(move(current, symbol))
            next_id = state_id(next_set)

            if not next_set:
                continue

            if next_id not in dfa_states:
                dfa_states[next_id] = state_counter
                queue.append(next_set)
                state_counter += 1

            dfa_transitions[current_id][symbol] = dfa_states[next_id]

        if any(s in nfa.accepts for s in current):
            dfa_accepts.add(current_id)

    return {
        "start": 0,
        "transitions": dfa_transitions,
        "accepts": dfa_accepts
    }

def simulate_dfa(dfa, word):

    current_state=dfa['start']

    for char in word:
        transitions = dfa["transitions"].get(current_state, {})
        if char not in transitions:
            return False
        current_state = transitions[char]

    return current_state in dfa["accepts"]
