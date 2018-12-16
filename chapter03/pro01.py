from typing import List


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
        
    def __repr__(self):
        return '%d/%d' % (self.num, self.den)


def farey(n: int)->List[Fraction]:
    farey_list = [Fraction(0, 1), Fraction(1, 1)]
    i = 1
    while i <= n:
        j = 0
        while j < len(farey_list) - 1:
            if farey_list[j].den + farey_list[j+1].den <= n:
                farey_list.insert(j+1, Fraction(farey_list[j].num + farey_list[j+1].num,
                                                farey_list[j].den + farey_list[j+1].den))
            j += 1
        i += 1
    return farey_list


if __name__ == '__main__':
    for i in range(1, 15):
        print(farey(i))

