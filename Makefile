
# define a variable to check if any files not up to date
.PHONY : all

all : allPhaseSpace.png energy.png energyWithErr.png\
ErrorOsc_x0_1.0_v0_0.0_h_0.003.png EulerOsc_x0_1.0_v0_0.0_h_0.003.png\
expPhaseSpace.png impEnergy.png impEnergyWithErr.png\
impErrorOsc_x0_1.0_v0_0.0_h_0.003.png impEulerOsc_x0_1.0_v0_0.0_h_0.003.png\
impPhaseSpace%png manyErrors.png symEnergy.png symEnergyWithErr.png\
symPhaseSpace.png log.txt Homework4.pdf

allPhaseSpace%png energy%png energyWithErr%png\
ErrorOsc_x0_1.0_v0_0.0_h_0.003%png EulerOsc_x0_1.0_v0_0.0_h_0.003%png\
expPhaseSpace%png impEnergy%png impEnergyWithErr%png\
impErrorOsc_x0_1.0_v0_0.0_h_0.003%png impEulerOsc_x0_1.0_v0_0.0_h_0.003%png\
impPhaseSpace%png manyErrors%png symEnergy%png symEnergyWithErr%png\
symPhaseSpace%png :
	python HarmOsc.py

# Make git log
log.txt :
	git log > $@

# Make the LATEX file
Homework4.pdf : Homework4.tex
	pdflatex $^