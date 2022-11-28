#include <iostream>

// преобразование градусов по цельсию в градусы фаренгейта
// f=9/5*c+32


int main()
{

std::cout << "Введите градусы по цельсию: ";
double dc;
std::cin >> dc;
double res = 9/5;

std::cout << (res*dc) + 32 << " fahrenheits" << '\n'; 

return 0;
}
