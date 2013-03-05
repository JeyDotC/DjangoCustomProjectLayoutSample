Django Custom Project Layout Sample
===================================

This sample project is an experiment to prove
several posible django project layouts. 

This time I made a django project that works like 
ASP.NET MVC's convention over configuration style by 
using an old known PHP pattern, the bootstrap pattern
(or front controller if you rather it), so, all requests
passes through a single function which in time resolves
the controller (just a module located at an specific place)
and executes it.

At the urls.py file you will notice that there is just two routes
configured, a default controller call and the bootstrap call.

If you look at the my_app/ folder, you'll see that is organized
like any .NET MVC project, with a models, views and controllers
folder.

All the magic tricks occurs in the django_utils/ folder which has just
two files, the convention.py and the net_mvc.py. Looking at the net_mvc file
you may see the posibilities, you can create a lot of possible project
layouts by just implementing the abstract class at the conventions.py module.

This project is just an experiment and is not intended to derogate the standard
way of doing applications in django, in fact, it emerged because I'm too lazy
to write url configurations for each single view and wanted to use a 
conventions system. 

Many may state that I'm reinventing the wheel, I gess there are other
libraries with this same purpose already. Well, reinventing the wheel is my very
personal way to learn how wheels work and how to use them.