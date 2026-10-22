# Contributing

Corrections and new path candidates are welcome. Keep each addition small and explain its value in the pull request.

For a path list, put one candidate per line without comments or surrounding whitespace. Preserve case, leading slashes, trailing slashes, and percent encoding when they matter. Check for an existing entry before adding a variant. If a value such as `%EXT%` needs substitution, describe it in the pull request.

Include the intended product or use case, expected response signal, likely false positives, and a public reference where possible. Do not submit real credentials, private data, or live target URLs. A login page, status code, or keyword match does not by itself show a vulnerability. AI-generated suggestions require manual review of the path and product terminology.

Only contribute material you may share under [CC BY 4.0](LICENSE), and mention any source or license obligations for adapted lists. The code check and workflow use [MIT](LICENSE-CODE).

Run `python3 scripts/check_lists.py` before submitting. This checks formatting and duplicates offline; it does not send requests or prove that a path exists.
