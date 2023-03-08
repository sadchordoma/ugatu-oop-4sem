#include "Point.cpp"


class ColoredPoint : public Point {
protected:
    std::string color{"white"};
public:
    // initialization of class fields in constructor initialization list
    ColoredPoint() : Point() { std::cout << "ColoredPoint()\n"; }

    ColoredPoint(int _x, int _y, std::string color = "white") :
            Point(_x, _y), color(color) {
        std::cout << "ColoredPoint(int _x, int _y, "
                     "std::string color = \"white\")\n";
    }

    ColoredPoint(const ColoredPoint &other) :
            Point(other.x, other.y), color(other.color)
            { std::cout << "ColoredPoint(const ColoredPoint &other)\n"; }

    ~ColoredPoint() {
        std::cout << "~ColoredPoint()\n";
        color = "";
    }

    void print_color() {
        std::cout << color << "\n";
    }

    void change_color(std::string new_color) {
        this->color = new_color;
    }
};