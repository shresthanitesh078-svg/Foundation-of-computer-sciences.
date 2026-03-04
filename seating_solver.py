# ST4015CMD - Task 2: Seating Arrangement Solver
# Demonstrates Brute Force vs Heuristic approaches

from itertools import permutations
import time

# ── Sample Data ──────────────────────────────────────
students = ["Alice","Bob","Charlie","Diana","Eve"]
cities   = {"Alice":"Kathmandu","Bob":"Pokhara","Charlie":"Kathmandu",
            "Diana":"Lalitpur","Eve":"Pokhara"}
friends  = {("Alice","Bob"),("Bob","Charlie"),("Diana","Eve")}

def are_friends(a, b):
    return (a,b) in friends or (b,a) in friends

def same_city(a, b):
    return cities[a] == cities[b]

def is_valid(arrangement):
    for i in range(len(arrangement)-1):
        a, b = arrangement[i], arrangement[i+1]
        if are_friends(a, b):
            return False
        if same_city(a, b):
            return False
    return True

# ── Brute Force ───────────────────────────────────────
def brute_force(students):
    print("\n=== BRUTE FORCE APPROACH ===")
    start = time.time()
    count = 0
    for perm in permutations(students):
        count += 1
        if is_valid(perm):
            elapsed = time.time() - start
            print(f"Valid arrangement found: {list(perm)}")
            print(f"Checked {count} arrangements in {elapsed:.4f}s")
            return list(perm)
    print("No valid arrangement exists.")
    return None

# ── Heuristic (Greedy + Constraint) ──────────────────
def count_constraints(student, placed, remaining):
    conflicts = 0
    for other in remaining:
        if are_friends(student, other) or same_city(student, other):
            conflicts += 1
    return conflicts

def heuristic(students):
    print("\n=== HEURISTIC APPROACH ===")
    start = time.time()
    remaining = students[:]
    arrangement = []
    # Sort by most constrained first
    remaining.sort(key=lambda s: sum(
        1 for o in students if o!=s and (are_friends(s,o) or same_city(s,o))
    ), reverse=True)
    for student in remaining:
        arrangement.append(student)
    # Local swap improvement
    improved = True
    swaps = 0
    while improved:
        improved = False
        for i in range(len(arrangement)-1):
            if are_friends(arrangement[i],arrangement[i+1]) or same_city(arrangement[i],arrangement[i+1]):
                for j in range(i+2, len(arrangement)):
                    arrangement[i+1], arrangement[j] = arrangement[j], arrangement[i+1]
                    if is_valid(arrangement):
                        improved = True
                        swaps += 1
                        break
                    else:
                        arrangement[i+1], arrangement[j] = arrangement[j], arrangement[i+1]
    elapsed = time.time() - start
    valid = is_valid(arrangement)
    print(f"Arrangement: {arrangement}")
    print(f"Valid: {valid} | Swaps made: {swaps} | Time: {elapsed:.4f}s")
    return arrangement

# ── Complexity Demo ───────────────────────────────────
def show_complexity():
    print("\n=== BRUTE FORCE COMPLEXITY ===")
    import math
    for n in [3,5,10,15,20]:
        fact = math.factorial(n)
        secs = fact / 1_000_000_000
        if secs < 60:
            time_str = f"{secs:.4f} seconds"
        elif secs < 3600:
            time_str = f"{secs/60:.2f} minutes"
        elif secs < 86400*365:
            time_str = f"{secs/3600:.2f} hours"
        else:
            time_str = f"{secs/86400/365:.2e} years"
        print(f"  n={n:2d}  |  n! = {fact:>20,}  |  ~{time_str}")

if __name__ == "__main__":
    print("ST4015CMD - Task 2: Classroom Seating Arrangement")
    print("Students:", students)
    print("Friends:", friends)
    print("Cities:", cities)
    show_complexity()
    brute_force(students)
    heuristic(students)
