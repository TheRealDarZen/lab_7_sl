import sys

def build_acronym(list_of_words: []):
    return ''.join(map(lambda x: x[0], list_of_words)).upper()

def find_median(list_of_numbers: []):
    sort_nums = sorted(list_of_numbers)

    length = len(sort_nums)
    center = length // 2

    return sort_nums[center] if length % 2 != 0 else (sort_nums[center] + sort_nums[center - 1]) / 2

#Newton's method
def find_square_root(x: float, epsilon: float, prev_g: float):
    previous_guess = prev_g if prev_g > 0 else x
    next_guess = 0.5 * (previous_guess + (x / previous_guess))
    return next_guess if abs(next_guess**2 - x) < epsilon else find_square_root(x, epsilon, next_guess)



NOPREV = -1
if __name__ == "__main__":
    print(build_acronym(["Zap", "Usps", "Kara"]))
    print(find_median([5, 7, 3, 9, 1, 2, 8, 6, 0]))
    print(find_square_root(3.0, 0.1, NOPREV))
