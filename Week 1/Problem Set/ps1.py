###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    def value_of_trip(trip):
        value = 0
        for el in trip:
            value += el.__getitem__(1)
        return value

    trips = []
    cows_copy = cows.copy()
    cows_copy = [(name, cows_copy[name]) for name in sorted(cows_copy, key=cows_copy.get, reverse=True)]

    while len(cows_copy) > 0:
        # Make trip
        trip = []
        weight = 0
        for el in cows_copy[:]:
            if weight + el.__getitem__(1) <= limit:
                weight += el.__getitem__(1)
                trip.append(el.__getitem__(0))
                cows_copy.remove(el)
        trips.append(trip)

    return trips


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    def evaluate_trips_weight(trips, dictionary, max):
        n_trips = 0
        total_weight = 0
        band = True
        for trip in trips:
            n_trips += 1
            weight = 0
            for cow in trip:
                weight += dictionary[cow]
                if weight > max:
                    band = False
            total_weight += weight
        if band:
            return trips, n_trips, total_weight
        else:
            return None

    cows_copy = cows.copy()
    combinations = []
    # Remove the overweight trips
    for combination in get_partitions([name for name in cows_copy.keys()]):
        aux = evaluate_trips_weight(combination, cows_copy, limit)
        if aux is not None:
            combinations.append(combination)
    best_answer = combinations[0]
    best_tuple = evaluate_trips_weight(combinations[0], cows_copy, limit)
    # Find the best one
    for combination in combinations:
        aux = evaluate_trips_weight(combination, cows_copy, limit)
        if aux[1] <= best_tuple[1] and aux[2] >= best_tuple[2]:
            best_answer = combination
            best_tuple = aux
    return best_answer


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    start = time.time()
    ans = greedy_cow_transport(cows, limit)    
    end = time.time()
    print('Greedy time:', end - start)
    print('Greedy n trips:', len(ans))

    print('')

    start = time.time()
    ans = brute_force_cow_transport(cows, limit)
    end = time.time()
    print('Brute time:', end - start)
    print('Brute n trips:', len(ans))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# limit = 100
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()