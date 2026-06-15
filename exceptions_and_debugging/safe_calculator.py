"""
## 1. Safe Calculator with try / except  *(Easy)*

=================================================
SAFE CALCULATOR
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_divide`
that takes two values from the user and
performs a division, but never crashes the
program.

Handle the following error cases gracefully:
   - non-numeric input        -> ValueError
   - division by zero         -> ZeroDivisionError
   - any other unexpected bug -> generic Exception

The function must always return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the result on success,
                         or an error string on
                         failure.

-------------------------------------------------
Debugging Skills to Practice:
- Read the FULL traceback. The last line of a
  traceback names the exception class — match
  it to your `except`.
- Use a temporary print(type(a), type(b))
  before the division to confirm the inputs.
- Insert breakpoint() and step through with
  the Python debugger (pdb) commands:
       n  -> next line
       s  -> step into
       p  -> print a variable
       q  -> quit

-------------------------------------------------
Input Example 1:
safe_divide("10", "2")

Output Example 1:
('ok', 5.0)
Calculation finished

-------------------------------------------------
Input Example 2:
safe_divide("10", "0")

Output Example 2:
('error', 'Cannot divide by zero')
Calculation finished

-------------------------------------------------
Input Example 3:
safe_divide("ten", "2")

Output Example 3:
('error', 'Inputs must be numbers')
Calculation finished
=================================================

"""
def safe_divide(a, b):
    try:
        # Step 1: Handle potential non-numeric inputs by casting to float
        # This will raise a ValueError if inputs are text strings like "ten"
        num1 = float(a)
        num2 = float(b)
        
        # Step 2: Perform the division operation
        # This will raise a ZeroDivisionError if num2 is 0.0
        result = num1 / num2
        
        # If no exceptions were raised, return the success tuple
        return ("ok", result)
        
    except ValueError:
        # Triggers when input cannot be converted to a float
        return ("error", "Inputs must be numbers")
        
    except ZeroDivisionError:
        # Triggers when attempting to divide by zero
        return ("error", "Cannot divide by zero")
        
    except Exception as e:
        # Catch-all block for any other unexpected bug
        return ("error", f"Unexpected error: {str(e)}")
        
    finally:
        # The assignment output shows "Calculation finished" prints in EVERY example case
        print("Calculation finished")


# --- Test Cases matching your examples ---
_name_ =     ' '
if _name_ == "_main_":
    print("--- Test 1 ---")
    print(safe_divide("10", "2"))
    
    print("\n--- Test 2 ---")
    print(safe_divide("10", "0"))
    
    print("\n--- Test 3 ---")
    print(safe_divide("ten", "2"))
