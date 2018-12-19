def preorder_print(data: list, idx: int=0, cur_pre: str='', next_pre: str=''):
    if idx < len(data):
        print(cur_pre+str(data[idx]))
        preorder_print(data, 2*idx+1, next_pre+'|-', next_pre+'| ')
        preorder_print(data, 2*idx+2, next_pre+'|-', next_pre+'  ')


class Heap:
    def __init__(self):
        self.data = list()

    def build_from_top(self, data_list):
        for el in data_list:
            self.enqueue(el)

    def build_from_bottom(self, data_list):
        self.data = list(data_list)
        last_par = len(data_list) // 2 - 1
        par = last_par
        while par >= 0:
            self.move_down(par)
            par -= 1

    def print_heap(self):
        preorder_print(self.data)

    @staticmethod
    def _parent(i):
        if i % 2 == 0:
            return (i - 2) // 2
        else:
            return (i-1) // 2

    def _swap(self, left, right):
        self.data[left], self.data[right] = self.data[right], self.data[left]

    def enqueue(self, el):
        self.data.append(el)
        i = len(self.data) - 1
        par = self._parent(i)
        while i > 0 and el > self.data[par]:
            self._swap(i, par)
            i = par
            par = self._parent(i)

    def dequeue(self):
        el = self.data[0]
        last = len(self.data)
        self.data[0] = self.data[last]
        del self.data[last]
        self.move_down(0)
        return el

    def move_down(self, start):
        par = start
        left = par * 2 + 1
        right = par * 2 + 2
        last = len(self.data) - 1

        largest = left if self.data[left] > self.data[right] else right

        while par < last and self.data[par] < self.data[largest]:
            self._swap(par, largest)
            par = largest
            if par*2 < last:
                left = par*2+1
                right = par*2+2
                largest = left if self.data[left] > self.data[right] else right


if __name__ == '__main__':
    heap = Heap()
    heap.build_from_top([2, 8, 6, 1, 10, 15, 3, 12, 11])
    heap.print_heap()
    heap.build_from_bottom([2, 8, 6, 1, 10, 15, 3, 12, 11])
    heap.print_heap()
