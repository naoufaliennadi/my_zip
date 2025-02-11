from unittest import TestCase, main
from my_zip import my_zip


class test_my_zip(TestCase):
    def test_empty(self):
        self.assertEqual(list(my_zip()),[])
        self.assertEqual(list(my_zip([])),[])
        self.assertEqual(list(my_zip((),())),[])

    def test_one(self):
        self.assertEqual(list(my_zip([2,3])), [(2,), (3,)])
        self.assertEqual(list(my_zip((2, 3), (4, 5), (6, 7))), [(2, 4, 6), (3, 5, 7)])

    def test_two(self):
        self.assertEqual(list(my_zip([2, 3, 4], [5, 6, 7])), [(2, 5), (3, 6), (4, 7)])
        self.assertEqual(list(my_zip([2, 3, 4], [5, 6, 7])), [(2, 5), (3, 6), (4, 7)])

    def test_three(self):
        self.assertEqual(list(my_zip([1,2,3],[4,5,6],[7,8,9])), [(1, 4, 7), (2, 5, 8), (3, 6, 9)])
        self.assertEqual(list(my_zip([1],[2],[3])),[(1, 2, 3)])


if __name__ == "__main__":
    main()
