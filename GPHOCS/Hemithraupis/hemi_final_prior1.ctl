GENERAL-INFO-START

		seq-file		Hemithraupis_GPHOCS.txt
		trace-file		hemi-mcmc-trace1.out
		num-loci		4189
		burn-in		0
		mcmc-iterations		300000
		mcmc-sample-skip		0
		start-mig		0
		iterations-per-log		100
		logs-per-line		100

		tau-theta-print		10000
		tau-theta-alpha		1
		tau-theta-beta		5000

		mig-rate-print		0.001
		mig-rate-alpha		0.002
		mig-rate-beta		0.001

		locus-mut-rate		CONST

		find-finetunes		TRUE
		find-finetunes-num-steps		100
		find-finetunes-samples-per-step		100


GENERAL-INFO-END


CURRENT-POPS-START

		POP-START
				name		AF
				samples		Hem_flaFMNH427240 d Hem_flaMBML7574 d Hem_flaML2557 d Hem_flaML2558 d Hem_flaMPEG70525 d Hem_flaMPEG70526 d Hem_flaMZUSP85816 d 
		POP-END

		POP-START
				name		AM
				samples		Hem_flaMPEG59747 d Hem_flaMPEG61610 d Hem_flaMPEG65543 d Hem_flaMPEG72595 d Hem_flaMZUSP86258 d Hem_flaMZUSP96539 d 
		POP-END

CURRENT-POPS-END


ANCESTRAL-POPS-START

		POP-START
				name		root
				children		AF		AM
				tau-initial		0.000005
		POP-END

ANCESTRAL-POPS-END


MIG-BANDS-START

		BAND-START
				source		AF
				target		AM
		BAND-END

		BAND-START
				source		AM
				target		AF
		BAND-END

MIG-BANDS-END


