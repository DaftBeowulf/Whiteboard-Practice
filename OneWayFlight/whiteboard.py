def reconstructTrip(tickets):
    dct = {}
    result = []
    # step 1: store all entries into dict for instant lookup
    for index, ticket in enumerate(tickets):
        if ticket[0] == None:  # first ticket
            result.append(ticket[1])
        # create table entry where k:p equals depart:arrive
        dct[ticket[0]] = ticket[1]

    # step 2: starting with verified first ticket, add chain of arrivals into result
    # by linking depart:arrive kvp's in dict
    curr_ticket = result[0]
    while dct[curr_ticket] != None:
        result.append(dct[curr_ticket])
        curr_ticket = dct[curr_ticket]

    return result


ticketsArr = [
    ['PIT', 'ORD'],
    ['XNA', 'CID'],
    ['SFO', 'BHM'],
    ['FLG', 'XNA'],
    [None, 'LAX'],
    ['LAX', 'SFO'],
    ['CID', 'SLC'],
    ['ORD', None],
    ['SLC', 'PIT'],
    ['BHM', 'FLG'],
]

reconstructTrip(ticketsArr)
# Your function should output an array with the route of your trip. For the above example, it should look like this:
# ['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD']
