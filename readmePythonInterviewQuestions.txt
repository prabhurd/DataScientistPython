1. What is Python?
    - Object Oriented Programming Language
    - Widely used in data science, AI and ML
    - Also used in Web Development, Software Development, Mathematics, System Scripting

2. What are the applications of Python?
    - Web Development [Frameworks: Django, Pyramid, Flask]
    - Scientific and Mathematical Application [Frameworks: SciPy and NumPy]
    - Image Processing and Graphic Design Application
    - Enterprise Application

3. What are the advantages of Python?
    - Free and Open Source
    - Built-in data structure
    - Cross-platform
    - Object-oriented
    - Interpreted

4. What is PEP8?
    - Python Enhancement Proposals
    - Guidelines on how to write the Python code

5. What do you mean by Python literals?
    - Data which is given in a variable or constant
    - String, Boolean, Numerical

6. Explain Python Function?
    - Make programming more functional and modular to perform modular tasks
    - It helps to achieve code re-usability
    - Built-In Functions: len(), copy(), count()
    - User-defined Functions:

7. What is zip() function in Python?
    - Python zip() function returns a zip object
    - Which maps a similar index of multiple containers
    - Zip function takes n number of iterators
    - whichever has less lenght it will considered for mapping

8. What is Python's parameter passing mechanism?
    - Pass By Value: Passes an argument by value [Eg: a = 5]
    - Pass By Reference: Passes an argument by reference [Eg: list = ["a","b"]]

9. How to overload constructors or methods in Python?
    - We cannot overload constructors or methods in Python
    - Constructor: is called automatically when an object is created
    - Methods: will be called for the instance of an object

10. What is the difference between remove() function and del statement?
    - Use remove() - to delete specific object in the list [list.remove()]
    - del statement - used to delete object or delete a object in list [del list[0]]

11. What is swapcase() function in the Python?
    - Converts all characters to upper case to lower case and vice versa

12. How to remove whitespaces from a string in Python?
    - Use str strip() to remove whitespaces from a string

13. How to remove leading whitespaces from a string in the Python?
    - Use str lstrip() to remove whitespaces from a string

14. Why do we use join() function in Python?
    - It concatenates the string
    - String method
    - It concatenates the list or string with defined string

15. Give an example of shuffle() method?
    - random.shuffle()
    - This method shuffles the given array
    - It randomizes the items in the array

16. What is the use of break statement?
    - It is used to terminate the execution of the current loop.

17. What is tuple in Python?
    - Tuple is a built in data structure
    - Stores value in Sequence and value cannot be changed (Immutable)
    - it denoted by ()

18. Which are the file related libraries/modules in Python?
    - os and os.path - modules include a function for accessing the filesystem
    - shutil - module enables you to copy and delete the files

19. What are the different file processing modes supported by Python?
    - Read-only mode : Open a file for reading. It is the default mode.
    - Write-only mode: Open a file for writing. If the file contains data, data would be lost. Other a new file is created.
    - Read-Write mode: Open a file for reading, write mode. It means updating mode.
    - Append mode: Open for writing, append to the end of the file, if the file exists.

20. What is an operator in Python?
    - Unary [!, -]
    - Binary [+, - , /]
    - Ternary [?, :]

21. What are the different types of operators in Python?
     - Arithmetic Operator [+, - , * , /]
     - Relational Operator [ >, <, == ]
     - Logical Operator [and, or, not]
     - Assignment Operator [=, +=, -=, *=, **=]
     - Membership Operator [in, not in]
     - Bitwise Operator [&, |,  ^, ~]

22. How to create a Unicode string in Python?
    - The string is treated as Unicode by default
    - we can use art.title.encode("utf-8") function

23. Is Python interpreted language?
    - Yes, Python is interpreted language
    - The Python language program runs directly from the source code.
    - It converts the source code into an intermediate language code,
    - which is again translated into machine language that has to be executed.
    - It has no compiler like Java or C

24. How is memory managed in Python?
    - The Python memory is managed by a Python private heap space
    - We can easily allocate heap space for Python objects by the Python memory manager
    - Python also has an inbuilt garbage collector

