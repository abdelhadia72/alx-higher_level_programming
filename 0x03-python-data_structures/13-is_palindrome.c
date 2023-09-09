#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *first = *head;
	listint_t *last = *head;
	int len = 0;
	int len_node;
	int i = 0;
	int j = 0;

	if (!(*head))
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	len_node = len;
	for (i = 0; i < len / 2; i++)
	{
		len_node--;
		last = *head;
		for (j = 0; j < len_node; j++)
		{
			last = last->next;
		}

		if (first->n != last->n)
		{
			return (0);
		}
		first = first->next;
	}

	return (1);
}
