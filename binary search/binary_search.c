#include <stdio.h>
#include <stdlib.h>

void swap(int * x, int * y) {
  int tmp = * x;
  * x = * y;
  * y = tmp;
}

void sorted(int * array, size_t len) {
  int i, j, min_idx;

  for (i = 0; i < len - 1; i++) {
    min_idx = i;
    for (j = i + 1; j < len; j++)
      if (array[j] < array[min_idx])
        min_idx = j;

    swap( & array[min_idx], & array[i]);
  }
}

void range_binary_search(int * array, int len, int val, int * res) {
  int right = 0;
  int left = 0;
  int middle;

  // not found
  if (val < array[0] || val > array[len - 1]) {
    right = 0;
    left = -1;
  }

  // found
  else {
    while (right < len) {
      middle = (right + len) / 2;
      if (val < array[middle])
        len = middle;
      else
        right = middle + 1;
    }
    len = right - 1;
    while (left < len) {
      middle = (left + len) / 2;
      if (val > array[middle])
        left = middle + 1;
      else
        len = middle;
    }
  }
  res[0] = left;
  res[1] = right - 1;
}
