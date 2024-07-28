
marks = [38, 41, 36, 31, 45, 38, 27, 32, 29, 39]


def calculate_mean(marks_list):
    return sum(marks_list) / len(marks_list)


mean_original = calculate_mean(marks)
print(f"(a) The mean of their marks: {mean_original}")

marks_increased_by_2 = [mark + 2 for mark in marks]
mean_increased_by_2 = calculate_mean(marks_increased_by_2)
print(f"(b) The mean of their marks when increased by 2: {mean_increased_by_2}")


marks_deducted_by_1 = [mark - 1 for mark in marks]
mean_deducted_by_1 = calculate_mean(marks_deducted_by_1)
print(f"(c) The mean of their marks when deducted by 1: {mean_deducted_by_1}")


marks_halved = [mark / 2 for mark in marks]
mean_halved = calculate_mean(marks_halved)
print(f"(d) The mean of their marks when halved: {mean_halved}")
