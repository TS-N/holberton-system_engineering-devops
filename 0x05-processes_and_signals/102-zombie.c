#include <unistd.h>
#include <stdio.h>

/**
  * infinite_while - inf loop
  * Return: 0
  **/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
  * main - creates 5 zombie processes
  * Return: 0
  **/
int	main(void)
{
	pid_t	c;
	int	i = 0;

	while (i < 5)
	{
		c = fork();
		if (c == 0)
			return (0);
		printf("Zombie process created, PID: %u\n", c);
		++i;
	}
	infinite_while();
	return (0);
}
