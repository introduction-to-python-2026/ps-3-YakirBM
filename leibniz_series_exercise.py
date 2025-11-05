def approximate_pi(n_terms):
    """
    Approximate π using the Leibniz series with n_terms terms.
    π ≈ 4 * Σ_{k=0}^{n_terms-1} (-1)^k / (2k+1)
    """
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("n_terms must be a non-negative integer")

    # 1/(1) - 1/(3) + 1/(5) - 1/(7) + ...
    leibniz_series = [((-1) ** k) / (2 * k + 1) for k in range(n_terms)]

    total = sum(leibniz_series)
    pi_approx = 4 * total
    return pi_approx
