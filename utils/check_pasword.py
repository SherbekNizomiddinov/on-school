from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def check_pass(parol: str) -> bool:
    '''
    bu funksiya parol kuchini tekshiradi
    retun: agar parol barcha mezonlarga javob bersa, rost, boshqa noto'g'ri.
    '''

    u, l, d, p = 0, 0, 0, 0

    if len(parol) > 7:
        for c in parol:
            if c in ascii_uppercase: u = 1
            elif c in ascii_lowercase: l = 1
            elif c in digits: d = 1
            elif c in punctuation: p = 1
            else: return False

    return all([u, l, d, p])