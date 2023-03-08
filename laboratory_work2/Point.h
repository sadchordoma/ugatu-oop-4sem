// class Point
class Point {
public:
    // methods

    // constructor without parameters
    Point();

    // constructor with parameters
    // explicit - prohibit implicit constructor call
    // for example - to prevent call this when passing this to func
    explicit Point(int _x, int _y = 0);

    // constructor with parameter-object the same class
    Point(Point &other);

    // destructor
    ~Point();

    int get_x() const;

    int get_y() const;

    void set_x(int _x);

    // method realisation immediately in the definition
    void set_y(int _y) {
        this->y = _y;
    }

    void print() {
        std::cout << "x = " << x << " y = " << y << "\n";
    }

protected:
    // attributes
    int x{0};
    int y{0};
};
