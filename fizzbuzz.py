def fizzbuzz_convert(number):
    for number in range(1, 101):

        if number % 15 == 0:
            return 'fizzbuzz'
        if number % 5 == 0:
            return 'buzz'
        if number % 3 == 0:
            return 'fizz'
        else:
            return number

    assert fizzbuzz_convert(15) == 'fizzbuzz'
    assert fizzbuzz_convert(5) == 'buzz'
    assert fizzbuzz_convert(3) == 'Fizz'
    assert fizzbuzz_convert(number) == number
