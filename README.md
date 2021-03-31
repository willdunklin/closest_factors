# closest_factors

Here we're trying to get the nearest factors of a number n.

Specifically we want numbers `a,b` such that `n = a*b`, while minimizing `|a-b|`.

### A use case:
For example, if you want to convert a 1d array of length `n` into the most square 2d matrix possible,
this algorithm efficiently shows what the dimensions `a,b` of that matrix should be for `n`.

## Usage

```
closest_factors(34929)
> (3881, 9)

closest_factors(429538750)
> (343631, 1250)

closest_factors(25)
> (5, 5)
```
