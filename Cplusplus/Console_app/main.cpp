#include <iostream>

using namespace std;


int main()
{

    setlocale(LC_ALL, "ru");

    for (int i = 1; i < 5; i++)
    {
        cout << "Сработал 1й цикл итерации For" << i << endl;

        for (int j = 1; j < 5; j++)
        {

            cout <<"\tсработал 2й цикл for итерации" << j << endl;
        }
    }


    cout << "Hello world!" << endl;
}
