# 哈希表
Hashtable又称为散列表，是基于键的哈希代码组织起来的键值对
主要用来提高数据查询的效率
使用键来访问元素
## 定义哈希表
```
Hashtable hash = new Hashtable();
// key和value都是object
```
## 增删查改
### 增
```
hash.Add(1,"123");
hash.Add("123",1);
```
### 删
```
hash.Remove(1);
hash.Remove(2);//不存在的key不报错
hash.Clear();//直接清空
```
### 查
```
hash[1];//return "123"
hash[2];//不存在return null
// return 布尔类型
hash.Contains(key);
hash.ContainsKey(key);
hash.ContainsValue(value);
```
### 改
```
hash[1] = 1234；
```
## 遍历
### 遍历所有键
```
foreach(object item in hash.Keys){
    Console.WriteLine(item);
}
```
### 遍历所有值
```
foreach(object item in hash.Values){
    Console.WriteLine(item);
}
```
### 遍历键值对
```
oreach(DictionaryEntry item in hash){
    Console.WriteLine(item.Key);
    Console.WriteLine(item.Value);
}
```
### 迭代器遍历法
```
IDictionaryEnumerator myEnumerator = hash.GetEnumerator();
bool flag = myEnumerator.MoveNext();
while(flag){
    Console.Write(myEnumerator.Key + myEnumerator.Value);
    flag = myEnumerator.MoveNext();
}
