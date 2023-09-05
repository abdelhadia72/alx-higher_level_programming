#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node in a sorted listint_t linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: Value to be inserted in the new node.
 * Return: Address of the new node, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		listint_t *current = *head;

		while (current->next && current->next->n <= number)
		{
			current = current->next;
		}

		new_node->next = current->next;
		current->next = new_node;
		return (new_node);
	}
}
