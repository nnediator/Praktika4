import unittest
import random
class Voin(object):
    def __init__(self, x, y, z):
        self._unit = x
        self._endurance = y
        self._armor = z

    def health(self): 
        return self._unit
    
    def endurance(self): 
        return self._endurance
    
    def armor(self): 
        return self._armor
    
    def attack(self):
        if self._endurance > 0:
            self._endurance = self._endurance - 10
            if self._endurance < 0:
                self._endurance = 0
    
    def protection(self, x):
        if self._armor > 0:
            self._armor = self._armor - x
            if self._armor < 0:
                self._armor = 0
    
    def damage(self, x):
        if self._unit > 10:
            self._unit = self._unit - x
            if self._unit < 0:
                self._unit = 0                         
    def text(self,obj):
        print('Первый юнит:')
        print('Здоровье:', self.health())
        print('Броня:', self.armor())
        print('Выносливость:', self.endurance())
        print('Второй юнит:')
        print('Здоровье:', obj.health())
        print('Броня:', obj.armor())
        print('Выносливость:', obj.endurance())
        print()
    
    def fight(self,obj):
        print('Бой начался!')
        while self.health() > 10 and obj.health() > 10:
            a = random.randint(1,2)
            b = random.randint(1,2)
            if a == 1 and b == 1:
                print('Оба война атакуют.')
                self.attack()
                if self.endurance() > 0:
                    if obj.armor() > 0:
                        c = random.randint(0,20)
                    else:
                        c = random.randint(10,30)
                else:
                    c = random.randint(0,10)
                obj.damage(c)
                d = random.randint(0,10)
                obj.protection(d)
                obj.attack()
                if obj.endurance() > 0:
                    if self.armor() > 0:
                        c = random.randint(0,20)
                    else:
                        c = random.randint(10,30)
                else:
                    c = random.randint(0,10)
                self.damage(c)
                d = random.randint(0,10)
                self.protection(d)
                self.text(obj)
            if a == 1 and b == 2:
                print('Второй воин защищается, первый атакует.')
                self.attack()
                if self.endurance() > 0:
                    if obj.armor() > 0:
                        c = random.randint(0,20)
                    else:
                        c = random.randint(10,30)
                else:
                    c = random.randint(0,10)
                obj.damage(c)
                d = random.randint(0,10)
                obj.protection(d)
                self.text(obj)
            if a == 2 and b == 1:
                print('Первый воин защищается, второй атакует.')
                obj.attack()
                if obj.endurance() > 0:
                    if self.armor() > 0:
                        c = random.randint(0,20)
                    else:
                        c = random.randint(10,30)
                else:
                    c = random.randint(0,10)
                self.damage(c)
                d = random.randint(0,10)
                self.protection(d)
                self.text(obj)
        if obj.health() <= 10:
            print('Бой окончен. Победил первый юнит. Убить его противника? Введите да или нет.')
        else:
            print('Бой окончен. Победил второй юнит.')
            print('Убить его противника? Введите да или нет.')
        while True:
            a = input()
            if a == 'Да' or a == 'да':
                print('Вы убили противника.')
                break
            elif a == 'Нет' or a == 'нет':
                print('Вы пощадили противника.')
                break
            else:
                print('Введите правильный ответ.')
                print('Убить его противника? Введите да или нет.')

class TestVoin(unittest.TestCase):
    def setUp(self): # Создаем двух воинов для тестов
        self.u1 = Voin(100, 100, 100)
        self.u2 = Voin(100, 100, 100)
        
    def test_attack_reduces_endurance(self):
        self.u1.attack()
        self.assertEqual(self.u1.endurance(), 90)  

    def test_damage_reduces_health(self): # Проверяет, что метод damage правильно уменьшает здоровье.
        self.u1.damage(20)
        self.assertEqual(self.u1.health(), 80)
        self.u1.damage(90)
        self.assertEqual(self.u1.health(), 0)  # Не должно быть меньше 0

    def test_protection_reduces_armor(self): #Проверяет, что метод protection правильно уменьшает броню.
        self.u1.protection(10)
        self.assertEqual(self.u1.armor(), 90)
        self.u1.protection(100)
        self.assertEqual(self.u1.armor(), 0)  # Не должно быть меньше 0
        
#unit1 = Voin(100, 100, 100)
#unit2 = Voin(100, 100, 100)
#unit1.fight(unit2)

if __name__ == '__main__':
    unittest.main()
 
while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
