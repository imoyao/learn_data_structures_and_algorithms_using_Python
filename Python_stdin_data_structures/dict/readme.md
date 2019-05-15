`Python` 中第二个主要的数据结构是`dict`。`dict`与`list`的不同之处在于你需要通过一
个键（`key`）来访问元素，而不是通过`index`。
过现在我们要说的重点是，`dict`条目的访问和赋值都是`O(1)`的时间复杂度。`dict`的另一个重要的操
作是所谓的`in`。检查一个键是否存在于`dict`中也只需 `O(1)`的时间。

## `dict`内置操作的时间复杂度

| 操作           | 操作说明 | 时间复杂度 |
| ---------------- | --------- | ---------- |
| copy             | 复制    | O(n)       |
| get(value)       | 获取    | O(1)       |
| set(value)       | 修改    | O(1)       |
| delete(value)    | 删除    | O(1)       |
| item `in` dict_obj | `in`关键字 | O(1)       |
| iterration       | 迭代 | O(n)       |


## 更多阅读

[TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
