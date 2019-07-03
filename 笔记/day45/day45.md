[TOC]



## 默写+内容回顾

### 1.伪类选择器

```css
a:link{} 没有被访问过时a标签的样式
a:visited{} 访问过后的
a:hover{} 悬浮时
a:active{} 摁住的时候
```

### 2.如何在p标签的后面添加''&'内容？

```html
<style>
    p::after{
        /*行内元素*/
        content:'&',
        color:red;
        font-size: 20px;
    }
</style>
<p>wusir</p>
```

### 3.设置网页字体使用哪个属性，备选字体如何写？

```css
font-family:'宋体','楷体';
```

### 4.如何设置文字间距和英文单词间距？

```css
文字间距:letter-spacing
英文单词间距:word-spacing
```

### 5.字体加粗使用哪个属性，它的取值有哪些？

```css
font-weight:lighter| normal | bold |bolder| 100~900 字体加粗
font-style:italic;/*斜体*/
```

### 6.文本修饰用哪个属性，它的取值有哪些？

```css
text-decoration:none| underline | overline | line-through
```

### 7.分别说明px，em,rem单位的意思

```
px: 绝对单位  固定不变的尺寸
em和rem :相对单位     font-size
	em:相对于当前的盒子
	rem:相对于根元素（html）
```

### 8.如何设置首行缩进，一般使用什么单位？

```
em
```

### 9.文本水平排列方式是哪个属性，它的取值有？

```css
text-align:left | center | right | justify(仅限于英文，两端对齐)
```

### 10.如何让一个盒子水平居中？

```css
盒子必须有宽度和高度，再设置margin: 0 auto;
让文本水平居中： text-align:center;
让文本垂直居中：line-height = height
```

### 11.margin在垂直方向上会出现什么现象？

```css
外边距合并，“塌陷”
尽量避免出现塌陷问题，只要设置一个方向的margin
```

### 12.如果让两个盒子并排在一行上显示？

```html
1.float浮动属性
2.设置盒子的显示方式 display:inline | inline-block;
```

### 13.简单阐述一下，浮动对盒子产生了什么现象？

```
1.脱离标准文档流，不在页面上占位置 “脱标”
2.文字环绕 设置浮动属性的初衷
3.“贴边” 现象： 给盒子设置了浮动，会找浮动盒子的边，如果找不到浮动盒子的边，会贴到父元素的边，如果找到了，就会贴到浮动盒子的边上
4.收缩效果

 有点像 一个块级元素转成行内块
```

## 今日内容：

### 浮动

布局方案

作用：实现元素并排

#### 	浮动的现象

- 脱离了标准文档流，不在页面上占位置
- 贴边现象
- 收缩效果

#### 	浮动的带来问题（撑不起父盒子的高度）

#### 	清除浮动的方式

- ````
  给父元素添加固定高度 （不灵活，后期不易维护）
  ````
  
  - 应用：万年不变导航栏
  
- ```
  内墙法：给最后一个浮动元素的后面添加一个空的块级标签，并且设置该标签的属性为clear:both;
  问题：冗余
  ```

- ```css
  伪元素清除法 推荐大家使用
  .clearfix::after{
      content:'';
      display: block;
      clear: both;
      /*visibility: hidden;*/
      /*height: 0;*/
  }
  ```

- ```
  overflow:hidden; 常用
  
  因为overflow:hidden;会形成BFC区域，形成BFC区域之后，内部有它的布局规则
  计算BFC的高度时，浮动元素也参与计算
  但是小心overflow：hidden它自己的本意
  ```

  

### 定位

```css
position:static | relative | absolute | fixed;
		 静态      相对        绝对        固定
```

#### 相对定位 relative

特征：

- 与标准文档流下的盒子没有任何区别
- 留“坑”，会影响页面布局

作用：

```
做“子绝父相”布局方案的参考
```

参考点：

```
以原来的盒子为参考点
```

#### 绝对定位 absolute

参考点

#####  如果单独设置一个盒子为绝对定位，

```
以top描述，它的参考点是以body的（0，0）为参考点
以bottom描述，它的参考点是以浏览器的左下角为参考点
```

##### 子绝父相

```
以最近的父辈元素的左上角为参考点进行定位
```

##### 特征

```
1.脱标
2.压盖
3.子绝父相
```

