####################################################################################################
#
# LaTeX Makefile
#
####################################################################################################

JOB_NAME = $(notdir ${PWD})

MASTER = master
TEXFILES = $(wildcard *.tex)
FIGURES_PY = $(wildcard figures/*.py)
FIGURES_PDF = $(patsubst %.py, %.pdf, ${FIGURES_PY})

# VPATH = parts:packages

####################################################################################################
#
# LaTeX options
#
####################################################################################################

LATEX_COMMAND=pdflatex
#LATEX_COMMAND=lualatex

#INTERACTION=
#INTERACTION=-interaction=batchmode
INTERACTION=-interaction=nonstopmode

LATEX = ${LATEX_COMMAND} ${INTERACTION}
# -jobname=${JOB_NAME}

####################################################################################################
#
# Rules
#
####################################################################################################

all: pdf

# force
f:
	touch ${MASTER}.tex
	$(MAKE)	all

pdf: ${JOB_NAME}.pdf

${JOB_NAME}.pdf: ${MASTER}.pdf
	cp ${MASTER}.pdf ${JOB_NAME}.pdf

${MASTER}.pdf: ${TEXFILES}
	${LATEX} ${MASTER}
#	${LATEX} ${MASTER}

fast: ${TEXFILES}
	${LATEX} ${MASTER}

# a3: poster-A3-margin.pdf
# poster-A3-margin.pdf: ${JOB_NAME}.pdf
a3: ${JOB_NAME}.pdf
	# pdfposter -v -m420x297mm -p840x1188mm poster.pdf poster-A3.pdf
	pdfposter -v -p3x3A3 -mA3 -p840x1188mm poster.pdf poster-A3.pdf
	convert -bordercolor white -border 20 poster-A3.pdf poster-A3-margin.pdf

clean:
	-rm *.aux *.bbl *.blg *.dvi *.log *.lof *.lot *.toc *.idx *.lgpl *.nav *.out *.snm *.vrb \
	${JOB_NAME}.pdf

####################################################################################################

.PHONY: f all clean link

####################################################################################################
#
# End
#
####################################################################################################
