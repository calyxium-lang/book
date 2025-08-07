# Introduction

Welcome to _The Calyxium Programming Language_, an introductory book about Calyxium. The Calyxium programming language helps you write faster, reliable software. High-level ergonomics with purity, safety, and speed.

## Who Calyxium is For
Calyxium is ideal for many people for a variety of reasons. Let’s look at a few of the most important groups.

### Students
Calyxium is for students and those who are interested about learning functional programming concepts. Using Calyxium, many people have learned about topics like expression based languages, immutable variables and polymorphism.  The community is very welcoming and happy to answer student questions. Through efforts such as this book, the Calyxium teams want to make functional concepts more accessible to more people, especially those new to programming.

## who Is This Book For

This book assumes that you’ve written code in another programming language but
doesn’t make any assumptions about which one. We’ve tried to make the material
broadly accessible to those from a wide variety of programming backgrounds. We
don’t spend a lot of time talking about what programming _is_ or how to think
about it. If you’re _entirely_ new to programming, you would be better served by
reading a book that specifically provides an introduction to programming. 
Don't feel threatened if you are new however, as it can be a good brain exercise,
and you are also challenging yourself to do something new. Not a lot of people
are doing that these days!

## How to Use This Book

In general, this book assumes that you’re reading it in sequence from front to
back. Later chapters build on concepts in earlier chapters, and earlier
chapters might not delve into details on a particular topic but will revisit
the topic in a later chapter.


You’ll find two kinds of chapters in this book: concept chapters and project
chapters. In concept chapters, you’ll learn about an aspect of Calyxium. In project
chapters, we’ll build small programs together, applying what you’ve learned so
far. Chapters 2, 12, and 21 are project chapters; the rest are concept chapters.

Chapter 1 explains how to install Calyxium, how to write a `“Hello, world!”` program.

Chapter 2 is a hands-on introduction to writing a program in Calyxium, having you build up a
number guessing game. Here we cover concepts at a high level, and later
chapters will provide additional detail. If you want to get your hands dirty
right away, Chapter 2 is the place for that. 

Chapter 3 covers Calyxium's features
that are similar to those of other programming languages. If you’re a particularly meticulous
learner who prefers to learn every detail before moving on to the next, you
might want to skip Chapter 2 and go straight to Chapter 3, returning to Chapter
2 when you’d like to work on a project applying the details you’ve learned.

Chapter 5 discusses classes, structs and methods, and Chapter 6 covers enums, `match` expressions, and the `if` `then` `else` control flow construct.

Finally, some appendixes contain useful information about the language in a more reference-like format. [**Appendix A**](appendix-01-keywords.md) covers Calyxium’s keywords, [**Appendix B**](appendix-02-operators.md) covers Calyxium’s operators and symbols and [**Appendix C**](appendix-03-functions.md) covers Calyxium's built-in functions.

There is no wrong way to read this book: if you want to skip ahead, go for it! You might have to jump back to earlier chapters if you experience any confusion. But do whatever works for you.

The website version also contains a handy search feature over <span id="arrow" style="display: inline-block; transition: transform 0.2s ease; font-size: 2em; transform-origin: center;">↑</span> &nbsp;&nbsp;which you can use to search for Code Snippets in [**Appendix D**](appendix-04-codebytes.md) or for anything else you can think of.

<style>
  #highlight-target {
    transition: box-shadow 0.2s ease, filter 0.2s ease;
  }

  .highlighted {
    box-shadow: 0 0 10px 3px #00ffff;
    filter: brightness(1.5);
  }
</style>

<script>
  const arrow = document.getElementById('arrow');
  const target = document.getElementById('search-toggle');

  function updateArrowRotation() {
    if (!arrow || !target) return;

    const arrowRect = arrow.getBoundingClientRect();
    const targetRect = target.getBoundingClientRect();

    const arrowX = arrowRect.left + arrowRect.width / 2;
    const arrowY = arrowRect.top + arrowRect.height / 2;
    const targetX = targetRect.left + targetRect.width / 2;
    const targetY = targetRect.top + targetRect.height / 2;

    const angleRad = Math.atan2(targetY - arrowY, targetX - arrowX);
    const angleDeg = angleRad * (180 / Math.PI);

    arrow.style.transform = `rotate(${angleDeg + 90}deg)`;
  }

  arrow.addEventListener('mouseenter', () => target.classList.add('highlighted'));
  arrow.addEventListener('mouseleave', () => target.classList.remove('highlighted'));

  window.addEventListener('load', updateArrowRotation);
  window.addEventListener('resize', updateArrowRotation);
  document.addEventListener('scroll', updateArrowRotation);
</script>