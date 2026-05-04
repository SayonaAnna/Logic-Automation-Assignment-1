from parser import Predicate, Implies, ForAll


def prove_improved(formula, depth=0, max_depth=10, visited=None):
    if visited is None:
        visited = set()

    print("  " * depth + f"Trying: {formula}")

    # --- stop if too deep ---
    if depth > max_depth:
        print("  " * depth + "Stopped (depth limit)")
        return False

    # --- avoid repeating same formula ---
    if str(formula) in visited:
        print("  " * depth + "Stopped (already visited)")
        return False

    visited.add(str(formula))

    # --- Case 1: Predicate ---
    if isinstance(formula, Predicate):
        return True

    # --- Case 2: Implication ---
    if isinstance(formula, Implies):
        return prove_improved(formula.right, depth+1, max_depth, visited)

    # --- Case 3: ForAll ---
    if isinstance(formula, ForAll):
        instantiated = substitute(formula.body, formula.var, "a")
        return prove_improved(instantiated, depth+1, max_depth, visited)

    return False


def substitute(formula, var, value):
    if isinstance(formula, Predicate):
        new_args = [value if arg == var else arg for arg in formula.args]
        return Predicate(formula.name, new_args)

    if isinstance(formula, Implies):
        return Implies(
            substitute(formula.left, var, value),
            substitute(formula.right, var, value)
        )

    return formula