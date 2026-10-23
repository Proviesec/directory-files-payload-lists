# Directory and file path wordlists

Path candidates for directory and file discovery during authorized web security work. A matching response is a lead to review, **not proof of a vulnerability**. Lists contain historical entries and have not been tested against every current product or scanner.

## Start here

1. Pick a list from the [catalog](CATALOG.md). The five-entry [sensitive shortlist](directory-best-sensitive-list.txt) is a small starting point; [Proviesec's favorites](directory-proviesec-favorite-list.txt) and [small-fast-list.txt](small-fast-list.txt) are broader. The [full list](directory-full-list.txt) is a large historical archive.
2. Check that the host and paths are in scope. Start with a low request rate and follow the owner's or bug bounty program's rules.
3. Review responses manually. Many sites return the same page or a redirect for nonexistent paths; status code alone does not establish that a file exists or is exposed. Do not publish sensitive response bodies, credentials, or live target URLs in issues or pull requests.

For example, [ffuf](https://github.com/ffuf/ffuf#typical-directory-discovery) accepts a one-path-per-line list. Replace the reserved example hostname with a host you are authorized to assess:

```sh
ffuf -w directory-best-sensitive-list.txt -u https://your-authorized-host.example/FUZZ -rate 2 -t 1
```

[PSFuzz](https://github.com/Proviesec/PSFuzz) is another compatible scanner; check its current command-line documentation before use. The lists themselves make no HTTP requests.

## Choosing and interpreting lists

The [catalog](CATALOG.md) links every text file and describes its role. File names are retained for existing links, even where the name is historical: `top-1000-filenames.txt` currently contains **10,288** entries, and `small-fast-list.txt` contains **4,842**. These names do not imply a measured ranking or scan time. The full archive contains **189,630** entries and can be noisy or expensive to run.

Most path lists contain one candidate per line. Some entries begin with `/`, end with `/`, contain percent encoding, or include placeholders such as `%EXT%` in the admin list. Review and adapt them for your scanner and target; do not assume every line is a ready-to-use URL. The [phpinfo list](directory-phpinfo-list.txt) also contains legacy expression payloads, so it is not a pure path list.

The file in [`payload-response/`](payload-response/best-payload-response-match-list.txt) has a different format: `path | possible response text | ...`. It is a reference for manual response review, **not** a one-path-per-line scanner input. A text marker by itself is not evidence of a security issue.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Explain why a path belongs in a list, when it is useful, and common false positives. Do not add real secrets, private data, or target-specific URLs. The offline [list check](scripts/check_lists.py) catches basic formatting errors and duplicates in maintained lists; it does not validate live results. Large historical lists and the mixed phpinfo list are documented exceptions.

## License and attribution

The wordlists (`*.txt`) and documentation (`*.md`) are licensed under [Creative Commons Attribution 4.0 International](LICENSE) where copyright or database rights apply. When sharing licensed material, credit **Proviesec**, link to [this repository](https://github.com/Proviesec/directory-files-payload-lists) and the [license](https://creativecommons.org/licenses/by/4.0/), and indicate changes. The license does not create rights over unprotected facts or individual common path names. Contributions must be material the contributor is allowed to share under this license.

The Python checker and GitHub Actions workflow are separately licensed under [MIT](LICENSE-CODE).
