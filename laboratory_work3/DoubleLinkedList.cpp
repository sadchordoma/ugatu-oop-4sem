#include <iostream>


template<typename T>
struct Node {
    Node<T> *next{nullptr};
    Node<T> *prev{nullptr};
    T data;
    bool is_empty{true};

    Node() {};

    Node(T _data) {
        is_empty = false;
        data = _data;
    }
    ~Node() {}
};


template<typename T>
class DoubleLinkedList {

public:
    DoubleLinkedList() {
        std::cout << "DoubleLinkedList()\n";
    };

    ~DoubleLinkedList() {
        while (head) {
            tail = head->next;
            delete head;
            head = tail;
        }
    }

    void push_back(T object) {
        if (size == 0) {
            initialize_first_node(object);
        } else {
            Node<T> *tmp = tail;
            tail->next = new Node<T>(object);
            tail = tail->next;
            tail->prev = tmp;
        }
        size++;
    }

    void push_front(T object) {
        if (size == 0) {
            initialize_first_node(object);
        } else {
            Node<T> *tmp = head;
            head->prev = new Node<T>(object);
            head = tmp->prev;
            head->next = tmp;
        }
        size++;
    }

    int insert(int index, T object) {
        if (index == 0 || size == 0) {
            push_front(object);
            return 0;
        }
        if (index > size) {
            return -1;
        }
        if (index == size) {
            push_back(object);
            return 0;
        }
        Node<T> *to_insert = head;
        for (std::size_t i = 0; i < index; i++) {
            to_insert = to_insert->next;
        }
        Node<T> *indexed = to_insert;
        to_insert = new Node<T>(object);
        to_insert->next = indexed;
        to_insert->prev = indexed->prev;
        indexed->prev->next = to_insert;
        indexed->prev = to_insert;
        size++;
        return 0;
    }

    // change - instead of giving object - give index

    //????? -----------

    // now returns data of object instead of object

    Node<T> *get_by(T object) {
        Node<T> *current = head;
        while (current != nullptr && current->data != object) {
            current = current->next;
        }
        if (current == nullptr) {
            return nullptr;
        }
        // bilo current; changed to current->data
        if (current->data == object) {
            return current->data;
        }
        return nullptr;
    }

    bool has(T object) {
        if (get_by(object) != nullptr) {
            return true;
        }
        return false;
    }

    Node<T> *next_elem(Node<T> *current = nullptr) {
        if (current == nullptr || current->next == nullptr) {
            return nullptr;
        }
        // bilo current->next; changed to current->next->data
        return current->next->data;
    }

    int remove(T object) {
        if (size == 0 && !has(object)) {
            return -1;
        }
        Node<T> *current = head;
        while (current != nullptr && current->data != object) {
            current = current->next;
        }
        if (current == nullptr) {
            return -1;
        }
        if (current->data == object) {
            if (head == tail) {
                size--;
                return 0;
            }
            if (current == tail) {
                tail = current->prev;
            }
            if (current == head) {
                head = current->next;
            }

            Node<T> *after_current = current->next;
            Node<T> *before_current = current->prev;
            if (after_current != nullptr) {
                after_current->prev = before_current;
            }
            if (before_current != nullptr) {
                before_current->next = after_current;
            }
            size--;
            return 0;
        }
        return -1;
    }

    std::size_t get_size() {
        return size;
    }

    void next_elem_object() {
        if (current == nullptr) {
            return;
        }
        if (current->next != nullptr) {
            current = current->next;
//            return current->data;
            return;
        }
        return;
    }

    void first() {
        if (size == 0) {
            return;
        }
        current = head;
        return;
    }

    bool eol() {        // end of list
        if (size == 0) {
            return true;
        }
        return false;
    }

    void get_object() {
        if (current != nullptr) {
            return;
        }
        return;
    }
// пофиксить с virtual and override functions Point..... and so on ...
// rewatch it and refactor things
private:

    std::size_t size{0};
    Node<T> *head{nullptr};
    Node<T> *tail{nullptr};
    Node<T> *current{nullptr};

    void initialize_first_node(T object) {
        head = new Node<T>(object);
        tail = head;
        current = head;
    }
};