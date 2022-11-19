/*
2022.11.19 Today, I Learned
ABOUT Class & Struct
*/



/*
We can make something by using class and struct, and we call it Instance.
Plus, in case of class, we call it object instead of instance(Of course we can call it instance)
there are some differences between class and struct.
First, for class, the instance is saved in heap teritory. But struct's instance is saved in stack teritory.
Second,for class,  if we binding some values from properties, some values and original property both of them is pointing same memory address. So both of them changes.
But for the struct, it doesn't happen.
Third, for class, if you say "let" , it only applies to the memory address, not the value.

*/


/*
lazy var              => we call it "lazy property", to make it efficiently
static let/var        => we call it "type property", to access the Type it self.
*/