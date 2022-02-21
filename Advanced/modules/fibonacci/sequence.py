def create_seq(number: int):
    sequence = [0, 1]
    for _ in range(3, number+1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def locate(number: int, sequence):
    if number in sequence:
        print(f"The number - {number} is at index {sequence.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")
