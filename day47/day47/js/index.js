
//1.测试语句
// console.log('hello world');
// alert('hello world');
// console.log(window);
// var name = prompt('请输入今天的天气？');
// console.log(name);

//2.变量
//2.1基本数据类型
//number  string Boolean undefined(未定义的) null
//ctrl+shift+/ 多行注释
/*var a = 2;
var b = '2' + a;
var c = true;
console.log(typeof b);

//先声明后定义
var e;
console.log(e);//值 undefined
console.log(typeof e);//类型 是undefined
var f = null;
console.log(f);
console.log(typeof  f);*/
//2.2 引用数据类型
//Array  Object  function

var arr = ['郭旭🐏','任世🐉'];
console.log(arr);


//js中 全局作用域和函数作用域
//1.普通函数的声明
function add(a,b){
    return a + b
}

//2.函数表达式
var add2 = function(){

};
//自执行函数
;(function(){
    alert(1111);
})();


console.log(add(2, 4));

//定义在对象中的函数，叫做对象的方法
var obj = {
    name:'mjj',
    age:19,
    fav:function () {
        console.log(this);
    }
};
obj.fav();

