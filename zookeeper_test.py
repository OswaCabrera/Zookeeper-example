import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    def test_crear_2_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree2 = Ztree()
        tree2.create('/node2', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')
    
    def buscar_Znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.exist('/node')
    
    def buscar_Znode_no_existente(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1', 'algo', True, True, 10, '/')
            tree.exist('/node22222')

    def info_Znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        print(tree.getData('/node1'))
    
    def info_Znode_inexistente(self):
        print(Ztree.getData('/nodenoexiste'))


if __name__ == '__main__':
    unittest.main()

