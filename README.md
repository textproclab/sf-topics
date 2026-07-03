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


## Contents

Available now:

- [`evaluation/topic_judgments.csv`](evaluation/topic_judgments.csv) –
  per-topic judgments for all 195 topics across the four model
  configurations reported in the paper (Tables 2–3).
- [`evaluation/verify_judgments.py`](evaluation/verify_judgments.py) –
  verifies the released judgments against the paper's published tables
  (Tables 2–3).

Coming shortly: the annotation rubric for the coherence and
thematic-content judgments (paper §3.3).

Being cleaned for release (expected by early August 2026): corpus metadata
and bin assignments, the stoplist, preprocessing and MALLET configuration,
the automatic author-concentration computation, and the cross-period
alignment code (cosine + Hungarian matching with permutation null).


### Data dictionary: `topic_judgments.csv`

One row per topic (195 rows). Configurations: `full_k15`, `full_k60`
(whole-corpus LDA), `binned_mallet`, `binned_authorless` (one k=15 model
per temporal bin; the Authorless variant downweights author-specific
vocabulary before fitting).

| Column | Source | Description |
|---|---|---|
| `configuration` | – | Model configuration (see above) |
| `bin` | – | Temporal bin (`pre_1880`, `1880_1899`, `1900_1914`, `1915_1930`) or `full_corpus` |
| `topic_id` | – | Topic index within its model |
| `top_10_words` | model output | Top 10 words by topic-word probability |
| `coherent` | manual annotation | Top words form a recognizable semantic field (Yes/No) |
| `thematic` | manual annotation | Coherent topic whose semantic field captures subject matter rather than register or paratext (Yes/No; empty for incoherent topics, which received no thematic label) |
| `concentration` | computed | Fraction of the topic's top-5 highest-loading chunks contributed by its dominant author (0.2–1.0) |
| `dominant_author` | computed | The author contributing the most top-5 chunks |
| `notes` | manual annotation | Free-text annotation notes |

Coherence and thematic-content labels were assigned by a single annotator
(see the paper's Limitations section). `concentration` and
`dominant_author` are currently populated for the full-corpus
configurations only; the values for the binned configurations will be
added with the pipeline release.


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
[MIT License](LICENSE.md).

The underlying texts are public-domain works from Project Gutenberg,
accessed via the [Sci-Fi-Books-gutenberg](https://huggingface.co/datasets/stevez80/Sci-Fi-Books-gutenberg)
dataset; they are not redistributed here.
