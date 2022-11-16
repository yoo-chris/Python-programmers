def solution(numbers, k):
    answer = 0
    i = 0
    while k > 1:
        i += 2
        if i >= len(numbers):
            i = i % len(numbers)
        k -= 1
    return numbers[i]