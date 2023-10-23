GENERAL-INFO-START

		seq-file		Thalurania_GPHOCS.txt
		trace-file		tha-mcmc-trace1.out
		num-loci		3321
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


GENERAL-INFO-END


CURRENT-POPS-START

		POP-START
				name		AF
				samples		MPEG71967 d glaFRA165 d glaMBML7695 d glaMCP5497 d glaMZUSP86021 d glaMZUSP87799 d glaMZUSP91154 d glaMZUSP91403 d glaMZUSP92131 d glaMZUSP92450 d watALG58 d watML2735 d watMZUSP85784 d watFMNH392348 d watFMNH392433 d watFMNH399149 d
		POP-END

		POP-START
				name		AM
				samples		PhasupMPEG58252 d PlamysMPEG74361 d colLSU11709 d fanLSU52956 d fanLSU7821 d COUFT0532 d DZ6795 d MC83 d MPEG56990 d MPEG61181 d MPEG62459 d MPEG62460 d MPEG62464 d MPEG65611 d MPEG67698 d MPEG70693 d MPEG74911 d MPEG76967 d MPEG77075 d MZUSP84368 d MZUSP87403 d MZUSP87419 d MZUSP88065 d MZUSP88400 d MZUSP88675 d MZUSP91909 d MZUSP92631 d MZUSP93633 d MZUSP95334 d MZUSP95335 d MZUSP95813 d T17089 d UFG4537 d LSU55204 d LSU5589 d LSU5997 d LSU7383 d 
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


