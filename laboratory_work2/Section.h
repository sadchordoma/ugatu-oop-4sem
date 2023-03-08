/*
 * композиция объектов: атрибутом одного объекта класса A является другой
 * объект класса B (не указатель!), инициализируемый в списке инициализации
 * конструктора класса A; показать, когда этот объект класса B удаляется
 */

class Section {
public:

    Section();

    Section(int _x1, int _y1, int _x2, int _y2);

    Section(const Section &other);

    ~Section();

    void print_p1();

    void print_p2();

    void print();

protected:
    Point p1;
    Point p2;
};