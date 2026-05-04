from parser import Predicate, Implies, ForAll


def prove(formula):
    print("Trying to prove:", formula)

    # 1: Predicate (base case)
    if isinstance(formula, Predicate):
        # baseline assumption: predicates are true
        return True

    # 2: Implication (A -> B) 
    if isinstance(formula, Implies):
        # backward reasoning:
        # to prove A -> B, try proving B
        return prove(formula.right)

    # 3: ForAll (forall x. A) 
    if isinstance(formula, ForAll):
        # instantiate x with a constant (e.g., 'a')
        instantiated = substitute(formula.body, formula.var, "a")
        return prove(instantiated)

    # No rule applies 
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