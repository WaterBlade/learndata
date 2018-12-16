from typing import List


class Custom:
    def __init__(self, name: str):
        self.name = name  # type: str
        self.flight_list = list()

    def __repr__(self):
        return self.name

    def book(self, flight):
        self.flight_list.append(flight)

    def cancel(self, flight):
        self.flight_list.remove(flight)

    def print_flight(self):
        for f in self.flight_list:
            print('  *' + str(f))


class Flight:
    def __init__(self, id_: str, capacity: int):
        self.id_ = id_  # type: str
        self.capacity = capacity  # type: str
        self.custom_list = list()  # type: List[Custom]

    def __repr__(self):
        return self.id_

    def book(self, custom: Custom)->bool:
        if custom in self.custom_list:
            return False
        else:
            self.custom_list.append(custom)
            custom.book(self)
            return True

    def cancel(self, custom):
        if custom in self.custom_list:
            self.custom_list.remove(custom)
            custom.cancel(self)
            return True
        else:
            return False

    def print_custom(self):
        for c in self.custom_list:
            print('  *'+str(c))


class BookCenter:
    def __init__(self):
        self.custom_list = list()  # type: List[Custom]
        self.flight_list = list()  # type: List[Flight]

    def search_flight(self, flight_id: str)->Flight:
        for f in self.flight_list:
            if f.id_ == flight_id:
                return f
        return None

    def search_custom(self, custom_name: str)->Custom:
        for c in self.custom_list:
            if c.name == custom_name:
                return c
        return None

    def book(self, flight_id, custom_name):
        flight = self.search_flight(flight_id)
        custom = self.search_custom(custom_name)
        if flight is None:
            flight = Flight(flight_id, 100)
            self.flight_list.append(flight)
        if custom is None:
            custom = Custom(custom_name)
            self.custom_list.append(custom)

        flight.book(custom)

    def cancel(self, flight_id, custom_name):
        flight = self.search_flight(flight_id)
        custom = self.search_custom(custom_name)
        if flight is not None and custom is not None:
            flight.cancel(custom)
            if len(custom.flight_list) == 0:
                self.custom_list.remove(custom)

    def print_flight_custom_booked(self, name):
        c = self.search_custom(name)
        if c is not None:
            print('Flight booked by %s' % c)
            c.print_flight()
        else:
            print('Cannot Find %s' % name)

    def print_custom_in_flight(self, flight):
        f = self.search_flight(flight)
        if f is not None:
            print('Custom in flight %s' % f)
            f.print_custom()
        else:
            print('Cannot Find %s' % flight)

    def run(self):
        while True:
            print('请选择需要的服务：')
            print('1.预定机票')
            print('2.取消预定机票')
            print('3.查询顾客所预定的所有机票')
            print('4.查询航班的所有乘客')
            i = input('请输入选项数字或退出[quit]：')
            if i == 'quit':
                break
            else:
                i = int(i)
            if i == 1:
                flight = input('请输入航班号：')
                name = input('请输入顾客名字：')
                self.book(flight, name)
            elif i == 2:
                flight = input('请输入航班号：')
                name = input('请输入顾客名字：')
                self.cancel(flight, name)
            elif i == 3:
                name = input('请输入顾客名字：')
                self.print_flight_custom_booked(name)
            elif i == 4:
                flight = input('请输入航班号：')
                self.print_custom_in_flight(flight)


if  __name__ == '__main__':
    BookCenter().run()