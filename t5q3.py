# پیاده‌سازی کلاس آقای خرچنگ
class MrKrabs:
    def init(self, data):
        self.data = data

    def process_data(self):
        # الگوریتم تغییر tt به o
        processed_data = self.data.replace("tt", "o")
        return processed_data[-10:] + processed_data

# پیاده‌سازی کلاس باب اسفنجی
class SpongeBob:
    def init(self, data):
        self.data = data

    def process_data(self):
        # الگوریتم مرتب‌سازی صعودی
        sorted_data = self.merge_sort(self.data)
        return sorted_data

    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

# پیاده‌سازی کلاس اختاپوس
class Squidward:
    def init(self, data):
        self.data = data

    def process_data(self):
        # الگوریتم جایگزینی aaa به (0_0)
        processed_data = self.data.replace("aaa", "(0_0)")
        return processed_data

# تابع بررسی و پردازش ورودی
def process_input(input_string):
    if input_string.startswith("m"):
        mr_krabs = MrKrabs(input_string)
        return mr_krabs.process_data()
    elif input_string.startswith("sb") and input_string[2] != "b":
        sponge_bob = SpongeBob(input_string)
        return sponge_bob.process_data()
    elif input_string.startswith("s") and input_string[1] != "b":
        squidward = Squidward(input_string)
        return squidward.process_data()
    else:
        return "invalid input"

input_str = "your_input_string_here"  # ورودی خود را در اینجا قرار دهید
print(process_input(input_str))