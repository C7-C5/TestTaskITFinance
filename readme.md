This is a test task for the company IT Finance.
The task consisted of three tasks:

Task #1
Get the value of the parameter clickid from the url: https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE

Task #2
It is necessary to go to the website https://ptable.com/?lang=ru and obtain all the elements of the periodic table in the form of a list of instances of the class Chemical_element. The instance of the class should contain the following attributes:
atomic: The atomic number in the table
name: The name of the element
weight: The atomic mass of the element
To solve this problem, any tool for automating actions in the web browser is suggested (for example, Selenium or Playwright).

Task #3
There is a test website http://qa.test/ located physically at IP 84.201.186.26. Since this is a test site that cannot be shown to the client yet, it is not possible to access this site just like that :)
The first level of difficulty is to open this site from a computer.
The second level of difficulty is to open this site from a mobile phone.

The tasks were solved by me in the following way.
Task #1
I chose the most obvious, in my opinion, option to split the string by the given parameters using the split() string method.

Task #2
To solve this task, I used @dataclass, which, firstly, allowed me to reduce the code base, albeit insignificantly in this case, and, secondly, elegantly solved the issue of collecting class instances into a list.

Task #3
This repository contains the code for solving the first part of the task, and the answer to the second part will be sent directly to the recruiter, as the solution to the second part did not involve writing any code.