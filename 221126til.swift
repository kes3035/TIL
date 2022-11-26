/*
2022.11.26 Today, I Learned
ABOUT Class & Struct
*/



/*
Class 
-> if we declare initial value (Of stored properties) or declare it as an optional, automatically it makes init()
-> but if we declare init(), then it doesn't provide automatic init
-> if we want to call another initializer, we should name current initializer "convenience init()"
-> convenience initializer means call another initializer.
-> convenience initializer <=> designated initializer


inheretence rules

1. 
(1) delegate up
    Subclass's designated initializer should call superclass's designated initializer
    (it is process that initializing the subclass's stored properties and superclass's stored properties)

(2) delegate across
    Convenience initializer should call another convenience initializer or another designated initializer On the Same Class. Ultimatley, designated initializer.
    (Only designated initializer initialize all of stored properties on its class)

*/

/*
Struct
-> it automatically provides memberwise initializer(even if we don't declare initial value)
-> if you declare one of the stored properties, memberswise initializer provides one or all

*/