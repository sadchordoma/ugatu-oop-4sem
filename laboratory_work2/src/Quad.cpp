#include "../include/Quad.h"


Quad::Quad() { std::cout << "Quad()\n"; };

Quad::Quad(int _x1, int _y1, int _x2, int _y2,
         int _x3, int _y3, int _x4, int _y4) :
            s1(new Section(_x1, _y1, _x2, _y2)),
            s2(new Section(_x3, _y3, _x4, _y4))
    { std::cout << "Quad(int _x1, int _y1, int _x2, int _y2)\n"; };

    // Quad(const Quad &other):
    // in this way just copying point other.s1 to this->.s1
    // if there will be created 2 these objects and one will be deleted
    // so another object with s1,s2 pointers to those pointers
    // that were deleted will be point to cleared areas of memory
    // and after call of 2-d destructor trying to delete these pointers....
    // spoiler: Process finished with exit code -1073740940 (0xC0000374)

    // it can be escaped by creating new object other
    // s1 = new Section(*s1) | s2 = new Section(*s2)
    // *s1 || *s2 - передаю объект, ибо s1, s2 - pointers
Quad::Quad(const Quad &other) : s1(other.s1), s2(other.s2) {
        std::cout << "Quad(const Quad &other)\n";
    }

Quad::~Quad() {
        std::cout << "~Quad()\n";
        delete s1;
        delete s2;
    }

void Quad::print() {
    std::cout << "s1 = ";
    s1->print_p1();
    std::cout << "s2 = ";
    s2->print_p2();
}