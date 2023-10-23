### Ecoevolity conexões com AM3
# 2 pops: AM3 e AF


### agora sim, rodando o progrAM3a

ecoevolity --relax-missing-sites ecoevolity-config-con-AM3.yml


### corrida 2
ecoevolity --relax-missing-sites ecoevolity-config-con-AM3.yml

## corrida3

ecoevolity --relax-missing-sites ecoevolity-config-con-AM3.yml

#Assessing mixing and convergence
#Now, let’s use the pyco-sumchains tool of the pycoevolity packages to help assess the convergence of our chains and choose what number of sAMples we want to remove as “burn in”:

pyco-sumchains -s 100 ecoevolity-config-con-AM3-state-run-1.log ecoevolity-config-con-AM3-state-run-2.log ecoevolity-config-con-AM3-state-run-3.log

pyco-sumchains -s 100 ecoevolity-config-con-AM3-state-run-1.log ecoevolity-config-con-AM3-state-run-2.log ecoevolity-config-con-AM3-state-run-3.log > pyco-sumchains-table.txt

#Summarizing divergence-model posterior probabilities

sumcoevolity -b 101 -c ecoevolity-config-con-AM3.yml -n 1000000 ecoevolity-config-con-AM3-state-run-1.log ecoevolity-config-con-AM3-state-run-2.log ecoevolity-config-con-AM3-state-run-3.log

#Plotting posterior probabilities of the number of events

pyco-sumevents sumcoevolity-results-nevents.txt

# Plotting marginal divergence times

pyco-sumtimes -b 101 -z ecoevolity-config-con-AM3-state-run-1.log ecoevolity-config-con-AM3-state-run-2.log ecoevolity-config-con-AM3-state-run-2.log ecoevolity-config-con-AM3-state-run-3.log

#SAMpling the prior distribution

ecoevolity --ignore-data --prefix "prior-" --relax-triallelic-sites --relax-missing-sites ecoevolity-config-con-AM3.yml

# CORRIDA 2

ecoevolity --ignore-data --prefix "prior-" --relax-triallelic-sites --relax-missing-sites ecoevolity-config-con-AM3.yml

#Now, you can use pyco-sumchains and Tracer to make sure both MCMC chains that sAMpled from the prior converged and mixed well, and to determine an appropriate number of sAMples to remove as burn-in:

pyco-sumchains -s 100 prior-ecoevolity-config-con-AM3-state-run-?.log > prior-pyco-sumchains-table.txt

# Now, to summarize the prior sAM3ples run:

sumcoevolity -b 101 --prefix "prior-" -c ecoevolity-config-con-AM3.yml -f prior-ecoevolity-config-con-AM3-state-run-?.log

# Open these up and check to see if the “posterior” probabilities are similar to the prior probabilities. I put “posterior” in quotes, because the numbers in these columns are actually the prior probabilities approximated by the MCMC chains that ignored the data.
