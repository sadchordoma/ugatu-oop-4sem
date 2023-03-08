#include <iostream>
#include "Point.cpp"


class Line{
public:

    Line() {
        std::cout << "Line()\n";
    };

    Line(int _x1, int _y1, int _x2, int _y2) {
        std::cout << 4;
        std::cout << "Line(int _x1, int _y1, int _x2, int _y2)\n";
        p1 = Point(_x1, _y1);
        p2 = Point(_x2, _y2);
    }

    ~Line() {
        std::cout << 5;
        std::cout << "~Line()\n";
    }
protected:
    Point p1;
    Point p2;
};


int main() {
/*    // статически создаваемых объектов («MyClass obj;»)
    // статически созданных объектов - destructor
    Point p1;
    p1.print();
    // динамически создаваемых объектов («MyClass *obj = new MyClass();»)
    Point *p2 = new Point();
    p2->print();
    // уничтожение динамически созданных объектов
    delete p2;
    // объектов с помощью различных конструкторов (у каждого создаваемого объекта
    // должны быть: конструктор без параметров, с параметрами, с параметром-объектом
    // того же класса – конструктор копирования)
    Point p3;
    p3.print();
    Point p4(1, 2);
    p4.print();
    Point p5(p4);
    p5.print();

    Line l;
    l.print_all_available_from_point();*/
//    Line l1(1, 2, 3, 4);
//    Point a ;
//    Point b ( 5 , 6 ) ;
//    Point c ( a ) ;
//    Point d = a ;

    Point a(1,2);
    Point d;
    d = a;
    d.print();
    return 0;
}



//TODO | инициализация полей класса в списке инициализации конструктора

//TODO | помещение объектов в переменные различных типов (объяснять,
// чем отличается MyBase * obj = new MyBase() от MyBase * obj = new MyDeriv())

//TODO | объектов классов-наследников (проверить и продемонстрировать,
// какие конструкторы классов при этом вызываются)

//TODO | композиция объектов: атрибутом одного объекта класса A является другой
// объект класса B (не указатель!), инициализируемый в списке инициализации
// конструктора класса A; показать, когда этот объект класса B удаляется

//TODO | композиция объектов: атрибутом одного объекта класса A является указатель
// на другой объект класса B, создаваемый в конструкторе класса A и уничтожаемый
// в деструкторе класса A; композируемые классы должны определяться отдельно
// (не один в другом); при композиции показать, в чем разница, если объект класса
// А хранит прямо объект класса В или указатель на объект класса В.

//TODO | уничтожение объектов классов-наследников (проверить и продемонстрировать,
// какие деструкторы классов при этом вызываются)
