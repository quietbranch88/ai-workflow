# Module contract

Review candidate.py for violations of this contract. This is a minimized module,
not a production installer. Callbacks are supplied by a caller; no real home path
or external services are used. No unrelated input/type validation is required.

sync(mode, backup, write) accepts only install and check. install calls backup
once before write, then returns 0. check returns 0 with neither callback called.
Any other mode raises ValueError before either callback is called. collect is
unsupported. Report concrete trigger, location and consequence for each defect;
return no findings when behavior meets the contract. Do not edit the candidate.
