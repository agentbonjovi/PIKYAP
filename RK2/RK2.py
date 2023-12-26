from operator import itemgetter

class Brau:
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.size = size
        self.comp_id = comp_id

class Comp:
    def __init__(self, brau_id, name):
        self.id = brau_id
        self.name = name

class ComBra:
    def __init__(self, comp_id, brau_id):
        self.comp_id = comp_id
        self.brau_id = brau_id

def get_one_to_many(brausers, computers):
    return [(b.name, b.size, c.name)
            for b in brausers
            for c in computers
            if b.comp_id == c.id
            ]

def get_many_to_many(brausers, computers, comps_braus):
    many_to_many_temp = [(c.name, cb.comp_id, cb.brau_id)
                         for c in computers
                         for cb in comps_braus
                         if c.id == cb.comp_id
                         ]
    return [(b.name, b.size, comp_name)
            for comp_name, comp_id, brau_id in many_to_many_temp
            for b in brausers if b.id == brau_id
            ]

def filter_brau_names_by_computer(computer_name, many_to_many):
    return list(filter(lambda i: i[2] == computer_name, many_to_many))

def calculate_average_sizes(computer, many_to_many):
    c_braus = filter_brau_names_by_computer(computer.name, many_to_many)
    if len(c_braus) > 0:
        c_sizes = [size for _, size, _ in c_braus]
        c_sizes_sum = sum(c_sizes)
        k = len(c_sizes)
        return c_sizes_sum / k
    return None

def get_task_D1_result(one_to_many):
    return [(brau[0], brau[2]) for brau in one_to_many if brau[0][-1] == 'a']

def get_task_D2_result(computers, many_to_many):
    res_2_unsorted = []
    for c in computers:
        avg_size = calculate_average_sizes(c, many_to_many)
        if avg_size is not None:
            res_2_unsorted.append((c.name, avg_size))
    return sorted(res_2_unsorted, key=itemgetter(1), reverse=True)

def get_task_D3_result(computers, many_to_many):
    res_3 = {}
    for c in computers:
        if 'msi' in c.name:
            c_braus = filter_brau_names_by_computer(c.name, many_to_many)
            c_braus_names = [x for x, _, _ in c_braus]
            res_3[c.name] = c_braus_names
    return res_3

if __name__ == '__main__':
    computers = [
        Comp(1, 'macintosh'),
        Comp(2, 'dell'),
        Comp(3, 'ibm'),
        Comp(4, 'toshiba'),
        Comp(5, 'msi')
    ]

    brausers = [
        Brau(1, 'safari', 173, 1),
        Brau(2, 'chrome', 140, 2),
        Brau(3, 'mozilla', 97, 3),
        Brau(4, 'Opera', 201, 4),
        Brau(5, 'Edge', 50, 5)
    ]

    comps_braus = [
        ComBra(1, 1),
        ComBra(1, 2),
        ComBra(2, 2),
        ComBra(2, 4),
        ComBra(3, 3),
        ComBra(4, 2),
        ComBra(4, 4),
        ComBra(5, 2),
        ComBra(5, 3),
        ComBra(5, 4)
    ]

    one_to_many = get_one_to_many(brausers, computers)
    many_to_many = get_many_to_many(brausers, computers, comps_braus)

    print('Задание Д1')
    result_D1 = get_task_D1_result(one_to_many)
    print(result_D1)

    print('Задание Д2')
    result_D2 = get_task_D2_result(computers, many_to_many)
    print(result_D2)

    print('Задание Д3')
    result_D3 = get_task_D3_result(computers, many_to_many)
    print(result_D3)
