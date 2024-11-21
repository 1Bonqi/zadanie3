from module_12_4 import Runner
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='test_mod.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            man = Runner('Арсен', -1)
            for i in range(5):
                man.walk()
            self.assertEqual(man.distance(25))
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            female = Runner(400)
            for i in range(10):
                female.run()
            self.assertEqual(female.distance(100))
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()
