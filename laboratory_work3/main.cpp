#include "DoubleLinkedList.cpp"
#include "../laboratory_work2/src/ColoredPoint.cpp"

int main() {
    srand(time(NULL));

     //int
//    DoubleLinkedList<int> list;
//    list.push_back(1);
//    list.push_back(2);
//    list.push_front(3);
//    list.insert(0, 5);
//    list.insert(1, 4);
//    std::cout << list.has(0) << "\n";
//    Node<int> *b = list.next_elem();
//    Node<int> *c = list.next_elem(b);
//    std::cout << b->data << "\n";
//    std::cout << c->data << "\n";
//    Node<int> *k = list.get_by(5);
//    std::cout << k->data << "\n";

    clock_t begin = clock();
        DoubleLinkedList<Point> list;
//    Node<Point> *tmp = new Node<Point>();
//    std::cout << list.first() << "\n" << list.eol() << "\n" << list.next_elem_object() << "\n";
//    for (list.first(); !list.eol(); list.next_elem_object()) {
//        std::cout << list.get_object();
//    }

//    for (int i = 0; i < 10000; i++) {
//        int r_num = rand() % 6;
//        int r_num2 = rand() % 6;
//        ColoredPoint CPoint(r_num, r_num2);
//        switch (r_num) {
//            case 0:
//                list.push_back(CPoint);
//                break;
//            case 1:
//                list.push_front(CPoint);
//                break;
//            case 2:
//                if (list.get_size() == 0) {
//                    list.insert(0, CPoint);
//                }
//                else {
//                    list.insert(r_num % list.get_size(), CPoint);
//                }
//                break;
//            case 3:
//                tmp = list.next_elem(tmp);
//                break;
//            case 4:
//                list.remove(CPoint);
//                break;
//            case 5:
//                tmp = list.next_elem(tmp);
//                if (tmp) {
//                    tmp->data.print();
//                    tmp->data.get_x();
//                    tmp->data.get_y();
//                }
//        }
//    }
//    DoubleLinkedList<Point> l;
//    l.push_back(Point());
    clock_t end = clock();
    double time_spent = (double) (end - begin) / CLOCKS_PER_SEC;
    std::cout << "Time of the programme:  " << time_spent << "s\n";
//    delete tmp;
    return 0;
}