25. What is the Python decorator?
    - Change the behaviour of existing function (without changing code in function)
    - Functions vs. Decorators
    - Function: is a block of code that performs a specific task w
    - Decorator: is a function that modifies other functions
    - https://www.youtube.com/watch?v=yNzxXZfkLUA&ab_channel=Telusko
    - https://www.youtube.com/watch?v=r7Dtus7N4pI&ab_channel=Kite (Must Watch)
    - https://realpython.com/primer-on-python-decorators/#functions

26. What are the rules for a local and global variable in Python?
    - Local variables are accessible within local body/function only
    - Global variables are accessible anywhere in the program,
                and any function can access and modify its value.
    - https://www.youtube.com/watch?v=QYUbLevwgDQ&ab_channel=Telusko
    - https://www.youtube.com/watch?v=pzNISmtmzcY&ab_channel=Telusko

27. What is the namespace in Python?
    - The namespace is a fundamental idea to structure
        and organize the code that is more useful in large projects.
    - A namespace is defined as a simple system to control the names in a program.
    - It ensures that names are unique and won't lead to any conflict.
    - https://www.youtube.com/watch?v=1RuMJ53CKds&ab_channel=Telusko

28. What are iterators in Python?
    - Iterators are used to iterate a group of elements, containers like a list
    - Python iterator implements __itr__ and next() method to iterate the stored elements.
    - __itr__()
    - __next__()
    - In Python, we generally use loops to iterate over the collections (list, tuple).

29. What is a generator in Python?
    - The generator is a way that specifies how to implement iterators
    - It is a normal function except that it yields expression in the function
    - It does not implements __itr__ and next() method and reduce other overheads as well
    - If a function contains at least a yield statement, it becomes a generator.
    - The yield keyword pauses the current execution by saving its states
        and then resume from the same when required.

30. What is slicing in Python?
    - Slicing is a mechanism used to select a range of items
        from sequence type like list, tuple, and string.
    - It requires a : (colon) which separates the start and end index of the field.

31. What is a dictionary in Python?
    - The Python dictionary is a built-in data type
    - one-to-one relationship between keys and values
    - The keys are unique whereas values can be duplicate

32. What is Pass in Python?
    - Pass specifies a Python statement without operations
    - If we want to create an empty class or functions,
        this pass keyword helps to pass the control without error.

33. Explain docstring in Python?
    - The Python docstring is a string literal that occurs
        as the first statement in a module, function, class, or method definition.
    - It provides a convenient way to associate the documentation.

34. What is a negative index in Python?
    - Python sequences are accessible using an index
        in positive and negative numbers.
    - Negative index traverse from right to left
        and iterate one by one till the start of the list.
    - A negative index is used to traverse the elements into reverse order.

35. What is pickling and unpickling in Python?
    - The Python pickle is defined as a module which accepts any Python object
        and converts it into a string representation.
    - It dumps the Python object into a file using the dump function;
        this process is called pickling.
    - The process of retrieving the original Python objects
        from the stored string representation is called as Unpickling.

36. Which programming language is a good choice between Java and Python?
    - Python has advantage in below things
    - Ease of Use
    - Coding Speed
    - Dynamic Data Type
    - Data Science and Machine learning application

37. What is the usage of help() and dir() function in Python?
    - Help() function: The help() function is used to display the documentation string
        and also facilitates us to see the help related to modules, keywords, and attributes.
    - Dir() function: The dir() function is used to display the defined symbols.

38. How can we make forms in Python?

39.

40. What are the differences between Python 2.x and Python 3.x?
   - Python3 it is Unicode

41. How can you organize your code to make it easier to change the base class?

42.

43. How Python does Compile-time and Run-time code checking?

44. What is the shortest method to open a text file and display its content?

45. What is the usage of enumerate () function in Python?

46. Give the output of this example: A[3] if A=[1,4,6,7,9,66,4,94].

47. What will be the output of ['!!Welcome!!']*2?

48. What will be the output of data[-2] from the list data = [1,5,8,6,9,3,4]?

49. How to send an email in Python Language?

50. What is the difference between list and tuple?

51. What is lambda function in Python?

52. Why do lambda forms in Python not have the statements?

53. How can you convert a number to string?

54. Mention the rules for local and global variables in Python?















Pickle Unpickle
https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex