#include <iostream>
#include "std_lib_facilities.h"
using namespace std;

int main()
{
	vector<string> words;

	for (string temp; cin >> temp;) // чтение слов, разделенных пробелом и запись в вектор типа string
		words.push_back(temp); // собственно запись в вектор

	cout << "Количество слов: " << words.size() << '\n';

	sort(words); // сортировка слов

	for (int i = 0; i<words.size(); ++i)
		if (i==0 || words[i-1] != words[i])
			cout << words[i] << '\n';

// Ctrl + D для остановки ввода данных

}