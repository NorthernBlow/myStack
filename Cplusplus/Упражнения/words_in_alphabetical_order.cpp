#include "std_lib_facilities.h"
#include <vector>

int main()
{
	vector<string> words;
	vector<string> purgewords = {"windows","макбук","фашисты","яваскрипт","ангуляр","реакт","нода","продакшн","прод","энтерпрайз"};

	for (string temp; cin >> temp;) // чтение слов, разделенных пробелом и запись в вектор типа string
		words.push_back(temp); // собственно запись в вектор

	cout << "Количество слов: " << words.size() << '\n';

	sort(words); // сортировка слов

	for (int i = 0; i<words.size(); ++i)   // удаляет повторяющиеся слова
		if (i==0 || words[i-1] != words[i])
			cout << words[i] << '\n';

	// выводит отдельно нежелательные слова

	for (int i = 0; i<purgewords.size(); ++i)
		for (int j=0; j<words.size(); ++j)
			if (purgewords[i] == words[j])
				cout << "Запрещенные слова: " << purgewords[i] << '\n';

// Ctrl + D для остановки ввода данных

}