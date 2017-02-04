#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

int main()
{

  int fd = open("image.ppm", 0666 | O_CREAT | O_TRUNC | O_EXEC);
  
  
  
  return 0;
}
