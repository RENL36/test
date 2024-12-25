.PHONY: apidoc html

# Par défaut, afficher l'aide
help:
	@echo "make apidoc : Générer les fichiers .rst avec sphinx-apidoc"
	@echo "make html : Construire la documentation HTML"
	@echo "make latex : Construire la documentation LATEX"
	@echo "make pdf : Construire la documentation PDF avec pdflatex"
	@echo "make clean : Nettoyer les fichiers temporaires"
	@echo "make cleanall : Nettoyer les fichiers temporaires et la documentation HTML"

# Générer les fichiers .rst avec sphinx-apidoc
apidoc:
	sphinx-apidoc -o docs/sphinx/source . -f

# Construire la documentation HTML
html: apidoc
	$(MAKE) -C docs/sphinx html

# Construire la documentation LATEX
latex: apidoc
	$(MAKE) -C docs/sphinx latex

# Construire la documentation PDF avec pdflatex
pdf: latex
	$(MAKE) -C docs/sphinx/_build/latex all-pdf

# Nettoyer la documentation Sphinx
clean:
	rm -rf docs/sphinx/source
	rm -rf docs/sphinx/_build
	rm -rf docs/sphinx/_static
	rm -rf docs/sphinx/_templates