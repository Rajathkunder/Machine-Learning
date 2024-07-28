#median
def median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

# compute Q1 and Q3
def quartiles(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid + 1:]
    q1 = median(lower_half)
    q3 = median(upper_half)
    return q1, q3


data = []
for i in range(10):
    k = int(input(f"Enter number {i+1}: "))
    data.append(k)


sorted_data = sorted(data)


min_value = min(sorted_data)
max_value = max(sorted_data)


q1, q3 = quartiles(sorted_data)


med = median(sorted_data)


five_number_summary = {
    'Minimum': min_value,
    'Q1': q1,
    'Median': med,
    'Q3': q3,
    'Maximum': max_value
}


iqr = q3 - q1


lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = [x for x in sorted_data if x < lower_bound or x > upper_bound]


print("\nSorted Data:", sorted_data)
print("Five-Number Summary:", five_number_summary)
print("Interquartile Range (IQR):", iqr)
print("Outliers:", outliers)
