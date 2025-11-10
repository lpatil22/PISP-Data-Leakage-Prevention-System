import re

# Luhn check for credit cards
def luhn_checksum_is_valid(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(digits_of(d*2))
    return total % 10 == 0

# Mask full sensitive data
def mask_sensitive_data(data_type, value):
    if data_type == "Email Address":
        # show first character + mask the rest before @
        parts = value.split("@")
        return parts[0][0] + "*"*(len(parts[0])-1) + "@" + parts[1]
    elif data_type == "Credit Card Number":
        return value[:2] + "*"*(len(value)-6) + value[-4:]
    elif data_type == "SSN":
        return "*"*len(value)
    elif data_type == "Password":
        return "*"*len(value)
    else:
        return "*"*len(value)


# Partial mask for emails (example: a****@example.com)
def partial_mask(data):
    if '@' in data:
        name, domain = data.split('@', 1)
        if len(name) <= 1:
            masked_name = '*'
        else:
            masked_name = name[0] + '*' * (len(name)-1)
        return masked_name + '@' + domain
    elif len(data) > 4:  # credit card or SSN
        return data[:2] + '*'*(len(data)-4) + data[-2:]
    else:
        return '*'*len(data)
