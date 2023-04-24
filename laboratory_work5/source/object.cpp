#include "separator.cpp"

#include <iostream>
#include <memory>

class Object {
private:
    std::string name;
public:
    Object(std::string name) {
        this->name = name;
        std::cout << "Object(std::string name)\n";
    }

    Object() {
        std::cout << "Object()\n";
    }

    ~Object() {
        std::cout << "~Object()\n";
    }

    void print_name() {
        std::cout << this->name << "\n";
    }
};


void func1() {
    auto *obj = new Object(); // не удалится после выхода из функции
    // (не удалится после выхода из области видимости)
}

// unique_ptr - ответственный за время жизни объекта
void func2() {
    std::unique_ptr<Object> o = make_unique<Object>("01"); // удалится при выходе из области видимости
}

std::unique_ptr<Object> func2_2(std::unique_ptr<Object> o) {
    o->print_name();
    // o удалится при выходе из области видимости
    return o;   // move(o)
}

void func3(std::shared_ptr<Object> o) {
    o->print_name();    // удалится при выходе из области видимости последнего из указаталей
}

int main() {
    func1();
    separate();

    unique_ptr<Object> o1 = make_unique<Object>("o1");
//    func2_2(o1) - doesn't work this way;
    // не скомпилится - при таком случае в какой-то
    // момент было бы 2 копии unique_ptr
    // но можно через move(o);
    // в таком случае объект удалится в функции
    // и на него уже ничего ссылаться не будет
    // а умный указатель останется на месте

    // передача из функции
    unique_ptr<Object> o3 = func2_2(move(o1));
    // btw - o1 = nullptr / o3 != nullptr
    separate();

    func2();
    separate();

    shared_ptr<Object> o2 = make_shared<Object>("o2");
    func3(o2);
    shared_ptr<Object> o4 = o2;
    separate();
    return 0;
}