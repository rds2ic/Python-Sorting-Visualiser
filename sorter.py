from random import randint
import pygame

pygame.init()
WIDTH = HEIGHT = 800
FPS = 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Bar:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colour = "white"

    def draw(self, s):
        pygame.draw.rect(s, self.colour, self.rect)
        # Border Lines
        # pygame.draw.rect(s, "black", pygame.Rect(
        #     self.x-1, self.y, 1, self.height+1))
        # pygame.draw.rect(s, "black", pygame.Rect(
        #     self.x+self.width, self.y, 1, self.height+1))
        # pygame.draw.rect(s, "black", pygame.Rect(
        #     self.x, self.y+self.height, self.width, 1))

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def update_height(self, height, s):
        # pygame.draw.rect(s, "white", self.rect)
        # pygame.draw.rect(s, "white", pygame.Rect(
        #     self.x-1, self.y, 1, self.height+1))
        # pygame.draw.rect(s, "white", pygame.Rect(
        #     self.x+self.width, self.y, 1, self.height+1))
        # pygame.draw.rect(s, "white", pygame.Rect(
        #     self.x, self.y+self.height, self.width, 1))
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def return_height(self):
        return self.height

    def is_checking(self):
        self.colour = "green"

    def is_checked(self):
        self.colour = "white"

    def is_pointer(self):
        self.colour = "red"


