if __name__ == "__main__":
    input_file = 'day1_input_file.txt'

    with open(input_file) as f:
        left_nums = []
        right_nums = []
        for num in f.read().splitlines():
            nums = num.split()
            left_nums.append(int(nums[0]))
            right_nums.append(int(nums[1]))

        left_nums.sort()
        right_nums.sort()

        diff_of_nums = []

        print(left_nums)
        print(right_nums)

        for a, b in zip(left_nums, right_nums):
            diff_of_nums.append(abs(a - b))

        print(diff_of_nums)

        total_diff_sum = sum(diff_of_nums)
        # part 1 answer
        print(str(total_diff_sum))

        sim_list = []

        for i in left_nums:
            count = right_nums.count(i)
            sim_list.append(i * count)

        print(sim_list)

        # part 2 answer
        print(str(sum(sim_list)))




