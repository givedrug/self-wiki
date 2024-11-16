
这几天苦逼的看汇编，做个小总结

**机器语言（debug环境）**

指令码：

```
E CS:0100 B4 09 BA 08 01 CD
E CS:0106 21 C3 48 45 4C 4C
E CS:010C 4F 20 57 4F 52 4C
E CS:0112 44 21 0D 0A 24 90
```

注：对ASCII码比较熟悉的明眼人，应该能看出二三四行中48 45 4C 4C……44 21分别对应HELLO WORLD!

有兴趣可以debug-u反汇编看看机器码和汇编码的对应关系。

![](assets/HELLO%20WORLD!/机器语言HW.jpg)

**汇编语言（masm5.0开发环境）**

代码：

```
DATA SEGMENT
  HWDB 'HELLO WORLD!'
DATA ENDS
CODE SEGMENT
 ASSUME CS:CODE,DS:DATA
START:
  MOV AX,DATA
  MOV DS,AX
  LEA BX,HW
  MOV CX,0CH
R:
  MOV AH,2
  MOV DL,[BX]
  INC BX
  INT 21H
 LOOP R
  MOV AH,4CH
  INT 21H
CODE ENDS
  ENDSTART
```

注：写这种小程序，貌似汇编还没有机器码方便~

![](assets/HELLO%20WORLD!/汇编语言HW.jpg)

**C 语言（MicrosoftVisual C++6.0开发环境下）**

代码：

```c
#include <stdio.h>
main()
{
    printf("HELLOWORLD!\n");
} 
```

注：这个大多数人很熟悉了，一个极简单的程序。充分体现了高级语言的优势。相对于只吃01代码的CPU，劳动人民万万岁啊~

![](assets/HELLO%20WORLD!/C语言HW.jpg)

2012-10-19
