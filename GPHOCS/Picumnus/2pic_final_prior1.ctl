GENERAL-INFO-START

		seq-file		Picumnus_GPHOCS.txt
		trace-file		pic-mcmc-trace1.out
		num-loci		3956
		burn-in		0
		mcmc-iterations		500000
		mcmc-sample-skip		0
		start-mig		0
		iterations-per-log		50
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
		finetune-coal-time		0.1
		finetune-mig-time		0.3
		finetune-theta		0.04
		finetune-mig-rate		0.02
		finetune-tau		0.0000008
		finetune-mixing		0.003


GENERAL-INFO-END


CURRENT-POPS-START

		POP-START
				name		AF
				samples		Pic_perALG97 d Pic_perFMNH399173 d Pic_perML2730 d Pic_perMZUSP85792 d Pic_exiMPEG70711 d Pic_exiMPEG79904 d Pic_exiMZUSP91330 d Pic_exiMZUSP91332 d 

		POP-END

		POP-START
				name		AM
				samples		Pic_bufFMNH391292 d Pic_bufFMNH392528 d Pic_bufMPEG66795 d Pic_bufMPEG70135 d Pic_undMPEG56316 d Pic_undMPEG58336 d Pic_undMPEG59390 d Pic_undMZUSP93718 d 
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
				source		AM
				target		AF
		BAND-END

		BAND-START
				source		AF
				target		AM
		BAND-END

MIG-BANDS-END


