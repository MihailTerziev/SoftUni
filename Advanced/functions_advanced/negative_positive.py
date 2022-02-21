def negative_vs_positive(*args):
    pos_sum, neg_sum = 0, 0

    for i in args:
        for n in i:
            if n < 0:
                neg_sum += n
            else:
                pos_sum += n

    return pos_sum, neg_sum


numbers = [int(x) for x in input().split()]

positive, negative = negative_vs_positive(numbers)
print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
