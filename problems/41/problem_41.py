def coding_problem_41(flights_db, starting_airport):
    """
    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a
    starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple
    possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    Examples:

    >>> coding_problem_41([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    >>> coding_problem_41([('SFO', 'COM'), ('COM', 'YYZ')], 'COM')  # returns None

    >>> coding_problem_41([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
    ['A', 'B', 'C', 'A', 'C']

    The itinerary ['A', 'C', 'A', 'B', 'C'] is also a valid however the first one is lexicographically smaller.
    """
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
