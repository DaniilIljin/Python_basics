"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if s == '':
        return ''
    elif len(s) == 1:
        return s.capitalize()
    else:
        return s[0].capitalize() + s[1:]


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times.

    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if nums.count(7) == 3:
        list_of_truth = []
        for index, element in enumerate(nums):
            if index != 0 and index != len(nums) - 1:
                if element != nums[index - 1] and element != nums[index + 1]:
                    list_of_truth.append(1)
        return len(list_of_truth) == len(nums) - 2
    else:
        return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], [], []]
    """
    if not initial_list:
        list_of_lists = []
        for i in range(amount):
            list_of_lists.append([])
        return list_of_lists
    else:
        final_list = [initial_list]
        for i in range(amount - 1):
            final_list.append([])
        counter = 0
        for rep in range(len(final_list) - 1):
            one_of_lists = []
            dict_with_indexes = {}
            one_of_lists.extend(final_list[counter])
            for index, element in enumerate(one_of_lists):
                if index + 1 + factor <= len(one_of_lists):
                    dict_with_indexes[index + factor] = element
                elif index + 1 + factor > len(one_of_lists):
                    needed_to_be_skipped = (index + 1 + factor) // len(one_of_lists)
                    new_index = index + factor - len(one_of_lists) * needed_to_be_skipped
                    dict_with_indexes[new_index] = element
            counter += 1
            for element1 in sorted(dict_with_indexes):
                final_list[counter].append(dict_with_indexes[element1])
    return final_list


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    calls = call_log.split(',')
    final_dict = {}
    for element in calls:
        caller_and_others = element.split(':')
        for index, person in enumerate(caller_and_others):
            if index != len(caller_and_others) - 1:
                if person in final_dict:
                    final_dict[person] += [caller_and_others[index + 1]]
                else:
                    final_dict[person] = [caller_and_others[index + 1]]
    for person in final_dict:
        final_dict[person] = list(set(final_dict[person]))
    return final_dict
