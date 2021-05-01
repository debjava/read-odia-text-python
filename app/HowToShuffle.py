import random


def shuffle_1():
    test_list = [1, 4, 5, 6, 3]
    print("Original shuffled list is : " + str(test_list))
    for i in range(len(test_list) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i + 1)
        # Swap arr[i] with the element at random index
        test_list[i], test_list[j] = test_list[j], test_list[i]
    print("The shuffled list is : " + str(test_list))


def shuffle_2():
    test_list = [1, 4, 5, 6, 3]
    print("Original shuffled list is : " + str(test_list))
    random.shuffle(test_list)
    print("The shuffled list is : " + str(test_list))


def shuffle_3():
    test_list = [1, 4, 5, 6, 3]
    print("Original shuffled list is : " + str(test_list))
    res = random.sample(test_list, len(test_list))
    print("The shuffled list is : " + str(res))



if __name__ == "__main__":
    # shuffle_1()
    # shuffle_2()
    shuffle_3()
