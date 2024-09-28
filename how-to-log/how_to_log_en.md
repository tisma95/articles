---
title: How to make logs useful?
author: Ismaël Maurice
date: 09/28/2024
---

<img src="./img/splash.jpg" alt="" width="100%" height="500px" />

[Image Source](https://unsplash.com/en/photos/ordinateur-portable-noir-allume-f5pTwLHCsAg)

# How to make logs useful?

As developers, logs are the expressive part of our application. They allow us to capture the activity of an application.

In computer programming, a developer can decide whether to display logs in his application, which can be a traceability aid in the event of errors.

The problem now is to know what to display and where, hence the purpose of this article.

## Logs in a single function

By definition, a function receives one or more parameters as input, then performs operations and returns a result.

<img src="./img/en/1. architecture.png" alt="Function architecture" width="50%" />

In a simple function, the useful information's to be displayed in the logs are:

- The parameter(s) the function receives.
- Result after operations (optional, useful when you have a sequence of function calls).

For example, for a function that takes no parameters and returns the message 'Hello' we would have in Python:

<img src="./img/en/3. func_no_parameter.png" alt="Log of a function without parameters" width="50%" />

Suppose the function took a name as parameter and returned “Hello username”, we'd have:

<img src="./img/en/4. func_with_parameter.png" alt="Log function with parameters" width="50%" />

If we want to display the result of the function in the logs we would have:

<img src="./img/en/5. func_with_parameter_and_response.png" alt="Log function with parameters and result" width="50%" />

**When parameters contain confidential information such as email and password, these should not be displayed in the logs and should be replaced by \*\*.**

## Logs in a sequence of functions

A computer program is a sequence of functions and methods that call each other. Let's assume a program consisting of 3 functions: _function A_, _function B_ and _function C_, with the following stack:

<img src="./img/en/2. architecture_multiple.png" alt="Multi-function call architecture" width="50%" />

When you have several functions, the logs should look like this:

- The calling function must display its parameters when called.
- After executing another function, the calling function must display the result obtained.
- The calling function can display the returned result.

Let's say a **main** function calls a **getName** function and, with the name entered by the user, calls a **hello** function to display the message 'Hello username'.

If we want to apply the logs in this sequence of functions, we would have:

<img src="./img/en/6. func_multiple_call.png" alt="Log of a sequence of functions" width="50%" />

Execution would give :

<img src="./img/en/7. example.png" alt="Log d'une suite de fonctions exécution" width="50%" />

**In the previous examples, we used the print function to display logs. In your projects, you should use log modules from your own language. In Python, you can use [Logging](https://docs.python.org/3/library/logging.html).**

**The techniques described above can be adapted to suit your needs.**

**When parameters contain confidential information such as email and password, these should not be displayed in the logs and should be replaced by \*\*.**
