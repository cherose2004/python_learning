[TOC]



## 内容回顾

### ECMAScript基础语法

#### 1.基本数据类型和引用数据类型

```
基本数据类型:number,string,boolean,undefined,null
引用数据类型:Array,Object,Function
```

#### 2.条件判断和循环

```js
switch(name){
	case 'xxx':
		break;
    case 'xxx':
		break;
    default:
        break;
}

for(var i = 0; i < 10; i ++){
    
}

三元运算
1 > 3 ? '真的' : '假的';
```

#### 3.赋值运算符，逻辑运算符

```
&&  跟py的and
||   or
!    not

i++

==   比较的值的
===   比较的值和数据类型
```

#### 4.字符串的常用方法

```js
slice() 切片，有一个参数，从当前位置切到最后，两个参数，顾头不顾尾
substring()
substr() 如果有两个参数，第二个参数表示切字符串的个数

拼接字符串
concat() 返回新的字符串
+
es6的模板字符串
``  插入变量用${变量名}

//获取索引
indexOf()
lastIndexOf()

//获取字符
charAt()
//获取字符的ASCII码
charCodeAt()


//转大写
toUppercase()
//转小写
tolowercase()


typeof 校验当前变量的数据类型

trim() 清除左右的空格

```

#### 5.数组的常用方法

```
toString()
join('*')
concat()

//栈方法 后进先出
push()
pop()

//堆方法 先进先出
unshift()
shift()


splice(起始位置，删除的个数，添加的元素)； 对数组的增加，删除，替换
slice()
reverse()
sort()


//迭代方法
for
forEach() 仅能在数组对象中使用
在函数中arguments 这个对象是伪数组


```

#### 6.对象

```js
var obj = {
	  name:'mjj',
	  age:18
}
obj['name']
obj['fav'] = function(){}
obj.name
obj.fav = function(){}


function fn(name){
    var obj = {};
    obj[name] = 'mjj';
    return obj;

}
fn('age')

//遍历对象
for(var key in obj){
    obj[key]
}
```

#### 7.函数

```js
1.创建方法
（1）普通函数
   function fn(){
       
   }
   fn();
(2)函数表达式
  var fn = function(){}
  
 (3) 自执行函数
 ;(function(){
    this指向 一定是指向window
 })()

全局作用域下，函数作用域，自执行函数都指向了window,函数作用域中this指向可以发生改变，可以使用call()或者apply()


var obj = {name：'mjj'};
function fn(){
    console.log(this.name);
}
fn();//是空值，因为函数内部this指向了window
fn.call(obj)//此时函数内部的this指向了obj


作用： 解决冗余性代码，为了封装


构造函数
new Object();
new Array();
new String();
new Number();


//使用构造函数来创建对象
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function () {
  return '(' + this.x + ', ' + this.y + ')';
};

var p = new Point(1, 2);

//es6用class来创建对象
class Person{
    constructor(x,y){
        this.x = x;
        this.y = y
    }
    toString(){
        
    }
    
}
var p = new Person();
```

#### 8.日期对象

```
var date = new Date();
date.getDate();
date.getMonth();
date.getDay();
date.getHours();
date.getMinutes();
date.getSeconds()

date.toLocaleString() 2018/08/21 21:30:23
```

#### 9.Math数学对象

```
Math.ceil();向上取整 天花板函数
Math.floor();向下取整，地板函数
Math.round()；标准的四舍五入

随机数
Math.random(); 获取0到1之间的数

function random(min,max){
	return Math.floor(Math.random()*(max-min)) + min;
}
```

#### 10.数值和字符串转换

```js
1.数值转字符串
toString();
数字+空的字符串
2.字符串转数值
parseInt() 转整数
parseFloat() 转浮点型
Number()
```



```
var a = NaN
isNaN(a)

Infinity 无限大的
```

## 今日内容

### BOM

Browser Object Model

#### 1.系统对话框方法

- alert()
- confirm()
- prompt()

#### 2.定时方法 **

**一次性任务**

```js
var timer = setTimeout(callback,2000);
clearTimeout(timer);
```



**周期性循环**

```js
var timer = setInterval(callback,2000);
//清除定时器 关闭
clearInterval(timer);
```



#### 3.location对象的属性和方法

### DOM  

#### 获取节点对象的方式

```js
document.getElementById();
document.getElementsByTagName();
document.getElementsByClassName();
```

#### 对样式操作

```
box.style.color
box.style.backgroundColor
box.style.width
....
```

#### 对属性设置

```js
setAttribute(name,value);
getAttribute(name);
```



#### 事件

```js
onclick
onmouseover()
onmouseout()
```









