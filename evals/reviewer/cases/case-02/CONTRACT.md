# Module contract

Review candidate.py for violations of this contract. This minimized quality
checker returns (exit_code, warnings); it never blocks delivery for text quality.
Inputs are strings. Only the three named fields matter; no Markdown parser or
other validation is required. Fields are case-insensitive complete lines, optionally
preceded by whitespace, one dash and whitespace. A value needs a non-whitespace
character on that same line. Prose containing field names is not a field line.

check(text) returns exit code 0 always. warnings contains each missing or empty
field once, in Observable, Environment, Verify order. At least one populated occurrence satisfies a repeated field. Populated field lines produce
no warning for that field. Report trigger, location and consequence for a defect;
return no findings when behavior meets the contract. Do not edit the candidate.
