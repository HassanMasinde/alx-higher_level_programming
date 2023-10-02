import subprocess

def test_nqueens():
    test_cases = [
        (4, [
            [[0, 1], [1, 3], [2, 0], [3, 2]],
            [[0, 2], [1, 0], [2, 3], [3, 1]]
        ]),
        (6, [
            [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]],
            [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]],
            [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]],
            [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
        ])
        # Add more test cases for different values of N here
    ]

    for n, expected_solutions in test_cases:
        output = subprocess.check_output(['./101-nqueens.py', str(n)], universal_newlines=True)
        solutions = [list(map(int, line.strip().split(','))) for line in output.strip().split('\n')]

        assert solutions in expected_solutions, f"Failed for N={n}"

if __name__ == "__main__":
    test_nqueens()
    print("All tests passed!")

