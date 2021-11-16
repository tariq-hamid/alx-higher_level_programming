#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: list to be checked
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = NULL;
	listint_t *hare = NULL;

	if (list == NULL)
		return (0);
	tortoise = list;
	hare = tortoise->next;
	if (hare == NULL)
		return (0);
	hare = hare->next;
	while (tortoise != NULL && hare != NULL)
	{
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		if (hare->next == NULL)
			break;
		hare = (hare->next)->next;
	}
	return (0);
}