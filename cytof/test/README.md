# Wrapper for test.

## Example:

```
rule samtools_sort:
    input:
        "hello"
    output:
        "output.txt"
    params:
        "1"
    threads: 8
    wrapper:
        "https://github.com/wdnlotm/snakemake/new/main"
```
