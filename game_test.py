import unittest
from game import Table

class GameTests(unittest.TestCase):

    def test_few_mines(self):
        arr = Table.MinesPlaces(self,3,3,4)
        self.assertEqual(len(arr), 4)
        for i in range(len(arr)):
            self.assertTrue((arr[i][0] >= 0) and (arr[i][0] < 3) and (arr[i][1] >= 0) and (arr[i][1] < 3))
            for j in range(i + 1, len(arr)):
                self.assertNotEqual(arr[i],arr[j])

    def test_10mines(self):
        arr = Table.MinesPlaces(self,10,10,10)
        self.assertEqual(len(arr), 10)
        for i in range(len(arr)):
            self.assertTrue((arr[i][0] >= 0) and (arr[i][0] < 10) and (arr[i][1] >= 0) and (arr[i][1] < 10))
            for j in range(i + 1, len(arr)):
                self.assertNotEqual(arr[i],arr[j])

    def test_40mines(self):
        arr = Table.MinesPlaces(self,16,16,40)
        self.assertEqual(len(arr), 40)
        for i in range(len(arr)):
            self.assertTrue((arr[i][0] >= 0) and (arr[i][0] < 16) and (arr[i][1] >= 0) and (arr[i][1] < 16))
            for j in range(i + 1, len(arr)):
                self.assertNotEqual(arr[i],arr[j])

    def test_99mines(self):
        arr = Table.MinesPlaces(self,30,16,99)
        self.assertEqual(len(arr), 99)
        for i in range(len(arr)):
            self.assertTrue((arr[i][0] >= 0) and (arr[i][0] < 30) and (arr[i][1] >= 0) and (arr[i][1] < 16))
            for j in range(i + 1, len(arr)):
                self.assertNotEqual(arr[i],arr[j])

    def test_tiny_table(self):
        self.assertEqual(Table.TableCells(self, 3, 3, [(2,0),(1,1),(1,2)]),
                            [[1,2,'*'],[2,'*',3],[2,'*',2]])

    def test_littel_table(self):
        mines = [(6, 5), (3, 1), (8, 3), (4, 0), (3, 9), (1, 1), (8, 0), (1, 0), (3, 5), (7, 8)]
        self.assertEqual(Table.TableCells(self, 10, 10, mines),
                            [[2,'*',3,2,'*',1,0,1,'*',1],
                             [2,'*',3,'*',2,1,0,1,1,1],
                             [1,1,2,1,1,0,0,1,1,1],
                             [0,0,0,0,0,0,0,1,'*',1],
                             [0,0,1,1,1,1,1,2,1,1],
                             [0,0,1,'*',1,1,'*',1,0,0],
                             [0,0,1,1,1,1,1,1,0,0],
                             [0,0,0,0,0,0,1,1,1,0],
                             [0,0,1,1,1,0,1,'*',1,0],
                             [0,0,1,'*',1,0,1,1,1,0]])

    def test_middle_table(self):
        mines = [(13, 0), (1, 7), (13, 8), (3, 11), (0, 10), (6, 8), (10, 4), (4, 11), 
                (11, 1), (13, 2), (14, 4), (8, 2), (3, 8), (0, 1), (13, 11), (12, 8), 
                (14, 12), (14, 10), (7, 6), (12, 9), (6, 3), (15, 4), (6, 10), (14, 11), 
                (6, 12), (7, 12), (1, 9), (3, 15), (7, 1), (10, 8), (0, 4), (5, 0), 
                (15, 0), (1, 11), (3, 12), (1, 8), (2, 5), (9, 3), (5, 6), (7, 3)]
        self.assertEqual(Table.TableCells(self, 16, 16, mines),
                            [[1, 1, 0, 0, 1, '*', 2, 1, 1, 0, 1, 1, 2, '*', 2, '*'], 
                            ['*', 1, 0, 0, 1, 1, 2, '*', 2, 1, 1, '*', 3, 2, 3, 1], 
                            [1, 1, 0, 0, 0, 1, 3, 4, '*', 2, 2, 1, 2, '*', 1, 0], 
                            [1, 1, 0, 0, 0, 1, '*', '*', 3, '*', 2, 1, 1, 2, 3, 2], 
                            ['*', 2, 1, 1, 0, 1, 2, 2, 2, 2, '*', 1, 0, 1, '*', '*'], 
                            [1, 2, '*', 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 2, 2], 
                            [1, 2, 2, 1, 1, '*', 2, '*', 1, 0, 0, 0, 0, 0, 0, 0], 
                            [2, '*', 3, 1, 2, 2, 3, 2, 1, 1, 1, 2, 2, 2, 1, 0], 
                            [3, '*', 4, '*', 1, 1, '*', 1, 0, 1, '*', 3, '*', '*', 1, 0], 
                            [3, '*', 3, 1, 1, 2, 2, 2, 0, 1, 1, 3, '*', 4, 2, 1], 
                            ['*', 3, 3, 2, 2, 2, '*', 1, 0, 0, 0, 1, 2, 4, '*', 2], 
                            [2, '*', 3, '*', '*', 3, 3, 3, 1, 0, 0, 0, 1, '*', '*', 3], 
                            [1, 1, 3, '*', 3, 2, '*', '*', 1, 0, 0, 0, 1, 3, '*', 2], 
                            [0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 1, 1, 1], 
                            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 1, '*', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    def test_big_table(self):
        mines = [(15, 10), (20, 0), (9, 15), (26, 6), (23, 11), (24, 6), (18, 6), (6, 15), (22, 6), (11, 9), 
                (21, 7), (8, 0), (16, 1), (23, 9), (18, 9), (17, 12), (6, 7), (13, 5), (11, 13), (10, 13), 
                (3, 13), (10, 6), (7, 7), (12, 7), (3, 9), (3, 6), (27, 7), (8, 14), (9, 2), (6, 0), 
                (14, 1), (23, 3), (27, 4), (9, 11), (15, 5), (16, 3), (26, 12), (29, 5), (25, 13), (20, 1), 
                (3, 7), (6, 5), (13, 12), (18, 15), (26, 5), (26, 11), (10, 0), (21, 3), (15, 13), (26, 10), 
                (16, 7), (28, 3), (23, 7), (4, 12), (14, 2), (27, 12), (0, 5), (21, 1), (28, 13), (23, 4), 
                (29, 1), (17, 4), (0, 13), (5, 7), (10, 10), (1, 9), (22, 11), (20, 9), (11, 1), (12, 15), 
                (11, 5), (5, 5), (4, 13), (13, 9), (1, 3), (18, 5), (18, 1), (2, 8), (13, 6), (22, 7), 
                (22, 2), (0, 8), (14, 8), (8, 7), (23, 8), (25, 1), (15, 7), (26, 0), (20, 8), (5, 9), 
                (26, 2), (4, 4), (15, 0), (23, 2), (9, 9), (14, 5), (26, 4), (28, 14), (0, 3)]
        self.assertEqual(Table.TableCells(self, 30, 16, mines),
                            [[0, 0, 0, 0, 0, 1, '*', 2, '*', 2, '*', 2, 1, 1, 2, '*', 2, 2, 1, 3, '*', 3, 1, 0, 1, 2, '*', 1, 1, 1], 
                            [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, '*', 1, 2, '*', 4, '*', 2, '*', 3, '*', '*', 3, 2, 2, '*', 3, 2, 1, '*'], 
                            [2, 2, 1, 0, 0, 0, 0, 0, 1, '*', 2, 1, 1, 2, '*', 4, 2, 3, 1, 2, 3, 4, '*', '*', 3, 2, '*', 2, 2, 2], 
                            ['*', '*', 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 2, '*', 2, 1, 0, 1, '*', 5, '*', 3, 2, 3, 4, '*', 1], 
                            [3, 3, 1, 1, '*', 3, 2, 1, 0, 0, 1, 1, 2, 2, 3, 3, 3, '*', 2, 1, 1, 1, 3, '*', 2, 2, '*', '*', 3, 2], 
                            ['*', 1, 1, 2, 3, '*', '*', 1, 0, 1, 2, '*', 3, '*', '*', '*', 2, 3, '*', 2, 0, 1, 2, 3, 2, 4, '*', 4, 2, '*'], 
                            [1, 1, 2, '*', 4, 4, 5, 4, 2, 2, '*', 3, 4, '*', 5, 4, 3, 3, '*', 2, 1, 3, '*', 4, '*', 3, '*', 3, 2, 1], 
                            [1, 2, 3, '*', 3, '*', '*', '*', '*', 2, 1, 2, '*', 3, 3, '*', '*', 2, 1, 2, 2, '*', '*', '*', 3, 2, 2, '*', 1, 0], 
                            ['*', 3, '*', 3, 4, 3, 4, 3, 3, 2, 2, 2, 3, 3, '*', 3, 2, 2, 1, 3, '*', 4, 5, '*', 3, 0, 1, 1, 1, 0], 
                            [2, '*', 3, '*', 2, '*', 1, 0, 1, '*', 3, '*', 2, '*', 3, 2, 1, 1, '*', 3, '*', 2, 2, '*', 2, 1, 1, 1, 0, 0], 
                            [1, 1, 2, 1, 2, 1, 1, 0, 2, 3, '*', 2, 2, 1, 2, '*', 1, 1, 1, 2, 1, 2, 3, 3, 2, 2, '*', 2, 0, 0], 
                            [0, 0, 0, 1, 1, 1, 0, 0, 1, '*', 2, 1, 1, 1, 2, 1, 2, 1, 1, 0, 0, 1, '*', '*', 1, 3, '*', 4, 1, 0], 
                            [1, 1, 1, 3, '*', 2, 0, 0, 1, 2, 3, 2, 2, '*', 2, 1, 2, '*', 1, 0, 0, 1, 2, 2, 2, 3, '*', '*', 2, 1], 
                            ['*', 1, 1, '*', '*', 2, 0, 1, 1, 2, '*', '*', 2, 1, 2, '*', 2, 1, 1, 0, 0, 0, 0, 0, 1, '*', 3, 4, '*', 2], 
                            [1, 1, 1, 2, 2, 2, 1, 2, '*', 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 2, '*', 2], 
                            [0, 0, 0, 0, 0, 1, '*', 2, 2, '*', 1, 1, '*', 1, 0, 0, 0, 1, '*', 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]])
