## [*Problem 221 - Alexandrian Integers.*](https://projecteuler.net/problem=221 "Go to problem page.")

$\bullet\text{ }$ Since $A$ is the product of three integers, then it is a composite number and cannot be prime.  
$\bullet\text{ }$ Since $A$ is a positive integer, than at least one integer $q,p,r$ has to be positive. This also means that either $p,q<0, r>0$ or $p,q,r>0$. We can now deduce that $p\cdot q$ is a positive composite number.

$A = p \cdot q \cdot r, \text{ }\text{ }\text{ } \dfrac{1}{A} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r}$  
  
$\dfrac{1}{p \cdot q \cdot r} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r} \rightarrow^{^{\cdot (pqr)}}$  
  
$1 = \dfrac{{p \cdot q \cdot r}}{p} + \dfrac{{p \cdot q \cdot r}}{q} + \dfrac{{p \cdot q \cdot r}}{r} \rightarrow$  
  
$1 = {q \cdot r} + {p \cdot r} + {p \cdot q} \rightarrow$  
  
$1 = q \cdot(r +  p) + p \cdot r \rightarrow$

$1 - p \cdot r = q \cdot(r +  p) \rightarrow$

$\dfrac{1 - p \cdot r}{(r +  p)} = q$ , Since $1 - p\cdot r$, then one of the numbers $p,r$ has to be negative.
But the above specifies that either $p,q,r>0$, or $p,q>0, r<0$, so this means that only $p,r<0, q>0$.
  
$A = p \cdot \dfrac{1 - p \cdot r}{(r +  p)} \cdot r \rightarrow$  
  
$A = \dfrac{pr \cdot(1 - pr)}{(r +  p)}$
  

```python
Text
```
<details>
  <summary>View answer</summary>  
Text
</details>
