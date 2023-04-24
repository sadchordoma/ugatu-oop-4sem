#include <iostream>
#include "separator.cpp"

class Animal {
private:
    std::string name;
public:

    Animal() {
        std::cout << "Animal()\n";
    }

    virtual ~Animal() {
        std::cout << "~Animal()\n";
    }
//    virtual void clean_method() = 0; //- Variable type 'Animal' is an abstract class
    // при создании такого чистого абстрактного метода - весь класс становится абстрактным
    // => нельзя создать объект этого класса

    void non_virtual_sound() {
        std::cout << "Animal::non_virtual_sound()\n";
    }

    virtual void virtual_sound() {
        std::cout << "Animal::virtual_sound()\n";
    }
};

class SomeAnimal {
public:
    SomeAnimal() {
        std::cout << "SomeAnimal()\n";
    }

    ~SomeAnimal() {
        std::cout << "~SomeAnimal()\n";
    }
};

class Cat : public Animal {
public:

    Cat() {
        std::cout << "Cat()\n";
    }

    ~Cat() {
        std::cout << "~Cat()\n";
    }

    // Function 'non_virtual_sound' hides a non-virtual function from class 'Animal'
    void non_virtual_sound() {
        std::cout << "Cat::non_virtual_sound()\n";
    }

    // override - просто для указания компилятору, что я перекрываю виртуальный метод класс предка
    // в случае - если неправильно напишу имя метода - компилятор поругается
    // 'virtual_sound1' marked 'override' but does not override any member functions
    virtual void virtual_sound() override {
        std::cout << "Cat::virtual_sound()\n";
    }

    void catch_mouse() {}
};


class Dog : public Animal {
public:
    Dog() {
        std::cout << "Dog()\n";
    }

    virtual ~Dog() override {
        std::cout << "~Dog()\n";
    }
};

class SomeDog : public SomeAnimal {
public:
    SomeDog() {
        std::cout << "SomeDog()\n";
    }

    ~SomeDog() {
        std::cout << "~SomeDog()\n";
    }
};

int main() {
    Animal animal = Animal();
    animal.non_virtual_sound(); // Animal::non_virtual_sound()
    separate();

    Cat cat = Cat();
    // перекрытый метод
    cat.non_virtual_sound(); // Cat::non_virtual_sound()
    separate();

    Animal *animal1 = new Animal();
    animal1->non_virtual_sound(); // Animal::non_virtual_sound()
    delete animal1;
    separate();

    Cat *cat1 = new Cat();
    // перекрытый метод
    cat1->non_virtual_sound();  // Cat::non_virtual_sound()
    delete cat1;
    separate();

    // Возникают вопросы с тем, какой будет вызван только при том случае
    // когда мы в переменную типа класса-предка засовываем класс-потомок (или же указателя....)
    Animal animal2 = Cat();
    // ???????? побитово заполнили?????? оператор присваивания
    // наследуемый, потому что мы хоть и присвоили Animal'u Cat, но
    // у нас тип переменной Animal => функционал только тот, что есть у Animal

    animal2.non_virtual_sound();    // Animal::non_virtual_sound()
    separate();

    Animal *animal3 = new Cat();
    // наследумый метод
    animal3->non_virtual_sound();   //Animal::non_virtual_sound()
    delete animal3;

//    Cat cat2 = Animal();  // ошибка компиляции, нельзя в потомка засунуть предка
    // бюрократия
    separate2();
    std::cout << "\t\tvirtual\n";
    separate();

    Animal animal4 = Animal();
    animal4.virtual_sound(); // Animal::virtual_sound()
    separate();

    Cat cat3 = Cat();
    // перекрытый метод
    cat3.virtual_sound(); // Cat::virtual_sound()
    separate();

    Animal *animal5 = new Animal();
    animal5->virtual_sound(); // Animal::virtual_sound()
    delete animal5;
    separate();

    Cat *cat4 = new Cat();
    // перекрытый метод
    cat4->virtual_sound();  // Cat::virtual_sound()
    delete cat4;
    separate();

    // Возникают вопросы с тем, какой будет вызван только при том случае
    // когда мы в переменную типа класса-предка засовываем класс-потомок (или же указателя....)
    Animal animal6 = Cat();
    // ???????? побитово заполнили?????? оператор присваивания
    // наследуемый, потому что мы хоть и присвоили Animal'u Cat, но
    // у нас тип переменной Animal => функционал только тот, что есть у Animal
    animal6.virtual_sound();    // Animal::virtual_sound()
    separate();

    Animal *some_cat = new Cat();
    // перекрытый метод - благодаря virtual
    some_cat->virtual_sound();  // Cat::virtual_sound()
    delete some_cat;

    separate2();
    std::cout << "\t\tvirtual destructor\n";
    // виртуальный деструктор
    separate();
    Animal *some_dog = new Dog();
    delete some_dog;
    separate();
    // не виртуальный деструктор
    SomeAnimal *some_dog1 = new SomeDog();
    delete some_dog1;
    separate();
}

//#TO-DO разобраться с Animal animal2 = Cat() на 44-й строке и на 93-й строке
