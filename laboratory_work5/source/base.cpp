#include "separator.cpp"

class Base {
private:
    int value{0};
public:
    void set_value() {
        this->value = 5;
    }
    Base() {
        std::cout << "Base()\n";
    }

    Base(const Base *obj) {
//        this->value = obj->value;
        std::cout << "Base(const Base *obj)\n";
    }

    Base(const Base &obj) {   // конструктор копирования
//        this->value = obj.value;
        std::cout << "Base(const Base &obj)\n";
    }

    virtual ~Base() {
        std::cout << "~Base()\n";
    }

    virtual void sound() {
        std::cout << "its-me " << this->value << "\n";
    }
};

class Desc : public Base {
public:
    Desc() {
        std::cout << "Desc()\n";
    }

    Desc(Desc *obj) {
        std::cout << "Desc(Desc *obj)\n";
    }

    Desc(Desc &obj) {   // конструктор копирования
        std::cout << "Desc(Desc &obj)\n";
    }

    virtual ~Desc() override {
        std::cout << "~Desc()\n";
    }

    virtual void sound() override {
        std::cout << "desc-sound\n";
    }
};

void func1(Base obj) {
    obj.sound();
    std::cout << "func1(Base obj)\n";
}

void func2(Base *obj) {
    if (dynamic_cast<Desc *>(obj)) {
        std::cout << "func2(Base *obj) casted\n";
    } else {
        std::cout << "func2(Base *obj)\n";
    }
    obj->sound();
}

void func3(Base &obj) {
    if (dynamic_cast<Desc *>(&obj)) {
        std::cout << "func3(Base &obj) casted\n";
    } else {
        std::cout << "func3(Base &obj)\n";
    }
    obj.sound();
}

Base static_create1() {
    std::cout << "Base static_create1()\n";
    Base obj;
    return obj;
//    return Base();
}

Base *static_create2() {
    std::cout << "Base* static_create2()\n";
    Base obj;
    return &obj;
}

Base &static_create3() {
    std::cout << "Base& static_create3()\n";
    Base obj;
    return obj;
}

Base dynamic_create4() {
    std::cout << "Base dynamic_create4()\n";
    Base *obj = new Base();
    // сначала создался Base(), затем создался указатель
    // Base *obj и записался адрес Base() в переменную
    return *obj;
}

Base *dynamic_create5() {
    std::cout << "Base* dynamic_create5()\n";
    Base *obj = new Base();
    return obj;
}

Base &dynamic_create6() {
    std::cout << "Base& dynamic_create6()\n";
    Base *obj = new Base();
    return *obj;
}

int main() {
    Base base;
    Desc desc;
    separate();
    separate();

    // Когда объект передается в функцию, нужно текущее состояние этого объекта.
    // Если бы при создании копии вызывался конструктор, то осуществлялась бы инициализация
    // объекта, которая бы изменила его состояние. Поэтому конструктор не может
    // вызываться при создании копии объекта для передачи в функцию.
    // => вызывается оператор копирования
    base.set_value();
    func1(base);   // передается копия base через оператор копирования?
    separate();
    func2(&base);
    separate();

    func3(base);
    separate();
    separate();

    func1(desc);    // передается копия desc, но типа Base
    separate();

    func2(&desc);
    separate();

    func3(desc);
    separate();
    separate();

    separate2();

    Base stat1 = static_create1();  // возвращается локально созданная копия
    // внутри функции элемент не удалился - его передали сюда
    stat1.sound();
    separate();

    Base *stat2 = static_create2(); // так как передается ссылка на локально
    // созданный объект, то сам он в функции создается и удаляется
//    stat2->sound(); - нельзя - объект уже удален
//    delete stat2;   // ничего не происходит - UB
    separate();

    Base &stat3 = static_create3(); // так как вовзращается ссылка на локально
    // созданный объект, то сам он в функции создается и удаляется
//    stat3.sound(); - нельзя - объект уже удален
//    delete &stat3; // ничего не происходит - UB
    separate();

    Base dyn4 = dynamic_create4(); // динамический объект в функции не уничтожится,
    // но скопируется и вернется
    dyn4.sound();
    separate();

    Base *dyn5 = dynamic_create5(); // в функции создается и передается в переменную
    dyn5->sound();
    delete dyn5;
    separate();

    Base &dyn6 = dynamic_create6(); // в функции создается и передается в переменную
    dyn6.sound();
    delete &dyn6;
    separate();

}
