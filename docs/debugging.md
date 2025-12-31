# 🐞 SmartDesk Bot – Debugging Notes & Lessons Learned

### Issue: Program Ran but Nothing Printed**

**Cause**: main() was defined but never executed.
**Fix:**

```python
if __name__ == "__main__":
    main()

```

---

### Issue: Infinite Loop Printing `None`**

**Cause**: A state handler did not return a next state.
**Fix**: Ensure every state returns a valid next state, even as a placeholder.

---

### Issue: Crash on Unimplemented State**

**Cause**: Flow transitioned to a state that did not yet exist.
**Fix**: Added a fallback condition in the flow controller.

**Lesson**: Always transition safely, even if a state is not ready yet.

---

### Issue: Infinite Loop in `TROUBLESHOOTING` State**

**Cause**: Free-text input and yes/no confirmation were handled in the same state.
**Fix**:

* `ISSUE_DETAILS` handles descriptive input

* `TROUBLESHOOTING` handles yes/no confirmation

**Lesson:** Each chatbot state should expect one type of input and produce **one clear outcome**.

---

### Issue: Full Sentences Not Recognized in `CATEGORY_SELECTION`**

**Cause**: Keyword-matching logic only checks for exact keywords or digits.
**Workaround**: Users can enter single keywords or digits.

**Lesson**: Document system limitations clearly. AI/NLU can handle full sentences in the future.