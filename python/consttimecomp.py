def equal(a, b):
    """Return ``a == b`` using an approach resistant to timing analysis.

    a and b must both be of the same type: either both text strings,
    or both byte strings.

    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b, but not their values.
    """
    # For a similar approach, see
    # http://codahale.com/a-lesson-in-timing-attacks/
    for T in (bytes, unicode):
        if isinstance(a, T) and isinstance(b, T):
            break
    else:  # for...else
        raise TypeError("arguments must be both strings or both bytes")
    if len(a) != len(b):
        return False
    result = True
    for x, y in zip(a, b):
        # VERY IMPORTANT: do **not** short-cut early. It is vital
        # that all comparisons take the same amount of time.
        result &= (x == y)
    return result
