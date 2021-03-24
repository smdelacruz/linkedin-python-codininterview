import time

# Modify the following function:
def appears_twice(given_list):
    """
    My solution
    """
    placeholder = []
    for name in given_list:
        if name not in placeholder:
            placeholder.append(name)
        else:
            return name
    return None


def appears_twice(given_list):
    """
    CS Dojo solution
    """
    start = time.time()
    name_dict = {}
    for name in given_list:
        if name in name_dict:
            print(time.time() - start)
            return name
        else:
            name_dict[name] = 1
    print(time.time() - start)
    return ''


print(appears_twice(['George', 'Tom', 'Emily', 'Jenny', 'Tom']))
print(appears_twice(['George', 'Claire', 'Tom', 'Lynda', 'George']))