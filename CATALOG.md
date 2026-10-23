# Wordlist catalog

These files contain candidate paths, not verified findings. Existing names are kept for compatibility. Start with a focused list; select the full archive only when its size and noise are appropriate for the authorized assessment.

## Starting points and archives

| File | Contents |
| --- | --- |
| [directory-best-sensitive-list.txt](directory-best-sensitive-list.txt) | 20 configuration, state, credential-file, and backup path candidates; no measured ranking. |
| [directory-proviesec-favorite-list.txt](directory-proviesec-favorite-list.txt) | Proviesec's broader selection; not ranked by measured success. |
| [directory-proviesec-interesting-list.txt](directory-proviesec-interesting-list.txt) | Two upload directory candidates, also present in the upload list. |
| [small-fast-list.txt](small-fast-list.txt) | 4,849 mixed path and filename candidates; “fast” is a historical name. |
| [top-1000-filenames.txt](top-1000-filenames.txt) | 10,202 mostly filename candidates, with some paths; the historical filename does not match its current size. |
| [directory-full-list.txt](directory-full-list.txt) | 189,477-entry historical archive; format-checked, not live-validated. |

The October 2026 refresh adds documented names for [Docker Compose](https://docs.docker.com/compose/intro/compose-application-model/), [Terraform state](https://developer.hashicorp.com/terraform/language/state), [ASP.NET Core settings](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/), and [Spring Boot configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html). Agent-related paths follow [GitHub's instruction-file documentation](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results) and [Cursor's MCP documentation](https://docs.cursor.com/context/model-context-protocol). These sources confirm filenames and roles, not that a public match is sensitive or exploitable.

This refresh also removes 109 host-specific domain paths from the filename list and 10 query or traversal payloads from the fast list. The full archive loses those 119 entries plus 48 malformed or response/payload artifacts. It still contains many historical and target-specific candidates; removal here reflects identifiable list-format or scope problems, not a measured claim that other older paths are ineffective.

## Focused path lists

| File | Contents |
| --- | --- |
| [directory-admin-list.txt](directory-admin-list.txt) | Administration paths; `%EXT%` entries need extension substitution. |
| [directory-apache-list.txt](directory-apache-list.txt) | Apache-related files and server paths. |
| [directory-backup-list.txt](directory-backup-list.txt) | Common backup names and extensions. |
| [directory-config-list.txt](directory-config-list.txt) | Configuration file and directory names. |
| [directory-database-list.txt](directory-database-list.txt) | Database file names. |
| [directory-docker-list.txt](directory-docker-list.txt) | Docker-related configuration names and paths; includes historical project-specific entries. |
| [directory-git-list.txt](directory-git-list.txt) | Git metadata and related names. |
| [directory-grafana-list.txt](directory-grafana-list.txt) | Grafana pages and assets. |
| [directory-kibana-list.txt](directory-kibana-list.txt) | Kibana path candidates. |
| [directory-log-list.txt](directory-log-list.txt) | Log filenames and paths. |
| [directory-phpinfo-list.txt](directory-phpinfo-list.txt) | Mixed legacy paths and expression payloads; not a pure directory list. |
| [directory-phpmyadmin-list.txt](directory-phpmyadmin-list.txt) | phpMyAdmin path variants. |
| [directory-stats-list.txt](directory-stats-list.txt) | Statistics and analytics paths. |
| [directory-swagger-list.txt](directory-swagger-list.txt) | OpenAPI and Swagger documentation paths. |
| [directory-upload-list.txt](directory-upload-list.txt) | Upload directory paths. |

## CMS lists

| File | Contents |
| --- | --- |
| [cms/joomla-payload-list.txt](cms/joomla-payload-list.txt) | Joomla archive filenames. |
| [cms/symfony-payload-list.txt](cms/symfony-payload-list.txt) | Symfony and application path candidates; some are generic. |
| [cms/wordpress-payload-list.txt](cms/wordpress-payload-list.txt) | WordPress files, directories, and historical paths. |

## Response reference

| File | Contents |
| --- | --- |
| [payload-response/best-payload-response-match-list.txt](payload-response/best-payload-response-match-list.txt) | `path | text marker` hints for manual review, not a scanner wordlist. |
