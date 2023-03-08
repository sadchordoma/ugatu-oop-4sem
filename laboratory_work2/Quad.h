/* композиция объектов: атрибутом одного объекта класса A является указатель
 * на другой объект класса B, создаваемый в конструкторе класса A и уничтожаемый
 * в деструкторе класса A; композируемые классы должны определяться отдельно
 * (не один в другом); при композиции показать, в чем разница, если объект класса
 * А хранит прямо объект класса В или указатель на объект класса В.
 */

// четырехугольник
class Quad {
public:

    Quad();

    Quad(int _x1, int _y1, int _x2, int _y2,
         int _x3, int _y3, int _x4, int _y4);

    // Quad(const Quad &other):
    // in this way just copying point other.s1 to this->.s1
    // if there will be created 2 these objects and one will be deleted
    // so another object with s1,s2 pointers to those pointers
    // that were deleted will be point to cleared areas of memory
    // and after call of 2-d destructor trying to delete these pointers....
    // spoiler: Process finished with exit code -1073740940 (0xC0000374)

    // it can be escaped by creating new object other
    // s1 = new Section(*s1) | s2 = new Section(*s2)
    Quad(const Quad &other);

    ~Quad();

    void print();

protected:
    Section *s1{new Section};
    Section *s2{new Section};
};