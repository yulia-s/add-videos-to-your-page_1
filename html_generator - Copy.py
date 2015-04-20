# Stage 2 by Yulia

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text


def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
LIST_OF_CONCEPTS = [ ['Lists', 'Lists are very powerful data structure. It is an ordered collection of objects.'],
                             ['For Loop', 'For Loops allow you to iterate over lists'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    res = ''
    for row in list_of_concepts:
        concept_title = row[0]
        concept_description = row[1]
        res += generate_concept_HTML(concept_title, concept_description)
    return res



print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)

LIST_OF_CONCEPTS_2 = [ ['OOP', 'Python provides full support for OOP. Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. One of the principal advantages of object-oriented programming techniques over procedural programming techniques is that they enable programmers to create modules that do not need to be changed when a new type of object is added. A programmer can simply create a new object that inherits many of its featuresfrom existing objects. This makes object-oriented programs easier to modify.'],
['Important terms','''What Is an Object?

An object is a software bundle of related state and behavior. Software objects are often used to model the real-world objects that you find in everyday life. 

What Is a Class?

A class is a blueprint or prototype from which objects are created. 

An object is an instance of a class - it's a concrete 'thing' that you made using a specific class. So, 'object' and 'instance' are the same thing, but the word 'instance' indicates the relationship of an object to its class.

Method - is a function which is a member of a class.

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable ­­__name__.

In computer science, a library is a collection of non-volatile resources used by computer programs, often to develop software. These may include configuration data, documentation, help data, message templates, pre-written code and subroutines, classes, values or type specifications.

'''],
['Instance VS Class variables', ''' Instance variables belong to an instance of a class. Another way of saying that is instance variables belong to an object, since an object is an instance of a class.

Class variables, however, only have one copy of the variable(s) shared with all instances of the class. It’s important to remember that class variables are also known as static member variables in C++, Java, and C#. 
'''],
['Inheritance and method overriding', ''' Object-oriented programming allows classes to inherit commonly used state and behavior from other classes. 

What is overriding? Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors.

Overriding is a very important part of OOP since it is the feature that makes inheritance exploit its full power. Through method overriding a class may "copy" another class, avoiding duplicated code, and at the same time enhance or customize part of it. Method overriding is thus a strict part of the inheritance mechanism.
'''],
['OOP and other disciplines','''There is a strong connection between OOP, HTML and CSS. As with any object-based coding method, the purpose is to encourage code reuse and, ultimately, faster and more efficient stylesheets that are easier to add to and maintain.

Almost every element on a styled Web page has different visual features (i.e. “skins”) that are repeated in different contexts. On the other hand, other generally invisible features (i.e. “structure”) are likewise repeated.

When these different features are abstracted into class-based modules, they become reusable and can be applied to any element and have the same basic result.
 ''']]
#print make_HTML_for_many_concepts(LIST_OF_CONCEPTS_2)
