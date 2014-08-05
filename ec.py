# copyright 2014 tim shaffer

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

crv = {"a": -1, "b": 1, "p": 113}
pt = (69, 96)

# this is crazy inefficient, but it's late and this is only a toy
# script, anyway
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ArithmeticError("{}^-1 mod {} does not exist".format(a, m))

def on(curve, P):
    x, y = P
    p = curve["p"]
    alpha = curve["a"]
    beta = curve["b"]
    return (y**2) % p == (x**3 + alpha * x + beta) % p

def add(curve, P, Q):
    if P == ():
        return Q
    elif Q == ():
        return P

    p = curve["p"]
    alpha = curve["a"]
    a, b = P
    c, d = Q

    if (a - c) % p == 0 and (b + d) % p == 0:
        return ()

    if (a - c) % p == 0:
        m = (3 * a**2 + alpha) * modinv(2 * b, p)
    else:
        m = (d - b) * modinv(c - a, p)
    k = b - m * a

    g = m**2 - a - c
    h = -m * g - k

    return g % p, h % p

def mul(curve, P, n):
    Q = ()
    for i in range(n):
        Q = add(curve, Q, P)
    return Q

def ord(curve, P):
    t = 1
    Q = P
    while Q != ():
        Q = add(curve, Q, P)
        t += 1
    return t
