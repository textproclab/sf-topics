# Tracing Thematic Change in Early English-Language Science Fiction, 1818–1930

Code and data for [Gordon
(2026)](https://doi.org/10.18653/v1/2026.nlp4dh-1.21).

We trace thematic change across 238 public-domain science fiction texts
(1818–1930) using temporally binned LDA, identifying four high-continuity
thematic chains and a broad turn from romantic toward technoscientific
forms. Methodologically: binning buys diachrony, Authorless preprocessing
buys cross-author representativeness – and the two effects should be
evaluated separately. This repository contains the analysis code, annotation
rubric, and judgments for all 195 topics.


## Status of contents

Per-topic judgments and rubric coming by July 4; the full pipeline is being
cleaned for release within the month.


## Citation

```bibtex
@inproceedings{gordon-2026-tracing,
    title = "Tracing Thematic Change in Early {E}nglish-Language Science Fiction, 1818-1930",
    author = "Gordon, Jonathan",
    editor = {Hamilton, Sil  and
      {\"O}hman, Emily  and
      Hicke, Rebecca M. M.  and
      Bizzoni, Yuri  and
      Bax, Axel  and
      Matthews, Jacob A.  and
      H{\"a}m{\"a}l{\"a}inen, Mika},
    booktitle = "Proceedings of the 6th International Conference on Natural Language Processing for the Digital Humanities",
    month = jul,
    year = "2026",
    address = "San Diego, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.nlp4dh-1.21/",
    doi = "10.18653/v1/2026.nlp4dh-1.21",
    pages = "226--235",
    ISBN = "979-8-89176-427-9",
}
```


## License

Code and annotations in this repository are released under the
[MIT License](LICENSE).

The underlying texts are public-domain works from Project Gutenberg,
accessed via the [Sci-Fi-Books-gutenberg](https://huggingface.co/datasets/stevez80/Sci-Fi-Books-gutenberg)
dataset; they are not redistributed here.
