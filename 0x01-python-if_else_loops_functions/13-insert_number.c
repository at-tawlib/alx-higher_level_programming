#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node by sorting it in a singly linked list
 * @head: head of node
 * @number: number to insert
 * Return: address of node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if (number < current->n)
			{
				new->next = current;
				*head = new;
				return (new);
			}
			if ((number >= current->n) && (number <= current->next->n))
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
		new->next = NULL;
	}

	return (new);
}
