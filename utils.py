import re

def luhn_checksum_is_valid(card_number):
    def digits_of(n): return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(digits_of(2 * d)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10 == 0

def partial_mask(data):
    if len(data) <= 4:
        return '*' * len(data)
    return '*' * (len(data) - 4) + data[-4:]

def mask_sensitive_data(text):
    if not text:
        return text
    return '*' * len(text)
