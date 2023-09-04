#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 *  * struct listint_s - Singly Linked List
 *   * @n: integer
 *    * @next: points to the next node
 *     *
 *      * Description: Singly Linked List Node Structure
 *       *  Holberton project
 *        */
typedef struct listint_s
{
		int n;
			struct listint_s *next;
} listint_t;
void free_listint(listint_t *head)
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
