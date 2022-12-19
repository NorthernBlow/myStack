#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>

//
// ПРОВЕРЯЕМ ЯВЛЯЕТСЯ ЛИ ЧИСЛОМ
//
int test_number(const char * str) {
    char * tail;
    long num;
    
    errno = 0;
    num = strtol(str, &tail, 10);
    
    return ( errno || *tail );
}


int main (int argc, char **argv) { 
    
    pid_t pid;
    pid_t pid2;

    FILE *file, *file1, *file2;
    

    //
    // ПРОВЕРЯЕМ КОЛИЧЕСТВО АРГУМЕНТОВ
    //
    if (argc != 2 ) {


        // fprintf(stderr, "Неверное количество параметров\n");
        fprintf(stderr, "1\n");
        return 1;
    }
    else {
        //
        // ПРОВЕРЯЕМ ВСЕ ПЕРЕДАННЫЕ АРГУМЕНТЫ НА СООТВЕТСТВИЕ ЧИСЛОВОМУ ТИПОМ
        //
        for(int i = 1; i < argc; i ++)
            if (test_number(argv[i])) {
                fprintf(stderr, "2\n");
                return 2;
            }

        // printf("%s var", argv[1]);

        if (atoi(argv[1]) < 1 || atoi(argv[1]) > 13) {
            fprintf(stderr, "3\n");
            return 3;

        }
        else if (atoi(argv[1]) == 1 || atoi(argv[1]) == 2) {
            fprintf(stderr, "1\n");
            return 1;

        }
        else {

            pid=fork();
            if(pid == 0) {  

                // printf(" CHILD: Это процесс-потомок!\n");
                // printf(" CHILD: Мой PID -- %d\n", getpid());

                int new_int = atoi(argv[1]) - 1;

                file = fopen("/tmp/child1", "w");
                

                char new_int_to_char[15];
                snprintf(new_int_to_char, 10, "%d", new_int);

                // printf("%s var1\n", new_int_to_char);

                fputs(new_int_to_char, file);
                fclose(file);

                char * new_argv[3] = { "a.out", new_int_to_char, NULL };

                // printf("%s\n", new_argv);
                execvp(argv[0], new_argv);
                return 1;
            
            } else {
                pid2 = fork();
            }

            if(pid2 == 0) {

                // printf(" CHILD: Это процесс-второй-потомок!\n");
                // printf(" CHILD: Мой PID -- %d\n", getpid());

                int new_int = atoi(argv[1]) - 2;
                
                file = fopen("/tmp/child2", "w");
                

                char new_int_to_char[15];
                snprintf(new_int_to_char, 10, "%d", new_int);

                // printf("%s var2\n", new_int_to_char);

                fputs(new_int_to_char, file);
                fclose(file);

                char * new_argv[3] = { "a.out", new_int_to_char, NULL };
                
                // printf("%d\n", new_argv);
                execvp(argv[0], new_argv);
                return 1;
            }

            int status1, child1 = wait(&status1);
            int status2, child2 = wait(&status2);


            file1 = fopen("/tmp/child1", "r");
            file2 = fopen("/tmp/child2", "r");

            char buffer_child1[4];
            char buffer_child2[4];

            fgets(buffer_child1, 4, file1);
            fgets(buffer_child2, 4, file2);

            printf("%d\t%d\t%s\t%d\n", getpid(), child1, buffer_child1, WEXITSTATUS(status1));
            printf("%d\t%d\t%s\t%d\n", getpid(), child2, buffer_child2, WEXITSTATUS(status2));
            printf("%d\t\t\t%d\n", getpid(), (WEXITSTATUS(status1) + WEXITSTATUS(status2)));

            return (WEXITSTATUS(status1) + WEXITSTATUS(status2));

            
            
        }

    }
    

  	return 0;
}