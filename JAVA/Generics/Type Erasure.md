- Generics are used for tighter type checks at compile time and to provide a generic programming. To implement generic behaviour, java compiler apply type erasure. 
- Type erasure is a process in which compiler replaces a generic parameter with actual class or bridge method. In type erasure, compiler ensures that no extra classes are created and there is no runtime overhead.

## Type Erasure rules
-   Replace type parameters in generic type with their bound if bounded type parameters are used. 
-   Replace type parameters in generic type with Object if unbounded type parameters are used.
-   Insert type casts to preserve type safety.
-   Generate bridge methods to keep polymorphism in extended generic types.

