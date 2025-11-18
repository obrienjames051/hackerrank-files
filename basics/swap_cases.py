def swap_case(s):
    # Use the built-in swapcase which correctly swaps the case
    # of each character without accidental global replacements.
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)