import pprint
obj = {"a":[1, 2],"b":[3, 4],"c":[5, 6]}
printer = pprint.PrettyPrinter(width=20)

printer.pprint(obj)