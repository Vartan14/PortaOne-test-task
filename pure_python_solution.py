"""
Solution without using any Python libraries and built-in functions like min(), max(), sum(), sorted() etc.
"""
import time

from pandas_solution import FindLongestSequenceMethods


class Statistics(FindLongestSequenceMethods):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

        self.arr = self.__get_numbers()
        self.n = len(self.arr)

    def __get_numbers(self) -> []:
        """Read numbers from file and return list of numbers"""
        with open(self.file_name) as file:
            text = file.readlines()

        return [int(number) for number in text]

    def get_max_value(self) -> int:
        """Find the maximum value in the list"""
        return self.__find_extremum_value(is_maximum=True)

    def get_min_value(self) -> int:
        """Find the minimum value in the list"""
        return self.__find_extremum_value(is_maximum=False)

    def __find_extremum_value(self, is_maximum: bool) -> int | None:
        """Find the extremum value"""
        # Empty list
        if not self.arr:
            return None

        # The compare function depending on we find max or min value
        compare_func = lambda x, y: x > y if is_maximum else x < y

        # Initialize extremum value
        extremum_value = self.arr[0]

        # Looping through the list
        for num in self.arr[1:]:

            # Check whether a number is bigger (or less) than current extremum value
            if compare_func(num, extremum_value):
                # Update extremum value
                extremum_value = num

        return extremum_value

    def get_median(self) -> float | None:
        """Find the median of the list"""
        # Empty list
        if not self.arr:
            return None

        # Sort list
        sorted_arr = self.__quick_sort(self.arr)

        # Check if the number of elements is odd
        if self.n % 2 != 0:
            # Get the middle element of the list
            median = sorted_arr[self.n // 2]
        else:
            # Get 2 middle elements of the list
            median_1 = sorted_arr[self.n // 2]
            median_2 = sorted_arr[self.n // 2 - 1]

            # Find mean of 2 middle elements
            median = (median_1 + median_2) / 2

        return median

    def __quick_sort(self, arr):
        """Sort and return new list. Uses Quick Sort algorithm with O(n*log(n)) time complexity"""
        # Check that the length of the list does not exceed 1
        if len(arr) <= 1:
            # Return sorted list
            return arr
        else:
            # Partition
            # Pick the first element as pivot
            pivot = arr[0]

            # Get all elements smaller than pivot
            less_than_pivot = [x for x in arr[1:] if x <= pivot]

            # Get all elements bigger than pivot
            greater_than_pivot = [x for x in arr[1:] if x > pivot]

            # Recursive Quick Sort calls for the left and right sides of list (relative to pivot)
            return self.__quick_sort(less_than_pivot) + [pivot] + self.__quick_sort(greater_than_pivot)

    def find_mean(self):
        """Find the mean of the list"""
        # Empty list
        if not self.arr:
            return None

        # The sum of the list
        list_sum = self.__list_sum()

        # Divide the sum of the list by the number of its elements
        mean = list_sum / self.n

        return mean

    def __list_sum(self) -> int:
        """Find the sum of the list"""
        # Initialize total sum
        total = 0

        # Looping through the list
        for num in self.arr:
            # Adding the numbers
            total += num

        return total

    def print_statistics(self) -> None:
        """Print the statistics"""

        start_time = time.time()

        # Максимальне значення
        max_value = self.get_max_value()
        print("1. Максимальне число:", max_value)

        # Мінімальне значення
        min_value = self.get_min_value()
        print("2. Мінімальне число:", min_value)

        # Медіана
        median_value = self.get_median()
        print("3. Медіана:", median_value)

        # Середнє арифметичне
        mean_value = self.find_mean()
        print("4. Середнє арифметичне:", mean_value)

        # Найдовша зростаюча послідовність
        longest_increasing_seq = self.longest_increasing_sequence()
        print("5. Найдовша зростаюча послідовність:", longest_increasing_seq)

        # Найдовша спадаюча послідовність
        longest_decreasing_seq = self.longest_decreasing_sequence()
        print("6. Найдовша спадаюча послідовність:", longest_decreasing_seq)

        print(f"Time: {time.time() - start_time}")


if __name__ == '__main__':
    solution = Statistics(file_name='data/10m.txt')
    solution.print_statistics()