class BarGrid:
    def __init__(self, num_of_bars):
        self.num_of_bars = num_of_bars
        self.width = WIDTH // num_of_bars
        self.bars = [
            Bar(self.width, randint(1, 600), i * self.width, 0)
            for i in range(len(self))
        ]

    def draw(self, s):
        for bar in self.bars:
            bar.draw(s)

    def __len__(self):
        return self.num_of_bars

    def return_values(self):
        arr = [self.bars[i].return_height() for i in range(len(self))]
        return arr

    def randomise(self, s):
        for i in range(self.num_of_bars):
            self.bars[i] = Bar(self.width, randint(1, 600), i * self.width, 0)
            update_display(s, self)

    def bubble_sort(self, s):
        for i in range(len(self)):
            j = 0
            while j < len(self) - 1:
                self.bars[j].is_checking()
                self.bars[j + 1].is_checking()
                num1_checking = self.bars[j].return_height()
                num2_checking = self.bars[j + 1].return_height()
                if num1_checking > num2_checking:
                    holder = num1_checking
                    self.bars[j].update_height(num2_checking, s)
                    self.bars[j + 1].update_height(holder, s)
                    update_display(s, self)

                self.bars[j].is_checked()
                self.bars[j + 1].is_checked()
                j += 1

    def quick_sort(self, s):
        """arr = [3, 8, 1, 9, 4, 2]

        def partition(array, start=0, end=0):
            # print(arr)
            # print(f'Start:{start}')
            # print(f'End:{end}')
            i = start
            pivot = array[end]
            # print(f'Pivot:{pivot}')
            for j in range(start, end+1):
                if array[j] < pivot:
                    holder = array[j]
                    array[j] = array[i]
                    array[i] = holder
                    i += 1

            array[end] = array[i]
            array[i] = pivot

            start1 = start
            end1 = i-1
            start2 = i+1
            end2 = end

            # print(array)
            # print(f'Start1:{start1}')
            # print(f'End1:{end1}')
            # print(f'Start2:{start2}')
            # print(f'End2:{end2}')
            # print()

            if (end1 - start1) > 0:
                partition(array, start1, end1)
            if (end2 - start2) > 0:
                partition(array, start2, end2)

        partition(arr, 0, len(arr)-1)"""

        def partition(array, start=0, end=0):
            i = start
            pivot = array[end]
            pivot.is_pointer()
            j = 0
            for j in range(start, end + 1):
                array[i].is_checking()
                array[j].is_checking()
                update_display(s, self)
                if array[j].return_height() < pivot.return_height():
                    holder1 = array[i].return_height()
                    holder2 = array[j].return_height()
                    array[j].update_height(holder1, s)
                    array[i].update_height(holder2, s)
                    array[i].is_checked()
                    update_display(s, self)
                    i += 1
                array[j].is_checked()
            array[i].is_checked()
            array[j].is_checked()

            holder1 = array[i].return_height()
            holder2 = array[end].return_height()
            array[end].update_height(holder1, s)
            array[i].update_height(holder2, s)
            update_display(s, self)
            start1 = start
            end1 = i - 1
            start2 = i + 1
            end2 = end

            if (end1 - start1) > 0:
                partition(array, start1, end1)
            if (end2 - start2) > 0:
                partition(array, start2, end2)

        partition(self.bars, 0, len(self.bars) - 1)

    def merge_sort(self, s):
        """arr = [1, 7, 8, 5, 4, 2, 6, 3, 9]
            # after i/j becomes 4 make it auto add the rset of the other array.


            def partition(array, start, end, parent_start, parent_end):
                # print(f'Array: {array[start:end+1]},Start:{start},End:{end},Parent Array:{array[parent_start:parent_end+1]}, Parent Start:{parent_start}, Parent End:{parent_end}')
                # a = input()
                if (end-start) > 0:
                    # print("partitionLeft")
                    partition(array, start, ((end + start + 1) // 2) -
                            1, start, end)
                    # print("partitionRight")
                    partition(array, ((end + start + 1) // 2),
                            end, start, end)
                if end == parent_end:
                    # print('merge')
                    merge(parent_start, start, end+1, array)


            def merge(start, mid, end, arr_main):
                if start == mid:
                    return
                # print(f'start:{start} mid:{mid} end:{end}')
                # print(f'Array1:{arr_main[start:mid]},Array2:{arr_main[mid:end]}')
                arr_main_copy = arr_main[:]
                i = 0
                j = 0
                count = 0
                holder = arr_main[start+count]
                # print(mid-start, end-mid)
                while (i < mid-start and j < end-mid) and count < end-start:
                    # print(f'i:{i} j:{j} count: {count}')
                    # print(arr_main_copy[start+i], arr_main_copy[mid+j])
                    # print(arr_main_copy[start+count])
                    if arr_main_copy[start+i] < arr_main_copy[mid+j]:
                        # print(f'{arr_main[start+i]} goes through')
                        if arr_main_copy[mid+j] > holder:
                            holder = arr_main_copy[mid+j]
                        arr_main[start+count] = arr_main_copy[start+i]
                        i += 1
                    else:
                        # print(f'{arr_main[mid+j]} goes through')
                        if arr_main_copy[start+i] > holder:
                            holder = arr_main_copy[start+i]
                        arr_main[start+count] = arr_main_copy[mid+j]
                        j += 1
                    count += 1
                    # print(f'holder:{holder}')
                    # print(arr_main_copy[start:mid], arr_main_copy[mid:end])
                    # print(arr_main[start:end])
                if i > j:
                    arr_main[start+count] = holder
                else:
                    arr_main[start+count] = holder
                while i < mid - start:
                    arr_main[start+count] = arr_main_copy[start+i]
                    i += 1
                    count += 1
                while j < end - mid:
                    arr_main[start+count] = arr_main_copy[mid+j]
                    j += 1
                    count += 1
                # print(f'i:{i} j:{j} count: {count}')
                # print(arr_main_copy[start], arr_main_copy[mid])
                # print(arr_main[start:end])


        partition(arr, 0, len(arr)-1, 0, len(arr)-1)"""

        def partition(array, start, end, parent_start, parent_end):
            if (end - start) > 0:
                partition(array, start, ((end + start + 1) // 2) - 1, start, end)
                partition(array, ((end + start + 1) // 2), end, start, end)
            if end == parent_end:
                merge(parent_start, start, end + 1, array)

        def merge(start, mid, end, arr_main):
            if start == mid:
                return
            arr_main_copy = self.return_values()
            i = 0
            j = 0
            count = 0
            while (i < mid - start and j < end - mid) and count < end - start:
                # arr_main[start+i].is_checking()
                # arr_main[mid+j].is_checking()
                update_display(s, self)
                if arr_main_copy[start + i] < arr_main_copy[mid + j]:
                    arr_main[start + count].update_height(arr_main_copy[start + i], s)
                    # arr_main[start+i-1].is_checked()
                    # arr_main[mid+j].is_checked()
                    i += 1
                else:
                    arr_main[start + count].update_height(arr_main_copy[mid + j], s)
                    # arr_main[start+i].is_checked()
                    # arr_main[mid+j-1].is_checked()
                    j += 1
                count += 1
                update_display(s, self)

                update_display(s, self)
            while i < mid - start:
                arr_main[start + count].update_height(arr_main_copy[start + i], s)
                i += 1
                count += 1
                update_display(s, self)
            while j < end - mid:
                arr_main[start + count].update_height(arr_main_copy[mid + j], s)
                j += 1
                count += 1
                update_display(s, self)

        partition(self.bars, 0, len(self.bars) - 1, 0, len(self.bars) - 1)

    def insert_sort(self, s):
        """arr = [12, 11, 13, 5, 6]
        print(arr)
        for i, v in enumerate(arr):
            # print(i, v)
            if i == len(arr) - 1:
                break
            if v > arr[i+1]:
                print(arr)
                arr[i] = arr[i+1]
                arr[i+1] = v
                print(arr)
                j = i
                while j > 0 and arr[j] < arr[j-1]:
                    holder = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = holder
                    print(arr)
                    j -= 1"""

        for i, v in enumerate(self.bars):
            if i == len(self) - 1:
                break
            if v.return_height() > self.bars[i + 1].return_height():
                holder1 = v.return_height()
                self.bars[i].is_checking()
                self.bars[i + 1].is_checking()
                update_display(s, self)
                self.bars[i].update_height(self.bars[i + 1].return_height(), s)
                self.bars[i + 1].update_height(holder1, s)
                update_display(s, self)
                self.bars[i].is_checked()
                self.bars[i + 1].is_checked()
                update_display(s, self)
                j = i
                while (
                    j > 0
                    and self.bars[j].return_height() < self.bars[j - 1].return_height()
                ):
                    self.bars[j].is_pointer()
                    update_display(s, self)
                    holder2 = self.bars[j].return_height()
                    self.bars[j].update_height(self.bars[j - 1].return_height(), s)
                    self.bars[j - 1].update_height(holder2, s)
                    self.bars[j].is_checked()
                    update_display(s, self)
                    j -= 1

    def selection_sort(self, s):
        """
        arr = [64, 25, 12, 22, 11]
        minElement = float('inf')
        pos = 0
        j = 0
        while j < len(arr) - 1:
            print(f'j:{j}')
            print(f'J array{arr[:]}')
            for i, v in enumerate(arr[j:]):
                print(i+j)
                if v < minElement:
                    minElement = v
                    pos = i + j
            print(f'Pos:{pos}, Min:{minElement}')
            holder = arr[j]
            arr[j] = arr[pos]
            arr[pos] = holder
            minElement = float('inf')

            j += 1

        """
        minElement = float("inf")
        pos = 0
        j = 0
        while j < len(self) - 1:
            for i, v in enumerate(self.bars[j:]):
                if v.return_height() < minElement:
                    if minElement != float("inf"):
                        self.bars[pos].is_checked()
                    minElement = v.return_height()
                    pos = i + j
                    self.bars[pos].is_checked()
                    update_display(s, self)
            self.bars[pos].is_checking()
            holder = self.bars[j]
            holder_height = holder.return_height()
            holder.is_checking()
            update_display(s, self)
            self.bars[j].update_height(self.bars[pos].return_height(), s)
            self.bars[pos].update_height(holder_height, s)
            update_display(s, self)
            self.bars[pos].is_checked()
            holder.is_checked()
            minElement = float("inf")
            update_display(s, self)

            j += 1


def update_display(s, b):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    s.fill("black")
    b.draw(s)
    clock.tick(FPS)
    pygame.display.update()


def main():
    bars = BarGrid(200)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bars.randomise(screen)
                elif event.key == pygame.K_0:
                    bars.bubble_sort(screen)
                elif event.key == pygame.K_1:
                    bars.quick_sort(screen)
                elif event.key == pygame.K_2:
                    bars.merge_sort(screen)
                elif event.key == pygame.K_3:
                    bars.insert_sort(screen)
                elif event.key == pygame.K_4:
                    bars.selection_sort(screen)
        update_display(screen, bars)


if __name__ == "__main__":
    main()
