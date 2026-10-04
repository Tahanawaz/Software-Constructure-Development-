# Student Marks

This project is a refactored Student Marks application for the Software
Construction and Development Week 4 Laboratory Assignment. It separates input,
validation, calculations, grading, and display into clear responsibilities.

## A. Code Archaeology

The original monolithic program combines these responsibilities in one place:

- **INPUT:** asks for the student's name and three marks.
- **VALIDATION:** checks whether each mark is from 0 to 100.
- **CALCULATION:** finds the total and average of the marks.
- **GRADING/BUSINESS RULE:** converts the average into a letter grade.
- **DISPLAY:** prints the completed student result.

Separating these responsibilities makes each part easier to understand, test,
and change.

## B. Responsibility Map

| Responsibility | What it does | Where it belongs |
| --- | --- | --- |
| Input | Reads the name and three marks from the user | `main.py` |
| Validation | Decides whether a mark is in the allowed range | `validation.py` |
| Calculation | Calculates the total and average | `calculations.py` |
| Grading | Applies the grade boundaries | `calculations.py` |
| Display | Prints the final result | `display.py` |

## C. Module Design

- `validation.py` exists so the mark rule is independent of input, calculations,
  and output. It provides `validate_mark()`.
- `calculations.py` holds the business logic. Its functions are
  `calculate_total()`, `calculate_average()`, and `calculate_grade()`.
- `display.py` controls only how results are shown. It should not calculate the
  grade because formatting and grading are different responsibilities.
- `main.py` coordinates the application: it collects input, calls validation,
  calls the calculation functions, and passes the results to the display
  function.

Each module hides its own implementation details. `main.py` does not need to
know how grade boundaries are checked. `calculations.py` does not need to know
the prompts or result layout. `display.py` receives completed values and does
not need the original marks or validation rules.

## D. Dependency Mapping

```text
             main.py
            /   |   \
           ↓    ↓    ↓
   validation calculations display
```

`main.py` depends on all three supporting modules because it coordinates their
functions. The supporting modules do not depend on one another.

`display.py` does not need to know how grades are calculated; it is given the
finished grade to print. Likewise, `calculations.py` does not need to know how
results are printed; it only returns values. If a GUI replaces `display.py`, the
calculation rules can stay unchanged and `main.py` can call the new display
layer.

These are necessary dependencies:

- `main.py` to `validation.py`
- `main.py` to `calculations.py`
- `main.py` to `display.py`

Dependencies from `display.py` to `calculations.py`, or from `calculations.py`
to input and display code, would be unnecessary coupling.

## E. Change Request Test

1. If grading changes to A >= 85, B >= 75, C >= 65, and D >= 55, only
   `calculate_grade()` in `calculations.py` should need modification.
2. If result formatting changes, `display.py` should change.
3. If the validation rule or invalid-mark message changes, the validation or
   input-related implementation should be updated while calculation logic stays
   unchanged. The range rule belongs in `validation.py`; the retry message and
   prompt belong in `main.py`.
4. If a GUI is introduced, the display layer should be replaceable without
   changing `calculations.py`.

## F. Verification

The following cases check normal use, boundaries, invalid data, and another
student:

| Test | Input | Expected result |
| --- | --- | --- |
| Normal marks | 75, 82, 68 | Total 225, average 75, grade B |
| Boundary below D | Average 49.99 | Grade F |
| Boundary D | Average 50 | Grade D |
| Boundary below C | Average 59.99 | Grade D |
| Boundary C | Average 60 | Grade C |
| Boundary below B | Average 69.99 | Grade C |
| Boundary B | Average 70 | Grade B |
| Boundary below A | Average 79.99 | Grade B |
| Boundary A | Average 80 | Grade A |
| Invalid low | -5 | Rejected; user is asked again |
| Invalid high | 105 | Rejected; user is asked again |
| Second student | 45, 55, 65 | Total 165, average 55, grade D |

The application can be run from this directory with:

```text
python main.py
```

## G. Reflection

**What is the difference between functions and modules?**  
A function is a named block of code that performs one task. A module is a Python
file that groups related functions and other code.

**Which module has the strongest cohesion and why?**  
`calculations.py` has strong cohesion because all its functions work with marks
to produce totals, averages, or grades.

**What is one example of coupling?**  
`main.py` is coupled to `validation.py` because it imports and calls
`validate_mark()`. This is necessary, clear coupling.

**How does modularity help when requirements change?**  
It keeps changes local. For example, new grade boundaries can be added in
`calculations.py` without changing input or display code.

**Is any module too broad or too small?**  
`validation.py` and `display.py` are small, but each has one clear responsibility.
For this beginner-sized application, that separation is useful rather than
unnecessary.
