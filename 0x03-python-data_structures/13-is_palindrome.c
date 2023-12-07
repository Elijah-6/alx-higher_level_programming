#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *prev_slow = NULL;
	listint_t *mid = NULL;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	prev_slow->next = NULL;

	reverse_list(&slow);
	result = compare_lists(*head, slow);
	reverse_list(&slow);

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = slow;
	}
	else
	{
		prev_slow->next = slow;
	}
	return (result);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 *
 * Return: 1 if lists are equal, 0 otherwise
 */

int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

