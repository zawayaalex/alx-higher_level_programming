#include "lists.h"

/**
 * check_cycle - check for loop in Linked List
 * @list: head of linked list
 * Description - check for loops in Linked List
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *low, *high;

	if (!list)
	{
		return (0);
	}
	low = list;
	high = list->next;
	while (high && low && high->next)
	{
		if (low == high)
		{
			return (1);
		}
		low = low->next;
		high = high->next->next;
	}
	return (0);
}
