def approximate_pi(n_terms):
    """
    Approximate π using the Leibniz series:
    π ≈ 4 * Σ_{k=0}^{n_terms-1} (-1)^k / (2k+1)
    """
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("n_terms must be a non-negative integer")

    # 1/1 - 1/3 + 1/5 - 1/7 + ...
    leibniz_series = [((-1) ** k) / (2 * k + 1) for k in range(n_terms)]
    total = sum(leibniz_series)
    return 4.0 * total


"""
def approximate_pi(n_terms):
    total = 0.0
    for n in range(n_terms):
        term = (-1.0)**n / (2*n + 1)
        total += term
    return 4.0 * total
   """
    
    
"""
def approximate_pi(n_terms):
    leibniz_series = []
    sign = 1.0     # start positive and change 
    denom = 1      #the odd numbers 1,3,5,7..
    for _ in range(n_terms):
        term = sign / denom
        leibniz_series.append(term)
        sign = -sign
        denom += 2
    return 4 * sum(leibniz_series)
    """
