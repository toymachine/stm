#include "mm.h"

void stm_init(void)
{
  GC_INIT();
}

void *stm_malloc(size_t size)
{
  return GC_MALLOC(size);
}

void *stm_realloc(void* ptr, size_t size)
{
  return GC_REALLOC(ptr, size);
}
