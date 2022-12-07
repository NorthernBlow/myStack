

int main(int argc, char*, argv[])
{

	int start, stop, step;
	cout << "Generator of progression.\n"
			"Enter start, stop, step:";

	cin >> start >> stop >>step;


	int x = start;

	while (x<stop)
	{

		printf("x = %d\n", x);
		x+=step;




	}


printf("After: x = %d\n", x);

	return 0;
}