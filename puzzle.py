from functools import lru_cache
import itertools

FOX = "FOX"
GOOSE = "GOOSE"
BEANS = "BEANS"
FARMER = "FARMER"

start_state = (set([FOX,GOOSE,BEANS,FARMER]),set())

ILLEGAL = "ILLEGAL"
SAFE = "SAFE"
UNSAFE = "UNSAFE"
WIN = "WIN"

def copy_state(state):
    return (state[0].copy(), state[1].copy())

def evaluate_state(state):
    if FOX in state[1] and GOOSE in state[1] and BEANS in state[1] and FARMER in state[1]:
        return WIN
    # FOX eats GOOSE
    for side in state:
        if FOX in side and GOOSE in side and not FARMER in side:
            return UNSAFE
    # GOOSE eats BEANS
    for side in state:
        if BEANS in side and GOOSE in side and not FARMER in side:
            return UNSAFE
    return SAFE

def legal_state(state):
    objs = [FOX, GOOSE, BEANS, FARMER]
    for obj in objs:
        if obj in state[0] and obj in state[1]:
            return False
        if obj not in state[0] and obj not in state[1]:
            return False
    return True

def move(state, what):
    # keep state immutable
    state = copy_state(state)
    current = state[0]
    opposite = state[1]
    # is it allowed?
    if not legal_state(state):
        return (ILLEGAL, state)
    if FARMER in state[0]:
        (current, opposite) = state
    elif FARMER in state[1]:
        (opposite, current) = state
    else:
        return (ILLEGAL, state)
    if what is not None and what not in current:
        return (ILLEGAL, state)
    # do the move
    if not what is None:
        current.remove(what)
        opposite.add(what)
    current.remove(FARMER)
    opposite.add(FARMER)
    ev = evaluate_state(state)
    return (ev, state)

    
def evaluate_moves(list_of_moves, state=None):
    if state is None:
        state = copy_state(start_state)
    if len(list_of_moves) > 0:
        # print("In state: %s moving: %s" % (state, list_of_moves[0]))
        ev, new_state = move(state, list_of_moves[0])
        # print(ev)
        if ev == WIN and len(list_of_moves) == 1: # what if we have more moves?
            return True
        elif ev == SAFE:
            return evaluate_moves(list_of_moves[1:] , state=new_state)
        else:
            return False
    else:
        return False # we didn't win

print(evaluate_moves([BEANS]))
print(evaluate_moves([FOX]))
print(evaluate_moves([GOOSE, None, FOX, GOOSE, BEANS]))
print(evaluate_moves([GOOSE, None, FOX, GOOSE, BEANS, None, GOOSE]))


import itertools
for i in range(1,11):
    print(i)
    for moves in itertools.product([GOOSE,FOX, BEANS, None], repeat=i):
        if evaluate_moves( moves ):
            print(i,moves)

def is_prime(x):
    if x == 1:
        return True
    if x < 1:
        return False
    for y in range(2,x):
        if x % y == 0:
            return False
    return True

primes = [x for x in range(2,100) if is_prime(x)]
# all pairs of primes less than 100 where their sum is a prime
print([x for x in   itertools.combinations(primes,2) if is_prime(sum(x))])
# all triples of primes less than 100 where their sum is a prime
print([x for x in   itertools.combinations(primes,3) if is_prime(sum(x))])
# count of triples of primes less than 100 where their sum is prime
print(len([x for x in   itertools.combinations(primes,3) if is_prime(sum(x))]))
# count of triples of primes less than 100 where their sum is NOT prime
print(len([x for x in   itertools.combinations(primes,3) if not is_prime(sum(x))]))

print(len([x for x in   itertools.combinations(primes,4) if is_prime(sum(x))]))
print(len([x for x in   itertools.combinations(primes,4) if not is_prime(sum(x))]))


def sum_prime_and_divisible(primes):
    sump = sum(primes)
    if is_prime(sump):
        for x in primes:
            if sump % x == 0:
                return True
    return False


def sum_prime_and_divisible_digits(primes):
    sump = sum(primes)
    if is_prime(sump):
        for x in primes:
            if str(x) in str(sump):
                return True
    return False


primes = [x for x in range(2,600) if is_prime(x)]
[x for x in itertools.combinations(primes,3) if sum_prime_and_divisible(x)]

primes = [x for x in range(2,100) if is_prime(x)]
[x for x in itertools.combinations(primes,3) if sum_prime_and_divisible_digits(x)]

def exponentiate(primes):
    v = primes[0]
    for i in range(1,len(primes)):
        v = v**primes[i]
    return v
primes = [x for x in range(2,50) if is_prime(x)]

[x for x in itertools.permutations(primes,2) if is_prime(exponentiate(x) - 1)]

import random
import itertools

_combo = list(range(0,10))
random.shuffle(_combo)

def combo(v):
    return list(v) == _combo

[x for x in itertools.permutations(list(range(0,10))) if combo(x)]

