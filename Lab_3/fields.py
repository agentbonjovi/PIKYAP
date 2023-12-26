def field(items, *args):

    assert len(args) > 0, 'Нет искомых ключей'
    if len(args) == 1:
        return [i[args[0]] for i in items if args[0] in i.keys() and i[args[0]] != None]
    return [{j:i[j] for j in args if j in i.keys() and i[j] != None} for i in items]

goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
                 {'title': 'Диван для отдыха', 'color': 'black'}]
print(field(goods, 'title'))
print(field(goods, 'title', 'price'))