#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;
	if (list == NULL)
		return (0);
	while (slow->next != NULL)
	{
		while (fast->next != NULL)
		{
			if (fast->next == slow)
				return (1);
			fast = fast->next;
		}
		slow = slow->next;
	}
	return (0);
}
