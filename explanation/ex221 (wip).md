## [*Problem 221 - Alexandrian Integers.*](https://projecteuler.net/problem=221 "Go to problem page.")

Since $A$ is the product of three integers, then it is a composite number and cannot be prime.

$A = p \cdot q \cdot r, \text{ }\text{ }\text{ } \dfrac{1}{A} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r}$  
  
$\dfrac{1}{p \cdot q \cdot r} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r} \rightarrow^{^{\cdot (pqr)}}$  
  
$1 = \dfrac{{p \cdot q \cdot r}}{p} + \dfrac{{p \cdot q \cdot r}}{q} + \dfrac{{p \cdot q \cdot r}}{r} \rightarrow$  
  
$1 = {q \cdot r} + {p \cdot r} + {p \cdot q} \rightarrow$  
  
$1 = q \cdot(r +  p) + p \cdot r \rightarrow$

$1 - p \cdot r = q \cdot(r +  p) \rightarrow$

$\dfrac{1 - p \cdot r}{(r +  p)} = q$  
  
$A = p \cdot \dfrac{1 - p \cdot r}{(r +  p)} \cdot r \rightarrow$  
  
$A = \dfrac{pr \cdot(1 - pr)}{(r +  p)}$
  

```python
Text
```
<details>
  <summary>View answer</summary>  
Text
</details>
