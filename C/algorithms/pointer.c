// указатели представляют собой объекты, значением которых служат адреса других объектов
// или функций. Указатели это неотъемлемый компонент для управления памятью в С
// для определения указателя надо написать тип объекта, на который указывает указатель и
// символ *.

//int *p;

//   int x = 10; // определяем переменную
//   int *p; // определяем указатель
//   p = &x; // указатель получает адрес переменной


// Указатель хранит адрес объекта в памяти компьютера. И для получения адреса к переменной
// применяется операция &. Эта операция применяется только к таким объектам, которые ////хранятся в памяти кудахтера, т.е. к переменным и элементам массива.

// Что важно, переменная x имеет тип int, и указатель, который указывает на ее адрес тоже имеет тип int. То есть должно быть соответствие по типу. Указатель должен быть того же типа что и объект на который он ссылается.

// Чтобы узнать какой адрес имеет переменная х, можно использовать спецификатор %p для нашего указателя:

#include <stdio.h>

int main(void) {
    int x = 10;
    int *p;
    p = &x;
    printf("%p \n", p);   //0060FEA8  - адрес в памяти в шестнадцатеричном формате
    return 0;
}


// указаль p ссылается на адрес, по которому располагается переменная Х 0x0060FEA8
// но так как указатель хранит адрес, то можно по этому адресу получить хранящееся там
// значение, то есть значение переменной х
