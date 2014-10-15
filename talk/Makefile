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

#INTERACTION=
#INTERACTION=-interaction=batchmode
INTERACTION=-interaction=nonstopmode

LATEX = pdflatex ${INTERACTION}
# -jobname=${JOB_NAME}

####################################################################################################
#
# Rules
#
####################################################################################################

all: pdf figures

# force
f:
	touch ${MASTER}.tex
	$(MAKE)	all

figures: ${FIGURES_PDF}

pdf: ${JOB_NAME}.pdf

${JOB_NAME}.pdf: ${MASTER}.pdf
	cp ${MASTER}.pdf ${JOB_NAME}.pdf

${MASTER}.pdf: ${TEXFILES} ${FIGURES_PDF}
	${LATEX} ${MASTER}
#	${LATEX} ${MASTER}

%.pdf : %.py
	python $^

fast: ${TEXFILES}
	${LATEX} ${MASTER}

clean:
	-rm *.aux *.bbl *.blg *.dvi *.log *.lof *.lot *.toc *.idx *.lgpl *.nav *.out *.snm \
	${JOB_NAME}.pdf

####################################################################################################

.PHONY: f all clean link

####################################################################################################
#
# End
#
####################################################################################################
