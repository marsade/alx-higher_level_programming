#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - function in c that insert a number into a sorted singly
 * linked list
 * @head: the pointer to the first node in the list
 * @number number to be in new node
 * Return: the address of the new node or NULL if it falied
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *node;
	listint_t *temp;

	ptr = *head;
	temp = ptr->next;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	while (ptr->next != NULL)
	{
		if (node->n <= ptr->n)
		{
			node->next = *head;
			*head = node;
			return (node);
		}
		else if ((node->n >= ptr->n) && (node->n <= temp->n))
		{
			ptr->next = node;
			node->next = temp;
			return (node);
		}
		ptr = ptr->next;
		temp = ptr->next;
	}
	add_nodeint_end(&*head, number);
	return (NULL);
}



