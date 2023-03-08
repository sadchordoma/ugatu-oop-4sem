#include "Point.h"


Point::Point() {
    std::cout << "Point()\n";
}

Point::Point(int _x, int _y) {
    std::cout << "Point(int _x, int _y)\n";
    set_x(_x);
    set_y(_y);
}

Point::Point(Point &other) {
    std::cout << "(Point &other)\n";
    set_x(other.get_x());
    set_y(other.get_y());
}

Point::~Point() {
    std::cout << "~Point()\n";
    x = 0;
    y = 0;
}

// methods realization after define

int Point::get_x() const {
    return x;
}

int Point::get_y() const {
    return y;
}

void Point::set_x(int _x) {
    this->x = _x;
}