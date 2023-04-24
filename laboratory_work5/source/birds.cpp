#include <iostream>
#include "separator.cpp"

#pragma clang diagnostic push
#pragma ide diagnostic ignored "IncompatibleTypes"

class Bird {
public:

    Bird() {
        std::cout << "Bird()\n";
    }

    virtual ~Bird() {
        std::cout << "~Bird()\n";
    }

    virtual std::string classname() {
        return "Bird";
    }

    virtual bool isA(const std::string &who) {
        return who == "Bird";
    }

};

class Eagle : public Bird {
public:
    Eagle() {
        std::cout << "Eagle()\n";
    }

    virtual ~Eagle() override {
        std::cout << "~Eagle()\n";
    }

    virtual std::string classname() override {
        return "Eagle";
    }

    // отличие isA and classname в том, что через
    // isA намного легче проводить проверку на принадлежность
    // ибо мы внутри функции сразу проверяем и Eagle, и Bird
    // А через в случае classname, нам в коде нужно будет проверять
    // не только classname, но и другие имена наследников класса Bird
    virtual bool isA(const std::string &who) override {
        return who == "Eagle" || Bird::isA(who);
    }

    void attack() {
        std::cout << "attacking\n";
    }

};

class Owl : public Bird {
public:
    Owl() {
        std::cout << "Owl()\n";
    }

    virtual ~Owl() override {
        std::cout << "~Owl()\n";
    }

    virtual std::string classname() override {
        return "Owl";
    }

    virtual bool isA(const std::string &who) override {
        return who == "Owl" || Bird::isA(who);
    }

    void sleep() {
        std::cout << "sleeping\n";
    }
};

// heliaca  - Могильник
class HeliacaEagle : public Eagle {
public:

    HeliacaEagle() {
        std::cout << "HeliacaEagle()\n";
    }

    virtual ~HeliacaEagle() override {
        std::cout << "~HeliacaEagle()\n";
    }

    virtual std::string classname() override {
        return "HeliacaEagle";
    }

    virtual bool isA(const std::string &who) override {
        return who == "HeliacaEagle" || Eagle::isA(who);
    }
};

class Quetzal : public Bird {
public:
    Quetzal() {
        std::cout << "Quetzal()\n";
    }

    virtual ~Quetzal() override {
        std::cout << "~Quetzal()\n";
    }

    virtual std::string classname() override {
        return "Quetzal";
    }

    virtual bool isA(const std::string &who) override {
        return who == "Quetzal" || Bird::isA(who);
    }

    void pose() {
        std::cout << "posing\n";
    }
};

int main() {
    Bird *bird;
    if (rand() % 2 == 0) {
        bird = new Eagle();
    } else {
        bird = new HeliacaEagle();
    }
    // usage of these validations - safe types cast manually
    // использование classname
    if (bird->classname() == "Eagle" || bird->classname() == "HeliacaEagle") {
        // 2 ways
        static_cast<Eagle *>(bird)->attack();
        ((Eagle *) bird)->attack();
    }
    separate();

    // использование isA(string)
    if (bird->isA("Eagle")) {
        static_cast<Eagle *>(bird)->attack();
    }
    separate();

    // static_cast<>() почему не надо
    Bird *owl = new Owl();
    // в owl находится не Eagle => Undefined Behaviour || crash programme
    // that's why it is called unsafe cast
    static_cast<HeliacaEagle *>(owl)->attack();
    separate();

    // dynamic_cast<>() - safe cast because
    // returns nullptr if not class provided in <>
    Bird *birds[10];
    int random = 0;
    for (int i = 0; i < 10; i++) {
        random = rand() % 3;
        if (random == 0) {
            birds[i] = new Eagle();
        } else if (random == 1) {
            birds[i] = new HeliacaEagle();
        } else {
            birds[i] = new Owl();
        }
    }
    separate();

    for (auto &bird: birds) {
        auto mb_owl = dynamic_cast<Owl *>(bird);
        if (mb_owl) {
            mb_owl->sleep();
        }
        auto mb_eagle = dynamic_cast<Eagle *>(bird);
        if (mb_eagle) {
            mb_eagle->attack();
        }
        auto mb_quetzal = dynamic_cast<Quetzal *>(bird);
        if (mb_quetzal) {
            mb_quetzal->pose();
        }

    }
    separate();
    delete bird;
    delete owl;
    // delete all birds
    for (auto &bird: birds) {
        delete bird;
    }
}

#pragma clang diagnostic pop