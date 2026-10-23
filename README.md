# Elixir Training Lesson template

[![DOI](https://zenodo.org/badge/564252010.svg)](https://zenodo.org/badge/latestdoi/564252010)


For instruction on how to use the template, please follow this documentation: 
https://elixir-europe-training.github.io/ELIXIR-TrP-LessonTemplateInstructions-Zensical/


**Any issues?** Contact Geert van Geest (@GeertvanGeest) 



## If working locally

This website is generated with [Zensical](https://zensical.org), the successor to MkDocs and Material for MkDocs.

Clone this repository, then install the dependencies (a virtual environment is recommended):
```bash
pip install -r requirements.txt
```

To refresh the list of repositories from the GitHub API (this is done weekly by the GitHub Action):
```bash
python scripts/parse_gh_api.py
```

To build or preview the site:
```bash
zensical build     # writes the static site to site/
# or
zensical serve     # preview at http://localhost:8000/
```

Check it out with your browser at [http://localhost:8000/](http://localhost:8000/).


## Citation

Please cite as

> Geert van Geest, Elin Kronander, Jose Alejandro Romero Herrera, Nadja Žlender, & Alexia Cardona. (2023). 
> The ELIXIR Training Lesson Template - Developing Training Together (v1.0.0-alpha). Zenodo. 
> https://doi.org/10.5281/zenodo.7913092
