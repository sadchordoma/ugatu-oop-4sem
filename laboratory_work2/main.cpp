#include <iostream>
#include "src/ColoredPoint.cpp"
#include "src/Section.cpp"
#include "src/Quad.cpp"


/* объекты классов-наследников (проверить и продемонстрировать,
 * какие конструкторы классов при этом вызываются)
 * уничтожение объектов классов-наследников (проверить и продемонстрировать,
 * какие деструкторы классов при этом вызываются)
 *
 * В случае класса-наследника,
 * то вначале всегда создаются - вызываются конструкторы
 * всех базовые классы, от которых был наследован класс-наследник
 * в конце же вызываются деструкторы всех классов в обратную сторону

 * в случае 1 класса и 1 класса-наследника,

 * при создании класса-наследника, сначала
 * создается класс, затем класс-наследник

 * при удалении класса-наследника, сначала удаляется класс-наследник,
 * затем тот класс, от которого было наследование
*/


int main() {
    // статически создаваемые объекты («MyClass obj;»)
    // уничтожение статически созданных объектов - destructor
    Point p1;
    p1.print();

    // динамически создаваемые объектов («MyClass *obj = new MyClass();»)
    Point *p2 = new Point();
    p2->print();
    // уничтожение динамически созданных объектов
    delete p2;

    // создание объектов с помощью различных конструкторов (у каждого создаваемого объекта
    // должны быть: конструктор без параметров, с параметрами, с параметром-объектом
    // того же класса – конструктор копирования)
    Point p3;
    p3.print();

    Point p4(1, 2);
    p4.print();


    Point p5(p4);
    p5.print();


    // помещение объектов в переменные различных типов (объяснять,
    // чем отличается MyBase * obj = new MyBase() от MyBase * obj = new MyDeriv())
    // p6 - class = class
    Point *p6 = new Point(1, 2);
    delete p6;
    Point *cp1 = new ColoredPoint(1, 2, "black");
    delete cp1;
    // cp1 - class = subclass
    // only usable available methods and fields of class cos
    // every square is a figure but not every figure is a square
    // cp1->print_color(); -- not callable - print_color - method of ColoredPoint only
    // Calls of .... Section? Quad?
    Section s1;
    std::cout << "\n\n\n";
    Section s2(1, 2, 3, 4);
    Quad q1;
    return 0;
}