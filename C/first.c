#include <stdio.h>
#include <stdlib.h>


#define RED "\e[0;31m"


int exec()
{

return 0;

}



int fork()
{

return 0;
}



int wait()
{

return 0;

}


int main(int argc, char *argv[])
{

	if (argc > 1){

		fprintf(stderr, RED "[ERROR]"
               RED  ": Больше 1 аргумента передано \n");

		exit(EXIT_FAILURE);
	}

return 0;

}