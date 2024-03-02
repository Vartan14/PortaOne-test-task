"""
The fastest solution using pandas
"""
import time
import pandas as pd

"""
Завдання - знайти наступні чотири/шість значень:
    1. максимальне число в файлі;
    2. мінімальне число в файлі;
    3. медіану ( https://goo.gl/hiCwVw );
    4. середнє арифметичне значення ( https://goo.gl/XJeAjZ );
    5*. найбільшу послідовність чисел (які ідуть один за одним), яка збільшується (опціонально)
    6*. найбільшу послідовність чисел (які ідуть один за одним), яка зменьшується (опціонально))
"""


class FindLongestSequenceMethods:
    """Provide methods to find the longest increasing and decreasing sequences"""

    def __init__(self):
        self.arr = None

    def longest_increasing_sequence(self):
        """Find the longest increasing sequence"""
        return self.__find_sequence(is_increasing=True)

    def longest_decreasing_sequence(self):
        """Find the longest decreasing sequence"""
        return self.__find_sequence(is_increasing=False)

    def __find_sequence(self, is_increasing: bool) -> []:
        """Find the first longest sequence of increasing or decreasing numbers"""
        # Empty list
        if not self.arr:
            return []

        # Initialize the longest sequence
        longest_seq = [self.arr[0]]
        # Initialize current sequence
        current_seq = [self.arr[0]]

        # The compare function depending on we find increasing or decreasing sequence
        compare_func = lambda a, b: a > b if is_increasing else a < b

        # Looping through the list
        for num in self.arr[1:]:

            # Check whether a number continues the sequence
            if compare_func(num, current_seq[-1]):
                # Adding number to sequence
                current_seq.append(num)

                # Check the current sequence is longer than the longest one
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq[:]
            else:
                # Start the new sequence
                current_seq = [num]

        return longest_seq


class PandasStatistics(FindLongestSequenceMethods):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        self.df = self.__get_data_frame()
        self.arr = list(self.df.value)

    def __get_data_frame(self) -> pd.DataFrame:
        """Get DataFrame from file"""
        return pd.read_csv(self.file_name, header=None, names=['value'])

    def print_statistics(self):
        """Print statistics"""
        start_time = time.time()

        # Знаходження максимального числа
        max_value = self.df.max().values[0]
        print("1. Максимальне число:", max_value)

        # Знаходження мінімального числа
        min_value = self.df.min().values[0]
        print("2. Мінімальне число:", min_value)

        # Медіана
        median = self.df.median().values[0]
        print("3. Медіана:", median)

        # Середнє арифметичне
        mean = self.df.mean().values[0]
        print("4. Середнє арифметичне", mean)

        # Найдовша зростаюча послідовність
        longest_increasing_seq = self.longest_increasing_sequence()
        print("5. Найдовша зростаюча послідовність:", longest_increasing_seq)
        #
        # Найдовша спадаюча послідовність
        longest_decreasing_seq = self.longest_decreasing_sequence()
        print("6. Найдовша спадаюча послідовність:", longest_decreasing_seq)

        print('Time:', round(time.time() - start_time, 5))


if __name__ == '__main__':
    solution = PandasStatistics(file_name="data/10m.txt")
    solution.print_statistics()
