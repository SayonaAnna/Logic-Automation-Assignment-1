class Formula:
    pass


class Predicate(Formula):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"{self.name}({', '.join(self.args)})"


class Implies(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} -> {self.right})"


class ForAll(Formula):
    def __init__(self, var, body):
        self.var = var
        self.body = body

    def __repr__(self):
        return f"(forall {self.var}. {self.body})"
    
def parse_formula(text):
    text = text.strip()

    # handle forall
    if text.startswith("forall"):
        parts = text.split(".", 1)
        var = parts[0].split()[1]
        body = parts[1].strip()
        return ForAll(var, parse_formula(body))

    # handle implication
    if "->" in text:
        left, right = text.split("->", 1)
        return Implies(parse_formula(left), parse_formula(right))

    # handle predicate like P(x)
    if "(" in text and ")" in text:
        name = text[:text.index("(")]
        args = text[text.index("(")+1:text.index(")")].split(",")
        args = [arg.strip() for arg in args]
        return Predicate(name, args)

    raise ValueError(f"Cannot parse: {text}")