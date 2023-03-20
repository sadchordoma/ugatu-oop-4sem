// class Point
class Point {
public:
    // methods

    // constructor without parameters
    Point();

    // constructor with parameters
    // explicit - prohibit implicit constructor call
    // for example - to prevent call this when passing this to func

//    explicit Point(int _x, int _y = 0);       // poka 4to ybral
    Point(int _x, int _y = 0);

    // constructor with parameter-object the same class
    Point(const Point &other);


    // destructor
    ~Point();

    int get_x() const;

    int get_y() const;

    // realization in Point.cpp
    void set_x(int _x);

    // method realization immediately in the definition
    void set_y(int _y) {
        this->y = _y;
    }

    void print() const { std::cout << "x = " << x << " y = " << y << "\n"; }

    friend std::ostream& operator<<(std::ostream& stream, const Point& obj)
    {
        obj.print();
        return stream;
    }

    bool operator==(const Point &other) {
        if (this->x == other.x && this->y == other.y) {
            return true;
        }
        return false;
    }

    bool operator!=(const Point &other) {
        return !(*this == other);
    }

protected:
    // attributes
    // {0} - x = 0 immediately
    // when creating object before call constructor
    int x{0};
    int y{0};
};