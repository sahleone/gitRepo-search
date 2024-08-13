def plot_top_terms(text_combined, most_common=50):
    """
    Plots a horizontal bar chart of the most common terms in the text.
    
    Parameters:
    text_combined (str): The input text.
    most_common (int): The number of top terms to plot.
    
    Returns:
    None: Displays a bar plot of the top terms.
    """
    words = text_combined.split()
    word_counts = Counter(words)
    top_words = word_counts.most_common(most_common)
    terms, frequencies = zip(*top_words)
    
    plt.figure(figsize=(10, 8))
    plt.barh(range(len(top_words)), frequencies, tick_label=terms)
    plt.gca().invert_yaxis()
    plt.xlabel('Frequency')
    plt.title(f'Top {most_common} Terms in Descriptions')
    plt.show()
