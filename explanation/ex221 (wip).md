## [*Problem 221 - Alexandrian Integers.*](https://projecteuler.net/problem=221 "Go to problem page.")

$A = p \cdot q \cdot r, \text{ }\text{ }\text{ } \dfrac{1}{A} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r}$  
  
$\dfrac{1}{p \cdot q \cdot r} = \dfrac{1}{p} + \dfrac{1}{q} + \dfrac{1}{r} \rightarrow^{^{\cdot (pqr)}}$  
  
$1 = \dfrac{{p \cdot q \cdot r}}{p} + \dfrac{{p \cdot q \cdot r}}{q} + \dfrac{{p \cdot q \cdot r}}{r} \rightarrow$  
  
$1 = {q \cdot r} + {p \cdot r} + {p \cdot q} \rightarrow$  
  
$1 = q \cdot(r +  p) + p \cdot r \rightarrow$

$1 - p \cdot r = q \cdot(r +  p) \rightarrow$  
  
$\dfrac{1 - p \cdot r}{(r +  p)} = q$.  
  
We can assume $q>0$ since we are given $A>0$, this is because $A = p \cdot q \cdot r\text{ } \rightarrow\text{ }(p,r<0\wedge\text{ }q>0)\text{ }\vee\text{ }(p,q,r>0)$.  
Because $q>0$ then for any $n,d$ that make $q=\dfrac{n}{d}$ there must be $n\wedge\text{ }d>0\vee\text{ }n\wedge\text{ }d<0$.  
This means:    
$(1) \text{ } (1 - p \cdot r>0)\wedge\text{ }(r + p>0)$ or  
$(2)\text{ } (1 - p \cdot r<0)\wedge\text{ }(r + p<0)$.  
  
Since $p,r$ are integers, then   
$(1)$ $(1 - p \cdot r>0) \leftrightarrow (1 > p \cdot r) \text{ }\leftrightarrow\text{ } (p>0 \wedge \text{ } r<0) \vee (p<0 \wedge \text{ } r>0)$.   
In which case, at least one of $p,r$ has to be negative.  

$(2)$ $(1 - p \cdot r<0) \leftrightarrow (1 < p \cdot r) \text{ }\leftrightarrow\text{ } (p>0 \wedge \text{ } r>0) \vee (p<0 \wedge \text{ } r<0)$,  
but since $r+p<0$, then at least one of $p,r$ has to be negative.  
  
This means the initial $p,q,r<0$ cannot happen.
  
So the only occurance is $p,r<0, \text{ } q>0$.  
  
  
  
$A = p \cdot \dfrac{1 - p \cdot r}{(r +  p)} \cdot r \rightarrow$  
  
$A = \dfrac{pr \cdot(1 - pr)}{(r +  p)}$
  
We also know that $A$ is an integer, so $pr \cdot(1 - pr) \equiv 0 \pmod{r+p}$ must occur. 

```python
Text
```
<details>
  <summary>View answer</summary>  
Text
</details>
