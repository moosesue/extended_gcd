# GCD Extended Algorithm: Finding Bézout coefficients

GCD Extended Algorithm: Finding Bézout coefficients

The GCD algorithm can be extended so that we can find the number of times that each number is multiplied to give the GCD.
Mathematically, this means finding the numbers $x$ and $y$ such that

$a \cdot x + b \cdot y = \gcd(a, b)$

This is called Bézout’s identity and is the basis for finding modular inverses. A modular inverse (or modular multiplicative inverse) is a number $x$ such that

$a \cdot x \equiv 1 \pmod{b}$

Understanding this is foundational for algorithms in modern cryptography and forms the backbone of algorithms such as RSA.

So, using our previous example, we find numbers $x$ and $y$ such that

$35x + 28y = 7$

Using the extended GCD algorithm, we reverse the steps to write each stage in terms of the last until we get back to the original two numbers. 

|Index|Last quotient|Current remainder|$x$|$y$|
|:---:|:-----------:|:---------------:|:-:|:-:|
|0|35|1|0|
|1|28|0|1|
|2|$\frac{35}{28} = 1$ |	35 – 1(28) = 7|	1 – 1 x 0 = 1|0 – 1 x 1 = -1|
|3|$\frac{28}{7} = 4$|	28 – 4(7) = 0|0 – 4 x 1 = -4|1 – 4 x -1 = 5|

So at each step we find : $\frac{a}{b}$, $a – (\frac{a}{b})(b)$, $x_0 – (\frac{a}{b})(x_1)$, $y_0 – (\frac{a}{b})y_1$

35 = 1 x 28 + 7

28 = 4 x 7 + 0

So, this becomes:

7 = (1)35 – 1(28)

So this has an easy solution where $x = 1$ and $y = -1$.

However, the problem becomes more difficult with larger numbers. 

In Python, we can solve this by using the following function:

```python
def extended_gcd(a: int, b: int, positive_x: bool)->tuple[int,int,int]:

    original_a = a
    original_b = b
    
    # We want to find x and y such that ax + by = gcd(a,b)
    # if b > a then the result output will swap and so will the signs of the output.   
    # previous x and y
    x0, y0 = 1,0 #represents a when x = 1 and y = 0
    # current x and y
    x1, y1 = 0,1 #represents b when x = 0 and y = 1

    while b !=0: #while the remainder isn't 0......
        # This part is same as ordinary GCD algorithm. 
        # quotient = whole number floor result of a divided by b
        quotient = a//b
        # set a to b and at same time set remainder b = a mod b
        a, b = b, a % b
        
        # This part for finding the coefficients by setting current values based on previous values.
        # We are keeping track of expressing each remainder in terms of current a and b.
        # This is why we are referring back to the previous values.
        # current x0 becomes last x1 and current x1 becomes last x0 - current quotient x last x1
        # This is because the new remainder is previous a - quotient x previous b.
        x0, x1 = x1, x0 - quotient * x1
        # current y0 becomes last y1 and current y1 becomes last y0 - current quotient x last y1
        y0, y1 = y1, y0 - quotient * y1

    # If we want positive x but we have negative x as a result, we can use:
    # x = x0 + k*(b/gcd)
    # y = y0 + k*(a/gcd)
    # k will represent a shift of multiples of b/gcd (or would be a/gcd if we wanted positive y)
    # needed if we are wanting a*x = 1 (mod original_b)
    if (positive_x and x0 < 0):
       # Shift of k calculates how much needs to be added in one go where original_b//a is size of step needed
       # use (original_b//a) - 1 to make sure we get shift rounded up so x0 becomes positive.
       shift_k = (abs(x0) + (original_b // a) - 1) // (original_b // a)  # smallest integer needed to make x positive
       x0 += shift_k*(original_b//a) #a = gcd
       y0 -= shift_k*(original_a//a)
            
            
    return a,x0,y0
```
Or in Rust:

```rust
fn extended_gcd(mut a: i32, mut b: i32, positive_x: bool) -> (i32, i32, i32) {
    let original_a = a;
    let original_b = b;

    let mut x0 = 0;
    let mut y0 = 1;
    let mut x1 = 1;
    let mut y1 = 0;

    while b != 0 {
        let quotient = a / b;
        let (new_a, new_b) = (b, a % b);
        a = new_a;
        b = new_b;

        let temp_x0 = x0;
        x0 = x1;
        x1 = temp_x0 - quotient * x1;

        let temp_y0 = y0;
        y0 = y1;
        y1 = temp_y0 - quotient * y1;
    }

    if positive_x && x0 < 0 {
        let shift_k = (x0.abs() + (original_b / a) - 1) / (original_b / a);
        x0 += shift_k * (original_b / a);
        y0 -= shift_k * (original_a / a);
    }

    (a, x0, y0)
}

```
