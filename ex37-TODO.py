''' 

这节复习符号

关键字：
and 	逻辑与
del 	删除对象属性
from    引用包名
not 	逻辑非
while 	循环
as 		with...as... 连用
		用法：
			with func() as name:
				data = name

		说明：
			1.先调用 func().__enter__()
			2.语句
			3.func().__exit__()
		例子：
			－－－－－－
			class Sample:
				def __enter__(self):
					print "In __enter__()"
					return "Foo"

				def __exit__(self, type, value, trace):
					print "In __exit__()"

			def get_sample():
				return Sample()

			with get_sample() as sample:
				print "sample:", sample

			执行结果:
			In __enter__()
			sample: Foo
			In __exit__()

			－－－－－－
elif
global
or
with
assert 断言：
		不满足assert条件，就会有assert异常
		例：
			assert n == 2
			n = 1 # 抛异常
			n = 2 # 无异常
else
if
pass
yield 	TODO
break
except 	TODO
import
print
class
exec 	TODO
in
raise 	TODO
continue
finally TODO
is 		TODO
return
def
for
lambda 	TODO
try 	TODO

数据类型：
True
False
None
strings TODO
numbers TODO
floats 	TODO
lists 	TODO

字符串转义序列:
\\
\'
\"
\a 		TODO
\b 		TODO
\f
\n
\r
\t
\v 		TODO

字符串格式化:
%d
%i
%o
%u
%x
%X
%e
%E
%f
%F
%g
%G
%c
%r
%s
%%

操作符
+
-
*
**
/
//
%
<
>
<=
>=
==
!=
<>
()
[]
@
,
:
.
=
;
+=
-=
*=
/=
//=
%=
**=

'''
