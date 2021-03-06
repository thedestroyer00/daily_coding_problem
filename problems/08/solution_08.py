def coding_problem_08(bt):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes have the same value.
    Given the root to a binary tree, count the number of unival subtrees.
    Example:

    >>> btree = (0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))
    >>> coding_problem_08(btree)
    6
    """
    def unival_count(btree):

        val, ln, rn = btree
        if ln is None and rn is None:  # leaf case
            return 1, True, val

        lcount, is_uni_l, lval = unival_count(ln)
        rcount, is_uni_r, rval = unival_count(rn)

        is_unival = is_uni_l and is_uni_r and val == lval and val == rval
        count = lcount + rcount + is_unival
        return count, is_unival, val

    return unival_count(bt)[0]


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
