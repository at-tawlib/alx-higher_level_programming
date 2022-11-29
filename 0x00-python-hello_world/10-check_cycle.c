#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly-linked list contains a cycle
 * @list: list to check
 * Return: returns 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (list == NULL || list->next == NULL)
		return (0);

	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		a = a->next;
		b = b->next->next;
	}

	return (0);
}
