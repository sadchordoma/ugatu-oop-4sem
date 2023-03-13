#include "../include/Section.h"


Section::Section() { std::cout << "Section()\n"; };

Section::Section(int _x1, int _y1, int _x2, int _y2) :
        p1(_x1, _y1), p2(_x2, _y2) { std::cout << "Section(int _x1, int _y1, int _x2, int _y2)\n"; }

//Section::Section(const Section &other) :
//        p1(other.p1.get_x(), other.p1.get_y()),
//        p2(other.p2.get_x(), other.p2.get_y()) { std::cout << "Section(const Section &other)\n"; }
Section::Section(const Section &other) :
        p1(other.p1),
        p2(other.p2)
        { std::cout << "Section(const Section &other)\n"; }

Section::~Section() { std::cout << "~Section()\n"; }

void Section::print_p1() {
    p1.print();
}

void Section::print_p2() {
    p2.print();
}

void Section::print() {
    print_p1();
    print_p2();
}