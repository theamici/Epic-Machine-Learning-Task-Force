# Improvements for Task 1
- isolate a stratified 10% of the data at the start for use in final testing of the models
    - from the remaining 90% of the data, make training and validation data
- remove comments and describe our work with markdown cells instead
- remove old code and comments making some calculations on dependencies
    - instead run Theil's U on features/variables in dataset to discover dependencies, and visualize with heatmap https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9 
    - Cramer's V is a subpar version of Theil's U that is symmetrical, such that we only know if 2 variables x and y are associated, but not if for instance x is dependent on y but y is independent of x (which is what we want to know when deciding features to drop)
- remember to better explain HOW we make discoveries (i.e. refer to visualizations and print-outs we make in Jupyter, or link to sources we use that give us domain knowledge), and remember to better explain WHY we choose to act or not act on our discoveries
- run grid search on a single decision trees or a small random forest instead of a full random forest, for the simple reason of time constraints, and use this as a basis for later training of the model

# Things to do for Task 2
- discover english sentences that may need translation or removal: https://pypi.org/project/langdetect/
- use lemmitisation to group words with same root meaning, which should help the model slightly to learn equivalencies: https://spacy.io/models/nb