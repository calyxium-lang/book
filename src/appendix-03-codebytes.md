# Appendix C: Code Bytes

This appendix contains some commonly used snippet examples in Calyxium; designed to be searched by that search bar up there <span id="arrow" style="display: inline-block; transition: transform 0.2s ease; font-size: 2em; transform-origin: center;">↑</span> &nbsp;&nbsp;&nbsp;give it a try!

> Under Construction

### For loops

As you can see in [Appendix A](appendix-01-keywords.md#deprecated-keywords) `for` loops have been discontinued
and are no longer accessible. For those of you who are used to imperative programming this may seem like a shock;
how am I supposed to loop things? You may ask, well its pretty simple. You use the `rec` keyword. Below is a template `for` loop and how to use it.

```ocaml
let rec iterator(index: int, max: int): unit  {
    if index < max then {
        print(index)
        iterator(index+1,max)
    }
}

iterator(0,9)
```

The following code will run `print` 10 times.\
This is a very simple `for` loop style function but they can get much more 
complex giving you more control than the standard `for` keyword from other languages.
Calling the `iterator` function starts the loop and you pass in index 0 and the max loop value.\
Passing in the values like this is similar to `for i in range(start,end)` in Python.

### While loops

You can do a similar thing for a `while` loop with the following code.\
Currently this will not work as mutable variables need to be added.

```ocaml
let rec iterator(boolean: bool): unit  {
    if boolean then {
        print("I'm a happy while loop!")
        iterator(boolean)
    }
}

iterator(boolean)
```

<script>
  function updateArrowRotation() {
    const arrow = document.getElementById('arrow');
    const target = document.getElementById('search-toggle');
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

  window.addEventListener('load', updateArrowRotation);
  window.addEventListener('resize', updateArrowRotation);
  document.addEventListener('scroll', updateArrowRotation);
</script>