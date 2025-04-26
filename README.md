# GCD Extended Algorithm: Finding Bézout coefficients

The GCD algorithm can be extended so that we can find the number of times that each number is multiplied to give the GCD.
Mathematically, this means finding the numbers $x$ and $y$ such that

\[
a \cdot x + b \cdot y = \gcd(a, b)
\]

This is called Bézout’s identity and is the basis for finding modular inverses. A modular inverse (or modular multiplicative inverse) is a number $x$ such that

\[
a \cdot x \equiv 1 \pmod{b}
\]

Understanding this is foundational for algorithms in modern cryptography and forms the backbone of algorithms such as RSA.

... (truncated for brevity, see code for full insertion)