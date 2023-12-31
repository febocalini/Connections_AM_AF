#! /usr/bin/env Rscript

library(ggplot2)
library(ggridges)

plot_prior <- TRUE
nevents <- c("1", "2", "3", "4")
posterior_probs <- c(0.000555556, 0.000555556, 0.095, 0.905)
prior_probs <- c(0.019321, 0.116098, 0.3574, 0.507181)
bf_labels <- c("<0.0282", "<0.00423", "0.189", "9.26")
max_prob <- 0.905
bf_position_bottom <- max_prob + (max_prob * 0.04)
bf_position_top <- bf_position_bottom + 0.04
bf_positions <- c()
for (i in 1:length(nevents)) {
    if (i %% 2 == 0) {
        bf_positions = c(bf_positions, bf_position_bottom)
    } else {
        bf_positions = c(bf_positions, bf_position_top)
    }
}

posterior_df <- data.frame(nevents = nevents, probability = posterior_probs, label = rep("posterior", 4))
prior_df <- data.frame(nevents = nevents, probability = prior_probs, label = rep("prior", 4))
if (plot_prior) {
    data <- rbind(posterior_df, prior_df)
    bar_colors <- c("posterior" = "gray30", "prior" = "gray85")
} else {
    data <- posterior_df
    bar_colors <- c("posterior" = "gray30")
}

if (plot_prior) {
    ggplot(data, aes(x = nevents, y = probability, fill = label)) +
        geom_col(position = "dodge") +
        theme_minimal(base_size = 14) +
        theme(legend.title = element_blank()) +
        scale_colour_manual(values = bar_colors) +
        scale_fill_manual(values = bar_colors) +
        labs(x = "Number of events") +
        labs(y = "Probability") +
        annotate("text", x = nevents, y = bf_positions, label = bf_labels)
} else {
    ggplot(data, aes(x = nevents, y = probability, fill = label)) +
        geom_col(position = "dodge") +
        theme_minimal(base_size = 14) +
        theme(legend.title = element_blank()) +
        scale_colour_manual(values = bar_colors) +
        scale_fill_manual(values = bar_colors) +
        labs(x = "Number of events") +
        labs(y = "Probability")
}

ggsave("pycoevolity-nevents.pdf", width = 7.0, height = 4.32623789117, units = "in")
ggsave("pycoevolity-nevents.png", width = 7.0, height = 4.32623789117, units = "in")
r <- tryCatch(
    {
        ggsave("pycoevolity-nevents.svg", width = 7.0, height = 4.32623789117, units = "in")
    },
    error = function(cond) {
        message("An error occurred while trying to save plot as SVG.")
        message("The plot has been saved in PDF and PNG format.")
        message("If you want the SVG file, you may need to install additional R packages.")
        message("Here's the original error message for details:")
        message(cond)
    },
    warning = function(cond) {
        message("A warning occurred while trying to save the plot in SVG format.")
        message("The plot has been saved in PDF and PNG format.")
        message("If you want the SVG file, you may need to install additional R packages.")
        message("Here's the original warning message for details:")
        message(cond)
    },
    finally =  {})
