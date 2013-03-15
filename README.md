Django Custom Project Layout Sample
===================================

This sample project is an experiment to prove
several possible django project layouts. 

This time I made two django projects: one that works with the 
ASP.NET MVC's convention over configuration style and the
other that works like a normal django app. Both do the exact
same thing, but are layed out in different ways.

At the urls.py file you will notice that there is just three routes
configured: a default controller call, the *NetMVC* routes configuration
and the *traditional* routes configuration.

If you look at the *NetMVC/* folder, you'll see that is organized
like any .NET MVC project, with a models, views and controllers
folders.

If you look at the *traditional/* folder, you'll find that it is organized
like any typical django project.

## How does this work?

All the magic tricks occurs in the django_utils/ folder which has just
three files, convention.py, net_mvc.py and traditional.py. Looking at the net_mvc.py 
or  traditional.py file you may see the posibilities, you can create a lot of possible 
project layouts by just implementing the abstract class at the conventions.py module.

Here is an article about how do this work: https://github.com/JeyDotC/articles/blob/master/Making%20django%20urls%20work%20by%20convention.md

## Notes

Many may state that I'm reinventing the wheel, I gess that there are other
libraries with this same purpose already. Well, reinventing the wheel is my very
personal way to learn how wheels work and how to use them, that's why I do it ;)