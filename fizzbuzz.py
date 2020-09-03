def fizzbuzz_convert(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    return str(number)


assert fizzbuzz_convert(15) == 'FizzBuzz'
assert fizzbuzz_convert(5) == 'buzz'
assert fizzbuzz_convert(3) == 'fizz'
assert fizzbuzz_convert(1) == '1'
