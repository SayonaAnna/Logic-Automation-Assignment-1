from parser import parse_formula
from baseline import prove
from improved import prove_improved


def run_test(file_name):
    print(f"\n=== Testing {file_name} ===")

    with open(f"datasets/{file_name}", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        formula = parse_formula(line)

        print("\nFormula:", formula)

        print("\n--- BASELINE ---")
        baseline_result = prove(formula)
        print("Baseline Result:", baseline_result)

        print("\n--- IMPROVED ---")
        improved_result = prove_improved(formula)
        print("Improved Result:", improved_result)


# Run all datasets
run_test("easy.txt")
run_test("medium.txt")
run_test("hard.txt")