#include "std_lib_facilities.h"

using namespace std;

int main()
{

	double x;
	double y;
	double cast_x;   // явное преобразование типов С-cast
	double cast_y;

	double why = 1.0;
	int because = 100;
	double res = why / because;
	bool fuck = x - y == res;

	while(cin >> x >> y)
		//std::cout << res << std::endl;
		if (x < y || fuck) {
			std::cout << "Наименьшее числов равно: \n" << x << std::endl;
			
		}	
		else if ( y > x ) {
			std::cout << "Наибольшее число равно: \n" << y << std::endl;
			
		}
		else if (y == x) {
			std::cout << "Числа равны \n" << std::endl;
		}
		 else  {
		 	std::cout << "Числа почти равны \n" << std::endl;
		 }


	return 0;
}