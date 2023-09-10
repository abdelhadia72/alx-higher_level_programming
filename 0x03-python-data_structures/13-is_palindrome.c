#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *last = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (last != NULL && last->next != NULL)
	{
		last = last->next->next;
		temp = first->next;
		first->next = prev;
		prev = first;
		first = temp;
	}

	if (last != NULL)
		first = first->next;

	while (first != NULL)
	{
		if (first->n != prev->n)
			return (0);
		first = first->next;
		prev = prev->next;
	}

	return (1);
}