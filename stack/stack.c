#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

stack create_stack(void) {
  static int indx = -1, size = 0;
  int * val;
  stack st = {
    val,
    indx,
    size
  };
  return st;
}

// check empty
int is_empty(stack * st) {
  if (st -> indx == -1)
    return 1;
  else
    return 0;
}

// push/append
void push(stack * st, int new_val) {
  st -> indx++;
  st -> val[st -> indx] = new_val;
  st -> size++;
}

// pop
void pop(stack * st) {
  if (is_empty(st)) {
    puts("\n\t stack IS EMPTY");
  } else {
    st -> indx--;
    st -> size--;
  }
}
