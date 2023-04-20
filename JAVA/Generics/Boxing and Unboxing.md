#### Boxing:
- Conversion of a primitive type to the corresponding reference type


#### Unboxing :
- Conversion of the reference type to the corresponding primitive type


```java
List<Integer> ints = new ArrayList<Integer>();
ints.add(1);
int n= ints.get(0);
```

_The above code is equivalent to: _

```java
List<Integer> ints = new ArrayList<Integer>();
ints.add(Integer.valueOf(1));
int n = ints.get(0).intValue();
```


```java
public static int sum(List<Integer> ints){
	int s = 0;
	for(int n : ints){
		s += n;
	}
	return s;
}
```


__Q:__ Why does argument have type `List<Integer>` and not `List<int>` ?
__Ans__: Because type parameters must always be bound to refernce types. not primitive types.

__Q:__ Why does the result have type int and not Integer?
__Ans:__ Because result types may be either primitive or refernce types, and if is more efficient to use the former than the latter. 


Unboxing occurs when each `Integer` in the list is bound to the variable `n` of type `int`.

#### Recommended:
> Never to use `==` to compare values of type `Integer`. Either unbox first, so `==` compares values of type `int`, or else use `equals` to compare values of type `Integer`.


