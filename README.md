# RRAM_work
In this work, we first extracted data of Resistance vs Cumulative probabilities from the Stanford paper.

The cumulative probability is plotted in probability scale which is neither log nor linear. To extract the data using webplot digitizer, we first calculate the Z-score corresponding to the given cumulative probabilities which converts y into a linear scale. Then with those Z-score limit we extract Resistance and Z-score values using webplot digitizer. 

Obtained Z-score is again converted to CDF and then we plot the data in linear as well as probability scale

We also fit the data using polyfit

PDF is calculated
