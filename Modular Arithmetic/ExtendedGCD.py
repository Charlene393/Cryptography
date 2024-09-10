def extended_gcd(p, q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, x, y) = extended_gcd(q % p, p)
        return (gcd, y - (q // p) * x, x)

p = 26513
q = 32321

gcd, x, y = extended_gcd(p, q)
print("[+] GCD: {}".format(gcd))
print("[+] x,y: {},{}".format(x, y))
print("\n[*] FLAG: crypto{{{},{}}}".format(x, y))
