#include <vector>
#include <iostream>


using namespace std;

int main()
{
	vector<string> words;
	vector<string> purgewords = {"windows","макбук","фашисты","яваскрипт","ангуляр","реакт","нода","продакшн","прод","энтерпрайз"};

	for (string temp; cin >> temp;) // чтение слов, разделенных пробелом и запись в вектор типа string
		words.push_back(temp); // собственно запись в вектор

	cout << "Количество слов: " << words.size() << '\n';

	//sort(words); // сортировка слов

	for (int i = 0; i<words.size(); ++i)   // удаляет повторяющиеся слова
		if (i==0 || words[i-1] != words[i])
			cout << words[i] << '\n';	// выводит слова без повторяющихся тебе В КОНСОЛЬ


	// выводит отдельно нежелательные слова
	for (int i = 0; i<purgewords.size(); ++i) // итерируемся по вектору запрещенных слов
		for (int j=0; j<words.size(); ++j)	 // итерируемся по вектору слов, который ввел пользователь
			if (purgewords[i] == words[j])  // сравниваем запрещенное слово с тем что ввел пользователь
				cout << "Запрещенные слова: " << purgewords[i] << '\n';  // тут и выводит то что плохое

// Ctrl + D для остановки ввода данных

}