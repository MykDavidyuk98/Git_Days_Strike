def multiply_array(array: list) -> None:
    for i in range(len(array)):
        for k in range(len(array)):
            print(f'Множення числа {array[i]} на число {array[k]}: {array[i] * array[k]}')