GENERAL-INFO-START

		seq-file		Caryothraustes_GPHOCS.txt
		trace-file		cary-mcmc-trace1.out
		num-loci		3597
		burn-in		0
		mcmc-iterations		1000000
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
				samples		Car_canALG126 d Car_canFMNH427231 d Car_canML2554 d Car_canMPEG70547 d Car_canMPEG70826 d Car_canMPEG79858 d Car_canMPEG79859 d Car_canMZUSP98351 d 
		POP-END

		POP-START
				name		AM
				samples		Car_canMPEG65547 d Car_canMPEG66890 d Car_canMPEG74146 d Car_canMPEG76879 d Car_canMZUSP96549 d Car_can_PN_153 d Car_can_PN_154 d 
		POP-END

		POP-START
				name		sim
				samples		Car_sim_LSUMZ_B1413 d Car_sim_LSUMZ_B1414 d 
		POP-END

		POP-START
				name		pol
				samples		Car_pol_LSUMZ_B18093 d 
		POP-END

CURRENT-POPS-END


ANCESTRAL-POPS-START

		POP-START
				name		AMAF
				children		AF		AM
				tau-initial		0.000004
		POP-END

		POP-START
				name		sp
				children		sim		pol
				tau-initial		0.000004
		POP-END

		POP-START
				name		root
				children		AMAF		sp
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


