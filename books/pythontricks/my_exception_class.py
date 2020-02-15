
class NegativeMoneyError(ValueError):
    pass

def validate(amount):
    if amount < 0:
        raise NegativeMoneyError(amount)

validate(-10)
