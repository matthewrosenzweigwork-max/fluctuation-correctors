# Preserved read-only comparison harness failure

After the first complete mathematical diagnostic passed, a --check-only
mode was added to rerun it without writing the stored result. Its first
execution completed all mathematical checks and then failed with:

```
AssertionError: Stored result mismatch: mutation_controls
```

Reason: tuples in newly computed witness metadata became lists after the
existing JSON result was reloaded. Direct Python equality distinguished
these containers despite identical JSON content. This was a comparison
harness error, not a failed mathematical assertion or a changed result.

The failed version is retained as diagnostic_check_only_initial_failed.py.
The active diagnostic.py compares canonical sorted JSON values and its
--check-only rerun passed with exactly the original result: 343,521
assertions, 17 categories, 15 nonvacuous mutation controls. No result count
or mathematical test was relaxed. The corrected version is the only
recommended diagnostic entry point.
