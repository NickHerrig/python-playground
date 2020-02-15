
def list_comp_example():
    symbols = "#(@#%*@#$()_)@#$("
    codes = [ ord(symbol) for symbol in symbols ]
    return codes 


ranks = [str(n) for n in range(2,11)] + list('JQKA')
suits = 'heart club spade diamond'.split()
cards_tuples = [(rank, suit) for rank in ranks for suit in suits]
print(len(cards_tuples))
