## 内容回顾+默写

### 1.浮动有哪些现象？

```
1.脱离标准文档刘
2.贴边
3.收缩
4.文字环绕
```

**浮动带来问题**：不去计算浮动元素的高度，导致撑不起父盒子的高度

### 2.清除浮动的方式？

```
1.给父盒子添加固定高度
2.内墙法：给最后一个浮动元素添加一个空的块级标签，设置该标签的属性为clear:both;
3.伪元素清除
 给父元素添加一个类
 .clearfix::after{
 	content:'',
 	display:block;
 	clear:both
 }
4.overflow:hidden; BFC区域
```

### 3.overflow:hidden和overflow:scroll属性的作用？

```
overflow:hidden;超出部分隐藏
overflow:scroll;出现滚动条

清除浮动
```

### 4.定位有哪几种？

```
position: static | relative | absolute | fixed
```



### 5.相对定位的元素有哪些特征？它的参考点是谁？

```
1.给一个标准文档流下的盒子单纯的设置相对定位，与普通的盒子没有任何区别
2.top|bottom|left|right

参考点：以原来的位置为参考点
应用：1.微调元素 2.做“子绝父相”
```

### 6.绝对定位的元素由哪些特征？它的参考点？

```
现象：
    1.脱标
    2.压盖现象
参考点：
是否有定位（相对定位，绝对定位，固定定位）的祖先盒子进行定位，如果没有定位的祖先盒子，以body为参考点

重要： “子绝父相”
```



### 7.阐述一下，“子绝父相”布局方案的好处



要浮动一起浮动，有浮动清除浮动，浮动带来的好处：实现元素并排

## 今日内容

### 固定定位

```
1.脱标
2.固定不变
3.提高层级

参考点：
	以浏览器的左上角为参考点
```



### z-index

只适用与定位的元素，z-index:auto;

```
z-index只应用在定位的元素，默认z-index:auto;
z-index取值为整数，数值越大，它的层级越高
如果元素设置了定位，没有设置z-index，那么谁写在最后面的，表示谁的层级越高。(与标签的结构有关系)
从父现象。通常布局方案我们采用子绝父相，比较的是父元素的z-index值，哪个父元素的z-index值越大，表示子元素的层级越高。
```

### background背景

```css
/*设置背景图*/
background-image: url("xiaohua.jpg");
background-repeat: no-repeat;
/*调整背景图的位置*/
background-position: -164px -106px;
```

### border

```
border-radius 设置圆角或者圆
```

### 阴影

```css
box-shadow: 水平距离 垂直距离 模糊程度 阴影颜色 inset
```



### 行内的水平和垂直居中

### 块的水平和垂直居中

链接：[https://book.apeland.cn/details/355/#8.%E7%BD%91%E9%A1%B5%E4%B8%AD%E7%9A%84%E5%B8%B8%E7%94%A8%E9%97%AE%E9%A2%98](https://book.apeland.cn/details/355/#8.网页中的常用问题)

## 周末作业

1.脑图 主要

2.小米商城 主要

3.预习 ： <https://book.apeland.cn/details/358/>