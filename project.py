
def main():
    numInput = input('Enter number list: ')

    target = int(input('Target : '))

    data = string_to_num_list(numInput)

    print()

    print(f'IsFound: {vis(binary_search(data, target))}')

def binary_search(data, target):
    data = sorted(data)
    steps = []
    left = 0
    right = len(data) - 1

    while left <= right:
        # be aware of operator descending, it takes so long to fix
        mid = (left + right) // 2
        steps.append(mid)

        if data[mid] == target:
            break
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return data, steps, target

def vis(func):
    data, steps, target = func

    lenItem = len(str(data[-1]))

    lines = ''.join(f'{str(i).zfill(lenItem)}|' for i in data)

    stepIndex = []

    for i in steps:
        if i == 0:
            stepIndex.append(lenItem - 1)
        else:
            stepIndex.append((i * (lenItem + 1)) + 1)
        
    plain = []
    order = []

    for i in range(len(lines)):
        if i in stepIndex:
            plain.append('V')
            order.append(str(stepIndex.index(int(i)) + 1))
        else:
            plain.append(' ')
            order.append(' ')

    print(''.join(order))
    print(''.join(plain))
    print(lines)
    print()

    return target in data

def string_to_num_list(numInput: str):
    numInput = list(map(lambda x: int(x), numInput.split(',')))
    return sorted(numInput)

if __name__ == "__main__":
    main()