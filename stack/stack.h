// initialize a stack (LIFO)
struct stck{
    int *val;
    int indx;
    int size;
};

typedef struct stck stack;
stack create_stack(void);
int is_empty(stack *st);
void push(stack *st, int new_val);
void pop(stack *st);
