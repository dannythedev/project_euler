## [*Problem 221 - Alexandrian Integers.*](https://projecteuler.net/problem=221 "Go to problem page.")

$A = p \cdot q \cdot r, \text{ }\text{ }\text{ } \dfrac{1}{A} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r}$  
  
$\dfrac{1}{p \cdot q \cdot r} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r} \rightarrow^{^{\cdot (pqr)}}$  
  
$1 = \dfrac{{p \cdot q \cdot r}}{p} + \dfrac{{p \cdot q \cdot r}}{q} + \dfrac{{p \cdot q \cdot r}}{r} \rightarrow$  
  
$1 = {q \cdot r} + {p \cdot r} + {p \cdot q} \rightarrow$  
  
$1 = q \cdot(r +  p) + p \cdot r \rightarrow$

$1 - p \cdot r = q \cdot(r +  p) \rightarrow$  
  
$\dfrac{1 - p \cdot r}{(r +  p)} = q$ , We now know that either:  
$(1) \text{ } (1 - p \cdot r>0)\wedge\text{ }(r + p>0)$ or  
$(2)\text{ } (1 - p \cdot r<0)\wedge\text{ }(r + p<0)$.  
  
Since $p,r$ are integers, then   
$(1)$ can happen if and only if $(1 > p \cdot r) \text{ }\leftrightarrow\text{ } (p>0 \wedge \text{ } r<0) \vee (p<0 \wedge \text{ } r>0)$.   
$(2)$ can only happen if and only if $(1 < p \cdot r) \text{ }\leftrightarrow\text{ } (p>0 \wedge \text{ } r>0) \vee (p<0 \wedge \text{ } r<0)$, but since $r+p<0$, then the only viable option is that both $p,r<0$.
  
Since $A$ is a positive integer and $A = p \cdot q \cdot r$, than at least one integer $q,p,r$ has to be positive. This also means that either $(p,r<0\wedge\text{ }q>0)\text{ }\vee\text{ }(p,q,r>0)$.  
But $p,q,r<0$ cannot happen due to the proof of $(1)$ and $(2)$ stating at least one composite of $A$ has to be negative.  
So the only occurance is $p,r>0, \text{ } q>0$.  
  
  
  
$A = p \cdot \dfrac{1 - p \cdot r}{(r +  p)} \cdot r \rightarrow$  
  
$A = \dfrac{pr \cdot(1 - pr)}{(r +  p)}$
  

```python
Text
```
<details>
  <summary>View answer</summary>  
Text
</details>
